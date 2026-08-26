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

## 1. Catalog and Metadata Management

1. What metadata does HMS store for databases, tables, columns, partitions, locations, and statistics? Which information is metadata, and which remains in HDFS or object storage?
2. Why is HMS commonly a standalone service backed by a relational database? What are the separate responsibilities of the service and database?
3. How do metastore tables such as `DBS`, `TBLS`, `SDS`, and `PARTITIONS` relate?
4. How do Hive, Trino, and Spark interact with HMS? Why does sharing a catalog not mean sharing a query engine?
5. What can still work if HiveServer2 is unavailable but HMS is healthy? What fails if HMS is unavailable, even when files and compute are healthy?
6. What administrative work does HMS require (backups, schema upgrades, migrations, statistics, and metadata repair)?

## 2. Tables, File Formats, and Storage

1. Distinguish a table definition in HMS, a file format, and a table format. Do not use “Hive format” as a substitute for all three.
2. Compare CSV/Text, Avro, Parquet, and ORC by layout, encoding, compression, schema handling, and scan performance.
3. Compare managed and external tables. Who controls their data lifecycle, and what should happen to files when each is dropped?
4. How does a logical table map to locations, directories, and files?
5. How are partitions and buckets represented in metadata and storage? How can they become inconsistent?

## 3. Query Planning and Execution

1. Trace a query through submission, parsing, semantic analysis, metadata lookup, logical optimization, physical planning, execution, and result delivery. Name the responsible component at each step.
2. How is a query divided into stages and tasks, and how do intermediate results move between stages?
3. What does `EXPLAIN` reveal? Find table scans, filters, shuffles, joins, aggregations, and writes in an example.
4. How can a Tez DAG avoid the rigid boundaries and repeated durable intermediate writes of chained MapReduce jobs?
5. For the same HMS table, compare queries submitted to HiveServer2, Trino, and Spark. What is shared, and what is independent?

## 4. Dedicated MapReduce Exercise

Research MapReduce using [A Day in the Life of a Hive Query](https://community.cloudera.com/t5/Community-Articles/A-Day-In-the-Life-of-a-Hive-Query/ta-p/287905) and the [official MapReduce tutorial](https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html).

Answer this independently of the broader Hive questions:

> An `orders` table is stored in HDFS and registered in HMS. Hive runs:
>
> ```sql
> SELECT customer_id, SUM(total_amount)
> FROM orders
> WHERE order_date >= '2026-01-01'
> GROUP BY customer_id;
> ```
>
> Explain how MapReduce executes this query. Describe the mapper input and output, what happens during shuffle and sort, and what each reducer computes. Explain what runs in parallel, identify one possible bottleneck, and clarify the role of HMS. Use concrete key/value pairs rather than only defining the stages.

## 5. Architecture Scenario

Draw the data flow for one HDFS table registered in HMS and queried independently by HiveServer2 and Trino. Include clients, HMS and its database, storage, planners, and compute workers. Label every arrow as metadata, query/control traffic, or table data.

Then compare HMS with one alternative catalog. In two short paragraphs, explain its architecture, the problem it solves, and when the department would or would not choose it.

## Optional Hands-On

Complete the [Docker Compose lab](./Hive%20Hand%20On%20(optional)/README.md) to inspect catalog and query services separately, create an external table, run `EXPLAIN`, and observe metadata and data lifecycles.

## Trainee Completion Checklist

- [ ] I can label catalog, planning, compute, and storage in an unfamiliar architecture.
- [ ] I can distinguish table metadata, file format, table format, and data files.
- [ ] I can explain why Trino and Spark use HMS without using Hive as their query engine.
- [ ] I can predict the independent effect of losing HMS, HiveServer2, compute, or storage.
- [ ] I can trace one HiveQL query from client to files and back.
- [ ] I can walk through the MapReduce example using concrete key/value pairs.
- [ ] I can explain why Tez can improve multi-stage Hive queries.
- [ ] I can use `EXPLAIN` to identify a scan, filter, shuffle, and aggregation.
- [ ] I completed the architecture scenario, cited resources, and recorded open questions.

## Recommended Resources

- [Apache Hive design overview](https://hive.apache.org/development/desingdocs/design/)
- [Hive Metastore overview](https://cwiki.apache.org/confluence/display/Hive/Metastore+Overview)
- [MapReduce video](https://youtu.be/cvhKoniK5Uo?si=MGoozk3SU-uOCGEA) — **Recommended viewing while learning about MapReduce.** It provides a visual explanation to reinforce the map, shuffle and sort, and reduce stages.
- [Hive on Tez design](https://hive.apache.org/development/desingdocs/hive-on-tez/)

Review the checklist and scenario with your mentor. The chapter is complete when you can diagnose a problem by layer instead of only saying that “Hive is broken.”
