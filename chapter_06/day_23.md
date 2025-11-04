# Day 20 - Introduction to Trino Concepts, Terminology, and Architecture :bar_chart:

## Overview
**Goals:**
- Introduce fundamental concepts, terminology, and architecture of Trino.
- Lay the groundwork for understanding and utilizing Trino for distributed query processing and analytics.

:warning: **Note:**
- Understanding Trino's core concepts and architecture is essential for effectively querying and analyzing distributed data sources.


### Read the following concepts from the [Trino Documentation](https://trino.io/docs/current/index.html)
#### Chapter 1: Introduction to Trino
  - **What is Trino?:**
    - Introduction to the Trino project, its history, and its role in the data ecosystem.
  - **Key Concepts and Terminology:**
    - Definitions of essential terms such as catalogs, connectors, sessions, and query stages.
  - **Core Components:**
    - Explanation of the key components in Trino's architecture, including the Coordinator, Worker, and Connector plugins.
  - **Architecture Overview:**
    - High-level overview of Trino's distributed architecture and its components' responsibilities.
  - **Query Execution:**
    - Understanding the lifecycle of a query in Trino, from parsing and planning to execution and result retrieval.


#### Chapter 2: Trino Architecture
  - **High-Level Architecture:**
    - Detailed overview of Trino's distributed architecture, including the roles of Coordinator and Worker nodes.
  - **Communication Protocols:**
    - Understanding communication protocols such as HTTP and Thrift used for inter-node communication and data transfer.
    - How cost-based optimization enhances query performance.
  - **Fault Tolerance:**
    - Overview of fault tolerance mechanisms in Trino to handle node failures and ensure query reliability.

  - **Query Planning and Optimization:**
   - Understand how Trino plans and optimizes queries for efficient execution across distributed data sources.
   - Explore query optimization techniques such as predicate pushdown, join reordering, and cost-based optimization.

#### Chapter 3: Advanced Features and Optimization
  - **Spill To Disk:**
    - Explanation of the spill-to-disk mechanism, its role in handling large queries, and scenarios where it is triggered.
  - **Get Familiar With Supported Storage:**
    - Understanding the integration of Trino with storage systems such as HDFS and S3.
  - **Get Familiar With What Functions & Operators Supported:**
    - Insights into combining functions to create complex expressions for advanced querying.
  - **Get Familiar With How User Defined Functions Supported:**
    - Overview of UDFs in Trino, including how to create and use custom functions to extend Trino's capabilities.

  - **Resource Groups:**
     - Learn how resource groups in Trino are used to control resource allocation and prioritization for different queries or workloads.
     - Understand how Trino’s resource group configuration can optimize query execution by balancing resources across multiple users or query types.
  - **Trino Gateway:**
      - Explore the role of the Trino Gateway in the overall architecture, handling client connections and query routing to Trino coordinators.
      - Understand how the Trino Gateway improves scalability and fault tolerance by acting as a reverse proxy to distribute query load.

### Questions: ❓
1) What is Trino and what problem does it solve?
2) Which data sources are supported by Trino, and how is connectivity achieved?
3) What is the role of the coordinator and worker in Trino?
4) How does Trino achieve high performance and efficiency when query processing?
5) Give an example for a use case where Trino is beneficial?
6) What is the role of a catalog in Trino? How is it configured?
7) How does Trino implement end to end fault tolerance?
8) compare Trino to Hive and Impala:
query complexity, use cases, performance and more.
9) How does Trino optimize queries involving joins or aggregations across large datasets?
10) How does Trino handle data types from different data sources?
11) What are Trino Resource Groups?, How can I configure them?
12) What is Trino Gateway? How can i set up a new Trino Gateway?
13) What authentication and authorization mechanisms are supported by Trino?
14) What are the main downsides or limitations of using Trino?
(Consider factors like query performance at extreme scale, compatibility with certain data sources, operational complexity, or limitations in handling highly transactional workloads.)
15) What is dynamic catalog mangment?
16) What is spi in Trino?

# 🧪 Trino Hands-On Practice: Setting Up Catalogs and Querying External Data

## 🎯 Goals
- Deploy a local Trino environment using Docker Compose.
- Configure Trino catalogs (Hive on MinIO and TPCH).
- Upload data using MinIO and query it using Trino.
- Learn how create Trino query using different catalogs.

📌 **Note:**  
There are several questions in this exercise. Please answer them in a separate file and send them to your mentor.

