# Hive Hands-On (Optional)

This lab runs Hive Metastore and HiveServer2 separately. The metastore is the catalog; HiveServer2 accepts and plans SQL and delegates execution.

| Service or volume | Responsibility |
| --- | --- |
| `metastore` | Catalog API on port `9083`; stores table metadata |
| `hiveserver2` | SQL endpoint on port `10000`; plans and runs lab queries |
| `warehouse` | Persists managed-table data separately from services |
| `./data` | Externally managed sample data |

The lab uses the image's embedded metastore database to stay small. Production HMS normally uses a separate, redundant PostgreSQL, MySQL, or Oracle database.

## Prerequisites and Startup

Use Docker Compose v2, allocate at least 4 GB to Docker, and ensure ports `9083` and `10000` are free.

```bash
docker compose up -d
docker compose ps
docker compose logs --tail=50 metastore hiveserver2
```

Wait until both services are healthy, then connect through HiveServer2:

```bash
docker compose exec hiveserver2 \
  beeline -u 'jdbc:hive2://localhost:10000/default' -n hive
```

## 1. Separate Metadata from Data

```sql
CREATE DATABASE IF NOT EXISTS onboarding_hive;
USE onboarding_hive;

CREATE EXTERNAL TABLE orders_external (
  order_id INT,
  customer_name STRING,
  total_amount DOUBLE,
  order_date STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/data/orders'
TBLPROPERTIES ('skip.header.line.count'='1');

DESCRIBE FORMATTED orders_external;
SELECT * FROM orders_external ORDER BY order_id;
```

Which service accepted the SQL? Which owns the table definition and location? Which path contains CSV bytes? Does HMS read every row to answer the query?

## 2. Inspect the Plan

```sql
EXPLAIN
SELECT customer_name, SUM(total_amount)
FROM orders_external
GROUP BY customer_name;
```

Find the scan, map-side work, shuffle/grouping boundary, and aggregation. Explain where HMS information was required and where compute began.

## 3. Test Lifecycle Boundaries

```sql
DROP TABLE orders_external;
```

Confirm that `SELECT` now fails because the catalog entry is gone, then verify that the external data remains:

```bash
docker compose exec hiveserver2 ls -l /data/orders
```

Recreate the table and confirm the data is queryable without reloading it.

## 4. Discover an Unregistered Partition

This exercise demonstrates that a partition directory and a catalog partition are separate things.

First, create a partitioned external table whose data lives in the shared warehouse volume:

```sql
CREATE EXTERNAL TABLE orders_partitioned (
  order_id INT,
  customer_name STRING,
  total_amount DOUBLE
)
PARTITIONED BY (order_date STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION 'file:///opt/hive/data/warehouse/onboarding_hive.db/orders_partitioned';

INSERT INTO orders_partitioned
PARTITION (order_date='2024-02-10')
VALUES (201, 'Alice Green', 125.50);

SHOW PARTITIONS orders_partitioned;
SELECT * FROM orders_partitioned;
```

Leave Beeline open. In another terminal, inspect the physical layout:

```bash
docker compose exec hiveserver2 \
  find /opt/hive/data/warehouse/onboarding_hive.db/orders_partitioned \
  -maxdepth 2 -type f -o -type d
```

Notice that the partition value is represented by a directory named `order_date=2024-02-10`. Hive created both the directory and its corresponding HMS partition entry.

Now bypass Hive and add another correctly structured partition directly to the filesystem:

```bash
docker compose exec hiveserver2 bash -c \
  "mkdir -p /opt/hive/data/warehouse/onboarding_hive.db/orders_partitioned/order_date=2024-02-15 && \
   printf '202,Bob Stone,89.90\n' > /opt/hive/data/warehouse/onboarding_hive.db/orders_partitioned/order_date=2024-02-15/orders.csv"
```

Back in Beeline, investigate before reading the hint:

```sql
SELECT * FROM orders_partitioned ORDER BY order_date, order_id;
SHOW PARTITIONS orders_partitioned;
```

The new file exists, but its row is absent from the query result. Explain why. Compare the filesystem directories with `SHOW PARTITIONS`, then research how Hive discovers partition directories that were added outside Hive.

<details>
<summary>Hint and solution</summary>

Hive scans only partitions registered in HMS. Adding a correctly named directory does not automatically add catalog metadata. Reconcile the filesystem with the catalog:

```sql
MSCK REPAIR TABLE orders_partitioned;
SHOW PARTITIONS orders_partitioned;
SELECT * FROM orders_partitioned ORDER BY order_date, order_id;
```

The `order_date=2024-02-15` partition and its row should now appear. `MSCK REPAIR` discovered the directory and registered the missing partition in HMS; it did not move or rewrite the CSV.

</details>

Discuss why continuously running `MSCK REPAIR` is not a substitute for adding partitions through the table-writing system, especially for tables with very large partition counts.

## 5. Failure Reasoning

Predict what happens when HiveServer2 stops but HMS is healthy; HMS stops but HiveServer2 is running; or the CSV disappears while its HMS entry remains. Optionally test services with `docker compose stop SERVICE` and restore them with `docker compose start SERVICE`. Do not delete volumes during these tests.

## Completion Checklist

- [ ] Both services became healthy.
- [ ] I can point to metadata, SQL/query, and data components.
- [ ] I created, queried, dropped, and recreated an external table.
- [ ] I identified a shuffle/aggregation boundary with `EXPLAIN`.
- [ ] I compared filesystem partition directories with HMS partition metadata.
- [ ] I explained why directly added partition data was initially invisible and used `MSCK REPAIR` to reconcile it.
- [ ] I can explain the results without treating HMS as the query engine.

## Clean Up

```bash
docker compose down
```

To also delete the lab's named volume, use `docker compose down --volumes`.
