# HDFS Hands-On (Optional)

## Overview
This optional lab launches a lightweight HDFS cluster using Docker Compose. The goal is to practice storing and retrieving files in HDFS, inspect block replication, and compare HDFS paths with local filesystem paths.

> This exercise is optional and designed to deepen your understanding of Hadoop Distributed File System storage.

## What You Will Learn
- How to start a NameNode/DataNode HDFS environment
- How HDFS stores files in blocks and replicates them
- How to use `hdfs dfs` commands for file operations
- How to inspect HDFS health and file metadata

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

## Access HDFS
Use the client container to run HDFS commands:

```bash
docker compose exec client bash
```

Then run commands such as:

```bash
hdfs dfs -ls /
hdfs dfs -mkdir -p /user/onboarding
hdfs dfs -put /data/sample_hdfs.txt /user/onboarding/
hdfs dfs -cat /user/onboarding/sample_hdfs.txt
```

## Exercise Tasks

### Task 1: Create HDFS directories
Create a working directory in HDFS for the lab:

```bash
hdfs dfs -mkdir -p /user/onboarding
```

### Task 2: Upload sample data
Copy the sample file into HDFS:

```bash
hdfs dfs -put /data/sample_hdfs.txt /user/onboarding/
```

### Task 3: Inspect file metadata
Check the uploaded file and its HDFS block details:

```bash
hdfs dfs -ls /user/onboarding
hdfs fsck /user/onboarding/sample_hdfs.txt -files -blocks -racks
```

### Task 4: Compare local and HDFS storage
Answer the following:
- Where is the original sample file stored inside the container?
- Where does the HDFS path `/user/onboarding/sample_hdfs.txt` point?
- What is the replication factor for the file?
- How does HDFS make storage fault tolerant?

## Deliverables
- A running HDFS environment from Docker Compose
- Sample data uploaded to HDFS
- HDFS metadata and file block inspection commands
- A short note describing how HDFS replication works

## Clean Up
When finished, stop the environment:

```bash
docker compose down
```