---

### 🧱 Step 1: Environment Setup

Clone the starter repository and start the environment:

```bash
git clone https://github.com/883G/Onboarding-Newbies.git
cd ./Onboarding-Newbies/chapter_06/exercise_files/trino-compose
docker compose up -d
```

This will start the following services:
- **Trino**
- **MinIO** (S3-compatible object storage)
- **Hive Metastore**
- **PostgresDB** (used by Hive Metastore for metadata storage)

Access the interfaces:
- Trino UI: 👉 [http://localhost:8080](http://localhost:8080)
- MinIO UI: 👉 [http://localhost:9000](http://localhost:9000)

**Login credentials for MinIO:**

```
Access Key: trino-compose  
Secret Key: trino-compose
```

---

### 📁 Step 2: Upload External Data to MinIO

1. Open MinIO UI.
2. Create a **new bucket** named: `warehouse` (Don`t create it as path under datalake! create your own bucket!)
3. Upload the provided CSV file located at:
   ```
   chapter_06/exercise_files/assets/orders_sample.csv
   ```
   into the following path:
   ```
   /warehouse/orders_sample.csv
   ```

---

### ⚙️ Step 3: Add a Hive Catalog

1. Create a file named `hive.properties` in the following path:
   ```
   etc/catalog/hive.properties
   ```
2. Add the required configuration for the Hive connector.  
   Refer to the official documentation for help:  
   [Hive Connector – Trino Docs](https://trino.io/docs/current/connector/hive.html)

✍️  Add your config and explanation in the answers file.

> 🧪 It might take some trial and error—don’t be afraid to experiment!

3. Restart Trino to load the new catalog:

```bash
docker compose restart trino
```

✍️ **Answer:** Why is a restart required after adding the catalog? Document your explanation in the answer file.

4. Use Trino CLI:
- Create the `default` schema in the Hive catalog if it doesn't already exist.
- Create an **external table** pointing to the CSV file uploaded to MinIO.
  - Remember to **skip the header** row in the file.
- try quering the newly created table

  > How to use trino cli? </br>
  > Enter Docker Desktop -> Find the Trino container -> Click Exec in the Trino container -> Write ```trino ```

✍️ Document how you created the schema and table in your answers.

---

### 📊 Step 4: Add TPCH Catalog

1. Create a file named `tpch.properties` in:
   ```
   etc/catalog/tpch.properties
   ```
2. Add the TPCH connector configuration as shown in:  
   [TPCH Connector – Trino Docs](https://trino.io/docs/current/connector/tpch.html)

3. Restart the cluster:

```bash
docker compose restart trino
```

4. Query the TPCH catalog to test it, for example scan 10 rows.

---

### 🔀 Step 5: Join Hive and TPCH Data

1. Write a query that **joins data** from both the Hive and TPCH catalogs.  

2. Visit the Trino UI at [http://localhost:8080](http://localhost:8080)

3. Locate the query you just executed and explore the query details like(and explain about those):
- Execution time
- CPU time (explain how come is it longer than the excution time)

✍️ In the answer file, document the join query and **at least 3 query statistics from the Trino Web UI**, and explain what each of them means.

---

### 🧠 Reflection Questions

All answers should be documented in file!

1. What would happen if the catalog file had a typo?  
2. How does Trino query two completely separate data sources in one query(technically)?  
3. What happens if you restart only the Hive Metastore?


## **Wrapping Up:** :hourglass_flowing_sand:
Reflect on today's learning's with your mentor and peers. Discuss potential projects or use cases where you can apply Trino for distributed query processing and analytics. Consider how Trino can enhance your data analysis capabilities and streamline your data workflows.

## Recommended Articles and Videos:
- [Trino Documentation](https://trino.io/docs/current/index.html) - Official documentation to explore Trino's features, architecture, and best practices.
- [Trino Gateway Documentation](https://trinodb.github.io/trino-gateway/) - Official documentation to Trino Gateway.
- [Trino: The Definitive Guide](https://dokumen.pub/trino-the-definitive-guide-sql-at-any-scale-on-any-storage-in-any-environment-2nbsped-109813723x-9781098137236.html) - A comprehensive guide to mastering Trino for distributed query processing and analytics.
- [Trino: An Origin Story](https://www.youtube.com/watch?v=_VUQ-Jh-M68) - A short into video.
-[Trino official youtube channel] (https://www.youtube.com/c/trinodb) - Trino official youtube channel.
