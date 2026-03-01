# Apache Iceberg :

## Overview
Apache Iceberg is an open table format for huge analytic datasets. This day focuses
on Iceberg’s design and how it improves upon traditional Hive-style tables.
You’ll answer five questions chosen by the user that dive deeply into its
architecture and behavior.

**Keep the discussion about the format; don’t cover specific engines or query
runtimes.**

## Goals
- Understand Iceberg’s purpose and the problems it solves.
- Learn how tables, catalogs, and transactions work in Iceberg.
- Familiarize yourself with operational tasks for maintaining Iceberg tables.

:warning: **Note:**
- This is self-study; plan your time and focus on the specified questions.
- If anything is unclear, consult the official docs or ask your mentor.

## Core Questions

1. **What is Apache Iceberg?**  Explain the problems it solves compared to Hive tables (schema evolution, partitioning, consistency, performance).

2. **Describe the Apache Iceberg table architecture.**  Explain metadata files, manifest files, data files, and snapshots and how they relate to each other.

3. **What is an Iceberg catalog, and what is its role?**  Explain what a catalog manages (table namespace, metadata pointers, commits), why it’s required, and how it differs from a metastore. Mention common implementations: Hive, Hadoop, REST, Polaris.

4. **How does Iceberg handle concurrent reads and writes?**  Explain snapshot isolation, atomic commits, optimistic concurrency control, and conflict detection.

5. **What maintenance operations does Iceberg require, and why?**  Discuss compaction, snapshot expiration, orphan file cleanup, and metadata cleanup.

## Wrapping Up :trophy:
Go over your answers with your mentor and relate Iceberg features to the earlier
catalog and partitioning chapters.

## Action Items
- Note areas of Iceberg you’d like to explore hands-on.
- Prepare questions for the mentor Q&A session.
- Continue mapping these topics into the Day 01 challenge.

## Recommended Resources
- [Apache Iceberg Documentation](https://iceberg.apache.org/) – official site with spec and guides.
- [Apache Iceberg Definitive Guide](https://www.dremio.com/wp-content/uploads/2023/02/apache-iceberg-TDG_ER1.pdf) - an official book by dream.ioguides.

