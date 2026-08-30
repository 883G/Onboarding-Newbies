# Hive Hands-On (Optional)

This lab runs Hive Metastore and HiveServer2 as separate services. Use the exercises to determine the responsibility of each service and distinguish metadata from table data and query execution.

Before continuing, inspect `docker-compose.yml`. Identify the services, ports, mounted directories, and named volumes. Predict which component owns each responsibility, then validate your answer during the lab.

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

Before dropping the table, predict what will happen to its metadata and CSV files. Then run the statement:

```sql
DROP TABLE orders_external;
```

Test the query again and inspect the data path:

```bash
docker compose exec hiveserver2 ls -l /data/orders
```

Explain the result, then recreate the table and determine whether the data must be loaded again.

## 4. Discover an Unregistered Partition

In this exercise, investigate the relationship between a partition directory and the information Hive uses when planning a query.

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

Compare the directory layout with the output of `SHOW PARTITIONS`. Record the naming convention you observe.

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

Investigate the result without reading a solution:

1. Prove that the new directory and file exist.
2. Compare the filesystem directories with `SHOW PARTITIONS`.
3. Research why the new row is not visible.
4. Find and run the appropriate Hive command to reconcile the table.
5. Query the table and inspect its partitions again.
6. Explain what changed in metadata and whether Hive moved or rewrote the CSV file.
7. Find a more targeted command for adding one known partition and compare its cost with scanning the full table directory.

## 5. Failure Reasoning

Predict what happens when HiveServer2 stops but HMS is healthy; HMS stops but HiveServer2 is running; or the CSV disappears while its HMS entry remains. Optionally test services with `docker compose stop SERVICE` and restore them with `docker compose start SERVICE`. Do not delete volumes during these tests.

## Completion Checklist

- [ ] Both services became healthy.
- [ ] I can point to metadata, SQL/query, and data components.
- [ ] I created, queried, dropped, and recreated an external table.
- [ ] I identified a shuffle/aggregation boundary with `EXPLAIN`.
- [ ] I compared filesystem partition directories with HMS partition metadata.
- [ ] I explained why directly added partition data was initially invisible and found a command that reconciled it.
- [ ] I can explain the results without treating HMS as the query engine.

## Clean Up

```bash
docker compose down
```

To also delete the lab's named volume, use `docker compose down --volumes`.
