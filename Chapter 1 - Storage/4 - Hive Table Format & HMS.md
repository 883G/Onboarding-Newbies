# Hive: Metastore, Table Formats (storage layer) and Query Execution (compute)

## Overview
This chapter combines two important Hive topics:
- Hive Metastore and table formats, which define metadata and physical storage layout.
- Hive query execution, which explains how Hive uses distributed engines like MapReduce and Tez.

The goal is to give a unified view of Hive as a platform that manages metadata, maps logical tables to storage, and delegates query execution to scalable compute engines.

## Goals
- Understand the Hive Metastore and why central metadata is required.
- Learn how Hive table formats control physical layout and performance.
- See how Hive queries are translated into distributed execution jobs.
- Compare MapReduce and Tez as query execution engines.
- Build a practical mental model for how storage, metadata, and execution fit together.

:warning: **Note:**
- Independence and time management are essential.
- Focus on concept clarity rather than rote memorization.
- Ask your mentor for clarification if any part feels unclear.

### ⏳ Timeline
Estimated Duration: 1 Day
- Day 1: Review Hive metadata, formats, and execution.
- Have a Q&A session with your mentor after studying.

## Hive Metastore

Answer the following questions to explore the metastore:

1. **Purpose & Function:**  What is the Hive Metastore and what types of metadata does it store (databases, tables, columns, partitions, locations, statistics)? Why is a centralized metadata service necessary in a distributed data platform?

2. **Architecture & Backend:**  Describe how the metastore is implemented as a standalone service backed by a relational database. What are common backend databases, and how does the service scale and handle concurrent clients?

3. **Schema & Tables:**  What are the key tables in the metastore schema (e.g. DBS, TBLS, SDS, PARTITIONS)? How do they relate to Hive objects?

4. **Extensibility & Clients:**  How do external engines such as Apache Spark, Trino, and other tools interact with the metastore? What APIs and protocols are used?

5. **Administration:**  What are common administrative tasks (backup, schema upgrades, migration, repair)? What happens if the metastore becomes unavailable, and why is it considered a critical dependency in data platforms?

## Hive Table Formats

Answer the following questions to understand table formats:

1. **Definition & Role:**  What does a “table format” mean in Hive? How does it differ from table metadata stored in the metastore? Explain the relationship between logical schema and physical file layout.

2. **Common Formats:**  Describe popular formats such as Text/CSV, Parquet, ORC, Avro. How do they differ in encoding, compression, columnar storage, and query performance?

3. **Schema & Tables:**  Explain the difference between managed and external tables, including ownership, lifecycle, and storage location semantics. How does the metastore map logical tables to physical data in storage systems like HDFS or object storage?

4. **Integration with Storage:**  How do table formats map to physical storage (directories, files)? What conventions does Hive use for partitions, buckets, and file naming?

## Hive Query Execution: MapReduce and Tez

### Execution Overview
Hive defines tables, schemas, and metadata through the Hive Metastore, but query execution is performed by an underlying processing engine. Historically Hive used MapReduce, and later Apache Tez improved performance by reducing disk I/O and allowing more flexible task graphs.

### Guide Questions❓

Answer these five questions to understand how Hive queries are executed using MapReduce and Tez.

1. **Hive as a Query Platform:**  
   Hive provides tables, schemas, and SQL querying on top of distributed storage systems such as HDFS. Explain Hive’s role as a platform layer that sits above storage and relies on external compute engines to execute queries.

2. **Hive Query Stages and Task Execution:**  
   When Hive translates a SQL query into a distributed job, how is the work divided into stages and tasks? Explain how Hive breaks a query into execution stages, how tasks are distributed across the cluster, and how intermediate results are passed between stages.

3. **Hive Query Execution Pipeline:**  
   What happens when a user runs a query in Hive? Describe the main stages of execution: SQL parsing, logical planning, physical planning, and submitting jobs to an execution engine such as MapReduce or Tez.

4. **MapReduce Fundamentals:**  
   What is the MapReduce programming model? Explain the roles of the `map phase`, `shuffle and sort`, and `reduce phase`. Why was MapReduce originally used as Hive’s execution engine?

5. **Introduction to Apache Tez:**  
   What is Apache Tez, and how does it improve Hive query execution? Explain how Tez replaces chains of MapReduce jobs with a Directed Acyclic Graph (DAG) of tasks, reducing unnecessary disk I/O and improving query performance.

### 🔄 Alternatives
Assignment: Briefly research another distributed processing framework used for large-scale data processing.

- Deliverable: A written summary (1–2 sentences).
- Add a simple real-life use case.
- Focus: What problem does this framework solve compared to MapReduce or Tez?

### 🎯 User Story & Scenario
Assignment: Based on your research and understanding of the department's pipeline, define a concrete Use Case for this technology.
- Deliverable: A written summary example/story (two paragraphs approx.).
- Requirement: Describe a real-world scenario (e.g., a specific client requirement) where this technology is the optimal solution.
- Data Flow: Map out the data flow and explain how this tool integrates with other components in the Data Pipeline.

## Wrapping Up :trophy:
Review your answers with your mentor and make sure you can clearly explain how Hive metadata, table formats, and query execution work together across the data platform.

## Action Items
- Identify areas of Hive metadata, table formats, or execution you want to explore further.
- Look at example Hive query plans to see how jobs are structured.
- Prepare questions for the next mentor Q&A session.
- Think about how metadata and execution choices affect performance and maintainability.

## Recommended Resources
- [Hive Metastore Documentation](https://cwiki.apache.org/confluence/display/Hive/Metastore+Overview)
- [Hive Language Manual – Table Formats](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL)
- [Hive Documentation](https://hive.apache.org/docs/latest/)
- [Hadoop: The Definitive Guide (O'Reilly)](https://piazza-resources.s3.amazonaws.com/ist3pwd6k8p5t/iu5gqbsh8re6mj/OReilly.Hadoop.The.Definitive.Guide.4th.Edition.2015.pdf)
- [Apache Tez Documentation](https://tez.apache.org/)
- [Apache MapReduce Docs](https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html)

