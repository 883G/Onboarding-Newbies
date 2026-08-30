# Apache Hive

## Overview

Hive includes several cooperating responsibilities. As you research, distinguish catalog and metadata management, SQL planning, distributed compute, and storage. Identify which Hive or Hadoop component performs each responsibility and how the components interact with one another.

> **Mental model:** HMS answers *“What is the table and where is it?”* The query engine answers *“How will this query run?”* Storage answers *“Where are the bytes?”*

## Timeline

Estimated duration: one study day.

Complete the research assignments, record the sources you used and the questions that remain open, and review your findings with your mentor.

## Research Assignments

### 1. Hive's Purpose and Place in the Ecosystem

Research why Apache Hive was created and where it fits in the Hadoop ecosystem. Explain the types of workloads it is designed for, the abstractions it adds above distributed storage, and how its approach differs from traditional database systems.

### 2. Hive Architecture

Draw the architecture of a production-style Hive environment. Include every component required for a client to submit a query, obtain metadata, execute distributed work, and access table data. Explain the responsibility of each component as well as every connection, protocol, deployment boundary, and important failure scenario.

Your explanation should make clear which responsibilities belong to the catalog, query processing, distributed compute, and storage. Explain which component manages metadata, which components plan and coordinate queries, and which components perform the distributed computation.

- Pay particular attention to **decoupling** in Hive's architecture. Explain which responsibilities can operate independently and why separating metadata management from query execution is useful.

### 3. Hive Tables and Storage

Choose one Hive table and investigate its complete lifecycle: definition, schema, storage location, file format, data loading, schema changes, querying, and deletion. Demonstrate how its logical definition relates to the files and directories in storage, and explain the important design choices at each stage.

### 4. Hive Partitioning

Research partitioning in general and how Hive implements it. Explain how a partitioned table is defined, how partitions affect the filesystem directory structure, and how partitioning can improve or harm query performance. Include the trade-offs involved in choosing partition columns.

### 5. Dedicated MapReduce Exercise: WordCount

Explain how the classic MapReduce WordCount program works from input to final output. Describe the mapper input and output, shuffle and sort, reducer input and output, and which operations run in parallel. Use concrete key/value pairs in your explanation. Then explain why executing a multi-stage Hive query with MapReduce can be expensive and how Tez differs.

### 6. Fault Tolerance

Research fault tolerance in Hive. Consider failures in the services involved in metadata management, query coordination, distributed execution, and storage. Explain which failures a query can recover from, which failures cause it to fail, and what makes recovery possible.

## Optional Hands-On

Complete the [Docker Compose lab](./Hive%20Hand%20On%20(optional)/README.md) to inspect catalog and query services separately, create an external table, run `EXPLAIN`, and observe metadata and data lifecycles.

## Trainee Completion Checklist

- [ ] I can explain why Hive exists and the workloads for which it is designed.
- [ ] I can draw Hive's architecture and distinguish catalog, query processing, compute, and storage.
- [ ] I can explain decoupling between metadata management and query execution.
- [ ] I can trace the lifecycle of a Hive table from its logical definition to its physical data.
- [ ] I can explain how Hive partitioning is represented in the table definition and filesystem.
- [ ] I can explain WordCount, especially shuffle and sort, and compare MapReduce with Tez.
- [ ] I can explain how Hive's components handle failures and where fault tolerance comes from.
- [ ] I recorded the sources I used and my remaining questions for the mentor.

## Recommended Resources

- [MapReduce video](https://youtu.be/cvhKoniK5Uo?si=MGoozk3SU-uOCGEA) — **Recommended viewing while learning about MapReduce.** It provides a visual explanation to reinforce the map, shuffle and sort, and reduce stages.

Review your research and checklist with your mentor. The chapter is complete when you can explain the system in your own words and diagnose a problem by layer instead of only saying that “Hive is broken.”
