# Hive Hands-On (Optional)

## Overview
This optional hands-on lab uses Docker Compose to launch a Hive metastore and Hive server for local experimentation. You'll practice creating Hive databases and tables, loading sample data, and comparing managed vs external tables.

> This exercise is optional, self-contained, and designed for learners who want practical exposure to Hive metadata and table formats.

## What You Will Learn
- How to start Hive using Docker Compose
- How the Hive Metastore stores metadata
- The difference between managed and external tables
- How to create and query Hive tables using `beeline`

## Prerequisites
- Docker installed
- Docker Compose available (`docker compose`)
- At least 2 GB of free RAM available for containers

## How This Lab Works
- `postgres` stores Hive Metastore metadata in a PostgreSQL database.
- `hive` runs the Hive service, including HiveServer2, which executes queries.
- This lab uses container-local storage instead of a full HDFS cluster.
- Sample data is mounted into the container at `/data`, and Hive warehouse files are preserved in `./data/warehouse`.

## Lab Setup
1. Open this folder in a terminal.
2. Inspect `docker-compose.yml`.
3. Start the environment:

```bash
docker compose up -d
```

4. Confirm services are running:

```bash
docker compose ps
```

## Access Hive
This environment includes HiveServer2 and a local warehouse directory for tables.

Connect to Hive using the Hive CLI inside the container:

```bash
docker compose exec hive bash
beeline -u jdbc:hive2://localhost:10000 -n hive -p hive
```

If `beeline` is not available in the container, use the Hive shell command below instead:

```bash
hive
```

## Exercise Tasks

### Task 1: Create a Hive database
In Hive, run:

```sql
CREATE DATABASE IF NOT EXISTS onboarding_hive;
USE onboarding_hive;
```

### Task 2: Create a managed table
Create a managed Hive table for the sample orders data:

```sql
CREATE TABLE IF NOT EXISTS orders_managed (
  order_id INT,
  customer_name STRING,
  total_amount DOUBLE,
  order_date STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
```

Load sample data into the managed table:

```sql
LOAD DATA LOCAL INPATH '/data/sample_orders.csv' INTO TABLE orders_managed;
```

### Task 3: Create an external table
Create an external table using the same CSV data path:

```sql
CREATE EXTERNAL TABLE IF NOT EXISTS orders_external (
  order_id INT,
  customer_name STRING,
  total_amount DOUBLE,
  order_date STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/data/external_orders';
```

Then copy or move the sample file into the external location if needed and refresh the table:

```bash
mkdir -p /data/external_orders
cp /data/sample_orders.csv /data/external_orders/
```

### Task 4: Query the tables
Run these queries and compare results:

```sql
SELECT * FROM orders_managed LIMIT 10;
SELECT COUNT(*) FROM orders_managed;
SELECT * FROM orders_external LIMIT 10;
DESCRIBE EXTENDED orders_external;
```

### Task 5: Compare managed vs external
Answer the following:
- Where is metadata stored for each table?
- What happens if you drop `orders_managed`?
- What happens if you drop `orders_external`?
- How does Hive track the data location for the external table?

## Deliverables
- A running Hive environment from Docker Compose
- A created Hive database and at least two tables
- Query results showing sample data
- A short written summary of the managed vs external table behavior

## Clean Up
When finished, stop the environment:

```bash
docker compose down
```

## Notes
- The sample data file is available at `/data/sample_orders.csv` inside the Hive service container.
- This lab is optional and intended to reinforce Hive table format and metastore concepts.
