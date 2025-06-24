# Day 20 - Introduction to Trino Concepts, Terminology, and Architecture :bar_chart:

## Overview
**Goals:**
- Introduce fundamental concepts, terminology, and architecture of Trino (formerly known as PrestoSQL).
- Lay the groundwork for understanding and utilizing Trino for distributed query processing and analytics.

:warning: **Note:**
- Understanding Trino's core concepts and architecture is essential for effectively querying and analyzing distributed data sources.

## Morning Session - Understanding Trino Concepts and Terminology

### Read the following chapters from the [Trino Documentation](https://trino.io/docs/current/index.html)
#### Chapter 1: Introduction to Trino

- **Topics Covered:**
  - **What is Trino?:**
    - Introduction to the Trino (formerly PrestoSQL) project, its history, and its role in the data ecosystem.
  - **Key Concepts and Terminology:**
    - Definitions of essential terms such as catalogs, connectors, sessions, transactions, and query stages.
  - **Core Components:**
    - Explanation of the key components in Trino's architecture, including the Coordinator, Worker, and Connector plugins.
  - **Architecture Overview:**
    - High-level overview of Trino's distributed architecture and its components' responsibilities.
  - **Query Execution:**
    - Understanding the lifecycle of a query in Trino, from parsing and planning to execution and result retrieval.

#### Core Concepts

##### 1. **What is Trino?:**
   - Understand the history and evolution of Trino (formerly PrestoSQL) and its role in distributed query processing.
   - Explore Trino's features and capabilities for interactive querying and analytics.

##### 2. **Key Concepts and Terminology:**
   - Learn essential terms and concepts used in Trino, including catalogs, connectors, sessions, and transactions.
   - Gain familiarity with Trino's query lifecycle and execution model.

##### 3. **Core Components:**
   - Explore the components that make up Trino's architecture, including the Coordinator, Worker, and Connector plugins.
   - Understand the responsibilities of each component in query planning, execution, and data retrieval.

## Afternoon Session - Exploring Trino Architecture and Optimization

### Read the following chapters from the [Trino Documentation](https://trino.io/docs/current/index.html)
#### Chapter 2: Trino Architecture

- **Topics Covered:**
  - **High-Level Architecture:**
    - Detailed overview of Trino's distributed architecture, including the roles of Coordinator and Worker nodes.
  - **Communication Protocols:**
    - Understanding communication protocols such as HTTP and Thrift used for inter-node communication and data transfer.
  - **Query Planning and Optimization:**
    - Explanation of Trino's query planning and optimization process, including predicate pushdown and cost-based optimization.
    - How cost-based optimization enhances query performance.
  - **Fault Tolerance:**
    - Overview of fault tolerance mechanisms in Trino to handle node failures and ensure query reliability.

#### Core Concepts

##### 1. **High-Level Architecture:**
   - Gain insights into the overall architecture of Trino, including its distributed nature and component interactions.
   - Understand how Trino's architecture enables scalable and efficient query processing across distributed data sources.

##### 2. **Communication Protocols:**
   - Learn about communication protocols used in Trino for inter-node communication and data transfer.
   - Explore techniques for optimizing network communication to enhance query performance.

##### 3. **Query Planning and Optimization:**
   - Understand how Trino plans and optimizes queries for efficient execution across distributed data sources.
   - Explore query optimization techniques such as predicate pushdown, join reordering, and cost-based optimization.

#### Chapter 3: Advanced Features and Optimization

- **Topics Covered:**
  - **Spill To Disk:**
    - Explanation of the spill-to-disk mechanism, its role in handling large queries, and scenarios where it is triggered.
  - **Dynamic Filtering:**
    - Overview of dynamic filtering, including its role in optimizing query execution by reducing scanned data.
  - **Object Storage:**
    - Understanding the integration of Trino with object storage systems such as HDFS and S3.
  - **Functions & Operators:**
    - Insights into combining functions to create complex expressions for advanced querying.
  - **User Defined Functions:**
    - Overview of UDFs in Trino, including how to create and use custom functions to extend Trino's capabilities.

