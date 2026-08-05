# HBase Hands-On (Optional)

## Overview
This optional lab launches a lightweight HBase environment using Docker Compose. You'll practice creating HBase tables, loading sample rows, and inspecting column families.

> This exercise is optional and designed to give practical exposure to HBase storage and access patterns.

## What You Will Learn
- How to start HBase with Docker Compose
- How to use the HBase shell to create tables and insert data
- How HBase stores data in column families
- How to scan and describe HBase tables

## Prerequisites
- Docker installed
- Docker Compose available (`docker compose`)
- At least 2 GB of free RAM available for containers

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

## Access HBase
Connect to the HBase shell:

```bash
docker compose exec hbase bash
hbase shell
```

## Exercise Tasks

### Task 1: Create a namespace and table
In `hbase shell`, run:

```ruby
create_namespace 'onboarding'
create 'onboarding:orders', 'info', 'metrics'
```

### Task 2: Insert sample rows
Add sample orders data:

```ruby
put 'onboarding:orders', 'order1', 'info:customer', 'Anna Johnson'
put 'onboarding:orders', 'order1', 'metrics:total', '310.50'
put 'onboarding:orders', 'order1', 'metrics:date', '2024-02-10'

put 'onboarding:orders', 'order2', 'info:customer', 'Marcus Lee'
put 'onboarding:orders', 'order2', 'metrics:total', '85.00'
put 'onboarding:orders', 'order2', 'metrics:date', '2024-02-11'
```

### Task 3: Scan and describe the table
Run:

```ruby
scan 'onboarding:orders'
describe 'onboarding:orders'
```

### Task 4: Compare HBase storage behavior
Answer the following:
- What are column families and why are they important?
- How does HBase store rows differently from a relational table?
- Where does HBase metadata live in this container environment?

## Deliverables
- A running HBase environment from Docker Compose
- A created HBase namespace and table
- Sample rows inserted and scanned successfully
- A short note describing HBase column families and file storage

## Clean Up
When finished, stop the environment:

```bash
docker compose down
```
