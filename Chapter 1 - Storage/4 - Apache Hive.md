# Apache Hive

## Overview

Hive includes several cooperating responsibilities. As you research, distinguish catalog and metadata management, SQL planning, distributed compute, and storage. Identify which Hive or Hadoop component performs each responsibility and how external engines such as Trino and Spark interact with them.

> **Mental model:** HMS answers *“What is the table and where is it?”* The query engine answers *“How will this query run?”* Storage answers *“Where are the bytes?”*

## Goals and Timeline

In one study day, learn to:

- Explain the boundary between catalog, query engine, compute framework, and storage.
- Relate logical Hive tables to physical files and directories.
- Trace HiveQL from submission to distributed execution.
- Explain MapReduce independently and compare it with Tez.
- Apply the model in the optional local lab.

Review the [completion checklist](#trainee-completion-checklist) before starting, then hold a mentor Q&A. Focus on cause and effect rather than memorized definitions.

## Research Assignments

### 1. Hive's Purpose and Place in the Ecosystem

Research why Apache Hive was created and where it fits in the Hadoop ecosystem. Explain the types of workloads it is designed for, the abstractions it adds above distributed storage, and how its approach differs from traditional database systems.

### 2. Hive Architecture

Draw the architecture of a production-style Hive environment. Include every component required for a client to submit a query, obtain metadata, execute distributed work, and access table data. Explain the responsibility of each component as well as every connection, protocol, deployment boundary, and important failure scenario.

Your explanation should make clear which responsibilities belong to the catalog, query processing, distributed compute, and storage. Consider how other engines can interact with components from this architecture without using Hive to execute their queries.

### 3. Hive Tables and Storage

Choose one Hive table and investigate its complete lifecycle: definition, schema, storage location, file format, data loading, schema changes, partitioning, querying, and deletion. Demonstrate how its logical definition relates to the files and directories in storage, and explain the important design choices at each stage.

### 4. Hive Metastore Investigation

Examine the Hive Metastore ERD and trace how a database, table, storage descriptor, columns, and partitions are represented. Select at least three central metastore tables and explain how their relationships reconstruct a Hive table definition.

### 5. Dedicated MapReduce Exercise: WordCount

Research MapReduce using [A Day in the Life of a Hive Query](https://community.cloudera.com/t5/Community-Articles/A-Day-In-the-Life-of-a-Hive-Query/ta-p/287905) and the [official MapReduce tutorial](https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html).

Explain how the classic MapReduce WordCount program works from input to final output. Describe the mapper input and output, shuffle and sort, reducer input and output, and which operations run in parallel. Use concrete key/value pairs in your explanation. Then explain why executing a multi-stage Hive query with MapReduce can be expensive and how Tez differs.

### 6. Metadata Inconsistency

In which situations can the partition metadata in Hive Metastore become inconsistent with the directories in the filesystem? Explain how this affects query results, how the inconsistency can be detected and repaired, and when a targeted metadata update is preferable to scanning the entire table location.

## Optional Hands-On

Complete the [Docker Compose lab](./Hive%20Hand%20On%20(optional)/README.md) to inspect catalog and query services separately, create an external table, run `EXPLAIN`, and observe metadata and data lifecycles.

## Trainee Completion Checklist

- [ ] I can explain why Hive exists and the kinds of workloads for which it is designed.
- [ ] I can draw Hive's architecture and trace a query from a client to the data and back.
- [ ] I can distinguish catalog, query processing, distributed compute, and storage responsibilities.
- [ ] I can explain the lifecycle of a Hive table and relate its definition to physical storage.
- [ ] I can use the HMS ERD to trace the metadata behind a table.
- [ ] I can explain WordCount using concrete MapReduce key/value pairs.
- [ ] I can explain why Tez can improve multi-stage Hive queries.
- [ ] I can diagnose a mismatch between partition metadata and filesystem directories and compare repair approaches.
- [ ] I cited the resources I used and recorded my remaining questions for the mentor.

## Recommended Resources

- [Apache Hive design overview](https://hive.apache.org/development/desingdocs/design/)
- [Hive Metastore overview](https://cwiki.apache.org/confluence/display/Hive/Metastore+Overview)
- [MapReduce video](https://youtu.be/cvhKoniK5Uo?si=MGoozk3SU-uOCGEA) — **Recommended viewing while learning about MapReduce.** It provides a visual explanation to reinforce the map, shuffle and sort, and reduce stages.
- [Hive on Tez design](https://hive.apache.org/development/desingdocs/hive-on-tez/)

Review your research and checklist with your mentor. The chapter is complete when you can explain the system in your own words and diagnose a problem by layer instead of only saying that “Hive is broken.”
