# Apache Iceberg :

## Overview
Apache Iceberg is an open table format for huge analytic datasets. This day focuses
on Iceberg’s design and how it improves upon traditional Hive/ Hive format tables.
(In Hive the table metadata and data files are often mixed, whereas Iceberg
separates them cleanly.)
You’ll answer five questions chosen by the user that dive deeply into its
architecture and behavior.  You should also be aware of the format’s trade‑offs
and where other systems such as Ducklake or Delta Lake might be chosen instead.

**Keep the discussion about the format; don’t cover specific engines or query
runtimes.**

## Goals
- Understand Iceberg’s purpose and the problems it solves, as well as its
  limitations and trade‑offs compared with simpler formats.
- Learn how tables, catalogs, and transactions work in Iceberg.
- Familiarize yourself with operational tasks for maintaining Iceberg tables.
- Recognize that the catalog layer—not the format itself—mediates concurrency
  and namespace management.

:warning: **Note:**
- This is self-study; plan your time and focus on the specified questions.
- If anything is unclear, consult the official docs or ask your mentor.

## Core Questions

1. **What is Apache Iceberg?**  Explain the problems it solves compared to Hive tables (schema evolution, partitioning, consistency, performance).
   As part of your answer, note that Iceberg adds complexity in the form of
   additional metadata and a transaction log; discuss scenarios where this
   overhead is acceptable and others where a lighter format may be preferable.

2. **Describe the Apache Iceberg table architecture.**  Explain metadata files, manifest files, data files, and snapshots and how they relate to each other.

3. **What is an Iceberg catalog, and what is its role?**  Explain what a catalog manages (table namespace, metadata pointers, commits), why it’s required, and how it differs from a metastore. Mention common implementations: Hive, Hadoop, REST, Polaris, and cloud‑vendor catalogs such as AWS Glue or Databricks Unity Catalog.  Clarify that the catalog is also responsible for coordinating concurrent
   writes and readers by handing out snapshot information;
   the Iceberg format itself is agnostic to concurrency but relies on the catalog
   to implement optimistic locking and conflict detection.

4. **How does Iceberg handle concurrent reads and writes?**  Explain snapshot isolation, atomic commits, optimistic concurrency control, and conflict detection.  Note that these guarantees are achieved by the catalog layering and by
   appending new metadata files; from the format’s perspective multiple writers
   simply create new snapshots that the catalog must reconcile.  Also mention
   that catalogs vary (NESSIE vs. Hive vs. Delta) so concurrency behavior can
   differ between implementations.

5. **What maintenance operations does Iceberg require, and why?**  Discuss compaction, snapshot expiration, orphan file cleanup, and metadata cleanup.  In your answer you may also comment on how these maintenance tasks can
   impact performance (e.g., coordination overhead during compaction, delays
   while expiring old snapshots) and where trade‑offs exist.

## Wrapping Up :trophy:
Go over your answers with your mentor and relate Iceberg features to the earlier
catalog and partitioning chapters.

## Action Items
- Note areas of Iceberg you’d like to explore hands-on.
- Prepare questions for the mentor Q&A session.
- Continue mapping these topics into the Day 01 challenge.

## Recommended Resources
- [Apache Iceberg Documentation](https://iceberg.apache.org/) – official site with spec and guides.
- [Apache Iceberg Definitive Guide](https://www.dremio.com/wp-content/uploads/2023/02/apache-iceberg-TDG_ER1.pdf) – an official book by Dremio.
- [Ducklake website](https://ducklake.select/) – a newer format that trades
  some of Iceberg’s features for simplicity and performance (see the comparison
  question above).
- [Apache Iceberg GitHub repo](https://github.com/apache/iceberg) for source
  and issue tracking.

