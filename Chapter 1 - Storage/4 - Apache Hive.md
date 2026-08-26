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

### 3. Hive Tables and Storage

Choose one Hive table and investigate its complete lifecycle: definition, schema, storage location, file format, data loading, schema changes, partitioning, querying, and deletion. Demonstrate how its logical definition relates to the files and directories in storage, and explain the important design choices at each stage.

### 4. Hive Metastore Investigation

Examine the Hive Metastore ERD and trace how a database, table, storage descriptor, columns, and partitions are represented. Select at least three central metastore tables and explain how their relationships reconstruct a Hive table definition.

### 5. Dedicated MapReduce Exercise: WordCount

Explain how the classic MapReduce WordCount program works from input to final output. Describe the mapper input and output, shuffle and sort, reducer input and output, and which operations run in parallel. Use concrete key/value pairs in your explanation. Then explain why executing a multi-stage Hive query with MapReduce can be expensive and how Tez differs.

### 6. Metadata Inconsistency

In which situations can the partition metadata in Hive Metastore become inconsistent with the directories in the filesystem? Explain how this affects query results, how the inconsistency can be detected and repaired, and when a targeted metadata update is preferable to scanning the entire table location.

## Optional Hands-On

Complete the [Docker Compose lab](./Hive%20Hand%20On%20(optional)/README.md) to inspect catalog and query services separately, create an external table, run `EXPLAIN`, and observe metadata and data lifecycles.

## Trainee Completion Checklist

- [ ] I can explain why Hive exists and the workloads for which it is designed.
- [ ] I can draw Hive's architecture and distinguish catalog, query processing, compute, and storage.
- [ ] I can trace the lifecycle of a Hive table from its logical definition to its physical data.
- [ ] I can use the HMS ERD to explain how a table and its related metadata are represented.
- [ ] I can explain WordCount, especially shuffle and sort, and compare MapReduce with Tez.
- [ ] I can explain how partition metadata becomes inconsistent with storage and compare repair approaches.
- [ ] I recorded the sources I used and my remaining questions for the mentor.

## Recommended Resources

- [MapReduce video](https://youtu.be/cvhKoniK5Uo?si=MGoozk3SU-uOCGEA) — **Recommended viewing while learning about MapReduce.** It provides a visual explanation to reinforce the map, shuffle and sort, and reduce stages.

Review your research and checklist with your mentor. The chapter is complete when you can explain the system in your own words and diagnose a problem by layer instead of only saying that “Hive is broken.”
