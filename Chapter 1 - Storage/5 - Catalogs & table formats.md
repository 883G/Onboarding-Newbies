# Catalogs & Table Formats :

## Overview
This session explores the idea of metadata catalogs and how various table formats sit on top of object storage. The file will mirror the pattern used in previous days: no processing engines, only metadata and format considerations.

**We’ll examine why catalogs exist, how they differ from Hive’s metastore, and the design goals of modern table formats such as Iceberg, Delta Lake, and Hudi.**

## Goals
- Understand the concept of a catalog and its role in a data lake/warehouse.
- Learn about emerging table formats that implement ACID, schema evolution, time travel, etc.
- Build on previous lessons by focusing on interoperability and metadata management.

:warning: **Note:**
- Self-study requires planning; review the [Exercise](#exercise) before starting.
- Keep the focus on metadata and format, not on query engines or execution.
- Ask your mentor if you're unsure about scope.

## Core Concepts

1. **What is a Catalog?**  Describe the purpose of a metadata catalog. How does it compare to Hive Metastore, and why might systems introduce separate catalog layers (e.g. AWS Glue, Databricks Unity Catalog)?

2. **Catalog Architecture:**  Explain typical components of a catalog service (namespace management, table metadata, permissions). What backend storage is used (databases, attaching to object stores)?

3. **Table Formats Overview:**  Define what a table format is in the context of a data lake. How do formats like Iceberg, Delta, and Hudi differ from simple Hive/Parquet tables? What features do they add (ACID, snapshots, partition evolution)?

4. **Metadata & Transaction Log:**  How do modern formats store their metadata? Discuss the concept of a transaction log or manifest file, and the distinction between file-level metadata and catalog entries.

5. **Interoperability & Ecosystem:**  Describe how catalogs and formats enable multiple compute engines to work on the same data (Spark, Trino, Flink). Why is standardization important? What role do open specifications (e.g. Apache Iceberg spec) play?

## Wrapping Up :trophy:
Review your answers with your mentor, focusing on how catalogs and formats enable a consistent data platform across tools.

## Action Items
- Identify catalogs or formats you’d like to try in practice.
- Prepare questions for the mentor Q&A session.
- Link these ideas back to the [intro chapter](../Chapter%200%20-%20Intro/1%20-%20Big%20Data%20Core%20Concepts.md).

