# Hive Metastore & Table Format :

## Overview
Today’s session zeroes in on two foundational pieces of Hive: the metastore that holds metadata and the table formats that define how data is structured on disk. We will avoid any discussion of Hive’s execution engines (MapReduce, Tez, etc.) or query processing. The goal is to understand the storage and metadata layers that other tools in the ecosystem rely on.

**Focus only on metadata management and table/format semantics.**

## Goals
- Understand what the Hive Metastore is and why it exists.
- Learn how Hive tables are defined and how formats describe their physical layout.
- Practice self-directed study and time management.

:warning: **Note:**
- Independence is essential; plan your study day accordingly.
- If you can’t explain a concept clearly, revisit the documentation.
- Review the [Exercise](#exercise) before diving into research.
- Ask your mentor for clarification on scope if needed.

## Hive Metastore

Answer the following five questions to explore the metastore:

1. **Purpose & Function:**  What is the Hive Metastore and what types of metadata does it store? Why is it necessary in a data platform?
2. **Architecture & Backend:**  Describe how the metastore is implemented (standalone service backed by a relational database). What are the common backend databases used?
3. **Schema & Tables:**  What are the key tables in the metastore schema (e.g. DBS, TBLS, SDS, PARTITIONS)? How do they relate to Hive objects?
4. **Extensibility & Clients:**  How do external tools (Spark, Presto, etc.) interact with the metastore? What APIs are available?
5. **Administration:**  What are typical operational tasks around the metastore (backup, repair, migration)? What happens if the metastore is unavailable?

## Hive Table Formats

Answer these five questions to understand table formats:

1. **Definition & Role:**  What does a “table format” mean in Hive? How does it differ from table metadata stored in the metastore?
2. **Common Formats:**  Describe popular formats such as Text/CSV, Parquet, ORC, Avro. How do they impact storage layout and performance?
3. **Schema Evolution:**  How do formats handle schema changes? What features make formats like Avro or Parquet attractive for evolving data?
4. **Serialization/Deserialization (SerDe):**  What is a SerDe and how does it connect format and data? Give examples of built‑in SerDes.
5. **Integration with Storage:**  How do table formats map to physical storage (directories, files)? What conventions does Hive use for partitions, buckets, and file naming?

## Wrapping Up :trophy:
Review your answers with your mentor and make sure you can articulate how the metastore and formats enable interoperability across Hadoop tools.

## Action Items
- Identify areas of metadata or format behavior you want to explore further.
- Prepare questions for the mentor Q&A session.
- Continue linking these ideas to other chapters as part of the Day 01 challenge.

## Recommended Resources
- [Hive Metastore Documentation](https://cwiki.apache.org/confluence/display/Hive/Metastore+Overview)
- [Hive Language Manual – Table Formats](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL)

