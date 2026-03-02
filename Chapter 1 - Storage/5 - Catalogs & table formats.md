# Catalogs & Table Formats :

## Overview
This session dives into the metadata layer that sits above raw files in a data
lake or warehouse.  Before we talk about individual systems, start by thinking
about the big picture: what is a *data warehouse* versus a *data lake* versus a
*lakehouse*, and why do teams care about catalogs and table formats in each
case?  (Hint: consistency, governance, and performance are the common threads.)

We’re not going to install or run Spark/Trino/etc.; the material stays at the
metadata level.  That said, good formats enable optimizations such as
partition pruning, predicate push‑down, and efficient file compaction, all of
which have a dramatic impact on execution even though we won’t be executing
anything here.

**We’ll examine why catalogs exist, how they differ from Hive’s metastore
(which is itself just one implementation of a catalog), and the design goals of
modern table formats such as Iceberg, Delta Lake, and Hudi.  Examples of
catalog implementations include Hive Metastore, AWS Glue, Databricks Unity
Catalog, and even simple relational databases; not all of them are tied to
Iceberg.**

## Goals
- Clarify what catalogs and table formats actually manage and why teams put
  them on top of object storage.
- Sketch the difference between a warehouse, a lake, and the newer lakehouse
  idea so you have context for why metadata matters.
- Learn about emerging formats that implement ACID, schema evolution, time
  travel and other optimizations, and why those features make life easier for
  query engines.
- Build on previous lessons by focusing on interoperability and metadata
  management rather than specific execution engines.

:warning: **Note:**
- Self-study requires planning; review the [Exercise](#exercise) before starting.
- Keep the focus on metadata and format, not on query engines or execution.
- Ask your mentor if you're unsure about scope.

## Core Concepts

1. **Data warehouse / lake / lakehouse:**  What are the defining
   characteristics of each?  Why do architects care about a separate metadata
   layer in a lakehouse versus a traditional warehouse?  (Put this question
   first since it sets the context for everything that follows.)

2. **What is a Catalog?**  Describe the purpose of a metadata catalog.  How
   does it compare to Hive Metastore (hint: the metastore *is* a catalog)
   and why might systems introduce separate catalog layers (e.g. AWS Glue,
   Databricks Unity Catalog, in‑house catalog backed by PostgreSQL)?

3. **Catalog Architecture:**  Explain typical components of a catalog service
   (namespace management, table and partition metadata, permissions).  What
   backend storage is used?  Is the catalog itself just a database, or does it
   also manage pointers to objects in a blob store?

4. **Table Formats Overview:**  Define what a table format is in the context of
   a data lake.  How do formats like Iceberg, Delta, and Hudi differ from
   simple Hive/Parquet tables?  What features do they add (ACID, snapshots,
   partition evolution, optimizations such as pruning and predicate push‑down)?

5. **Metadata & Transaction Log:**  How do modern formats store their own
   metadata?  Discuss the concept of a transaction log or manifest file, and
   the distinction between file‑level metadata (e.g. Iceberg data file footers)
   and catalog entries.  When would you even need to think about files if the
   catalog abstracts them away?  (Answer: when debugging, cleaning up
   orphan files, or understanding performance.)

6. **Interoperability & Ecosystem:**  Describe how catalogs and formats enable
   multiple compute engines to work on the same data (Spark, Trino, Flink).
   Why is standardization important?  What role do open specifications
   (e.g. Apache Iceberg spec) play?

## Wrapping Up :trophy:
Review your answers with your mentor, focusing on how catalogs and formats enable a consistent data platform across tools.

## Action Items
- Identify catalogs or formats you’d like to try in practice.
- Prepare questions for the mentor Q&A session.
- Link these ideas back to the [intro chapter](../Chapter%200%20-%20Intro/1%20-%20Big%20Data%20Core%20Concepts.md).