#### Core Concepts

##### 1. **Spill To Disk:**
    - Explanation of Trino’s spill-to-disk mechanism for handling large queries that exceed memory limits.
    - Configuration options and performance considerations.
    - Understand scenarios where spill-to-disk is triggered and how it ensures query reliability.

##### 2. **Dynamic Filtering:**
    - Understanding how dynamic filtering improves query efficiency by reducing scanned data.
    - Use cases and best practices for enabling dynamic filtering.
    - Understand how dynamic filtering works with distributed data sources to optimize resource utilization.

##### 3. **Object Storage:**
    - Learn about Trino’s integration with object storage systems like HDFS and S3.

##### 4. **Functions & Operators:**
    - Overview of built-in functions and operators available in Trino.
    - Examples of using these functions for data transformation and analysis.

##### 5. **User Defined Functions:**
    - How to create and use UDFs for custom processing.
    - Best practices for deploying and managing UDFs in a Trino cluster.

#### Chapter 4: Extra Topics

- **Topics Covered:**
  - **Resource Groups:**
    - Overview of resource groups in Trino, which enable the allocation of compute resources to different query types or users.
  - **Trino Gateway:**
    - Explanation of the Trino Gateway, its role in managing client connections and routing queries to the appropriate Trino coordinators.

#### Core Concepts

##### 1. **Resource Groups:**
     - Learn how resource groups in Trino are used to control resource allocation and prioritization for different queries or workloads.
     - Understand how Trino’s resource group configuration can optimize query execution by balancing resources across multiple users or query types.

 ##### 2. **Trino Gateway:**
      - Explore the role of the Trino Gateway in the overall architecture, handling client connections and query routing to Trino coordinators.
      - Understand how the Trino Gateway improves scalability and fault tolerance by acting as a reverse proxy to distribute query load.

### Questions: ❓
1) What is Apache Trino and what problem does it solve?
2) Can you explain how Trino executes queries across different data sources without moving data?
3) What are the key features of Trino? what it does better than Spark, Hive and Impala?
4) Which data sources are supported by Trino, and how is connectivity achieved?
5) What is the role of the coordinator and worker in Trino's distributed query execution model?
6) How does Trino achieve high performance and efficiency in query processing?
7) Can you describe a use case where Trino would be particularly beneficial?
8) What is the role of a catalog in Trino? and how is it configured?
9) How does Trino handle query retries or failovers to ensure reliability?
10) Compare Trino to Hive,Impala and spark refer to query complexity, use case suitability,performance and more.
11) How does Trino optimize queries involving joins or aggregations across large datasets?
12) How does Trino handle data types from different data sources?
13) How does Trino differ from traditional databases (Postgres, MySQL)?
14) What are Trino Resource Groups, and how are they used for workload management?
15) What is the difference between Trino and Presto?
16) How does Trino integrate with Hive metastore, and why is this integration significant?
17) How does Trino differ from ETL tools in its approach to data integration?
18) How does Trino secure query execution and access to data sources?
19) What authentication and authorization mechanisms are supported by Trino?
20) What is Trino Gateway, and how does it enhance Trino's routing and workload management capabilities?
21) How does Trino Gateway handle query routing across multiple Trino clusters, and what benefits does this provide in multi-cluster deployments?
22) What are the main downsides or limitations of using Trino?
(Consider factors like query performance at extreme scale, compatibility with certain data sources, operational complexity, or limitations in handling highly transactional workloads.)

# 🧪 Trino Hands-On Practice: Setting Up Catalogs and Querying External Data
## 🎯 Goals
* Deploy a local Trino environment using Docker Compose.

* Configure Trino to connect to external data sources (Hive on MinIO and TPCH).

* Upload data using MinIO and query it using Trino.

* Learn how Trino federates data from different catalogs.

🧱 Step 1: Environment Setup
Clone the starter repository or download the setup files provided by your instructor.

Run:
```
git clone https://github.com/883G/Onboarding-Newbies.git
cd ./chapter_06/exercise_files/trino-compose
docker compose up -d
```
This starts the following services:

* Trino

* Minio (S3-compatible storage)

* Hms (Hive Metastore)

* PostgresDb (mainly used by hms)

Access Trino Web UI:
👉 http://localhost:8080

Access MinIO UI:
👉 http://localhost:9000
Login:

Access Key: trino-compose

Secret Key: trino-compose

📁 Step 2: Upload External Data to MinIO
In the MinIO UI:

Create a bucket named warehouse

Upload the provided CSV file (chapter_06/exercise_files/assests/orders_sample.csv) into a folder:
warehouse/orders/


⚙️ Step 3: Add a Hive Catalog
* Create a file named hive.properties in etc\catalog\hive.properties
* Add needed config as shown at [trino docs]("https://trino.io/docs/current/connector/hive.html").

It might take some trail and error, Dont be afraid!

Restart Trino (and anwaer in a file why reatart is needed)?

```
docker compose restart trino
```

In Trino CLI/Web UI, run:
##todo finish
now create schema named default in hive catalog only if not exist (docume)

CREATE TABLE hive.default.orders (
  o_orderkey BIGINT,
  o_custkey BIGINT,
  o_orderstatus VARCHAR,
  o_totalprice DOUBLE,
  o_orderdate DATE,
  o_orderpriority VARCHAR,
  o_clerk VARCHAR,
  o_shippriority INTEGER,
  o_comment VARCHAR
)
WITH (
  external_location = 's3a://warehouse/orders/',
  format = 'CSV',
  skip_header_line_count = 1
);

SELECT * FROM hive.default.orders LIMIT 10;
📊 Step 4: Add TPCH Catalog
Create a file named tpch.properties in trino/catalog/:

properties
Copy
Edit
connector.name=tpch
Restart Trino (again) and verify:

sql
Copy
Edit
SHOW SCHEMAS FROM tpch;
SHOW TABLES FROM tpch.tiny;
Run a simple query:

sql
Copy
Edit
SELECT name, regionkey FROM tpch.tiny.nation LIMIT 5;
🔀 Step 5: Join Hive and TPCH Data
Try a federated query that joins both sources:

sql
Copy
Edit
SELECT
  o.o_orderkey,
  o.o_custkey,
  o.o_orderdate,
  n.name AS nation
FROM
  hive.default.orders o
JOIN
  tpch.tiny.nation n
ON
  o.o_custkey = n.nationkey
LIMIT 10;
🧠 Reflection Questions
What would happen if the catalog file had a typo?

How does Trino query two completely separate data sources in one query?

What happens if you restart only the Hive Metastore?

## **Wrapping Up:** :hourglass_flowing_sand:
Reflect on today's learning's with your mentor and peers. Discuss potential projects or use cases where you can apply Trino for distributed query processing and analytics. Consider how Trino can enhance your data analysis capabilities and streamline your data workflows.

## Recommended Articles and Videos:
- [Trino Documentation](https://trino.io/docs/current/index.html) - Official documentation to explore Trino's features, architecture, and best practices.
- [Trino Gateway Documentation](https://trinodb.github.io/trino-gateway/) - Official documentation to Trino Gateway.
- [Trino: The Definitive Guide](https://dokumen.pub/trino-the-definitive-guide-sql-at-any-scale-on-any-storage-in-any-environment-2nbsped-109813723x-9781098137236.html) - A comprehensive guide to mastering Trino for distributed query processing and analytics.
- [Trino: An Origin Story](https://www.youtube.com/watch?v=_VUQ-Jh-M68) - A short into video.
-[Trino official youtube channel] (https://www.youtube.com/c/trinodb) - Trino official youtube channel.
