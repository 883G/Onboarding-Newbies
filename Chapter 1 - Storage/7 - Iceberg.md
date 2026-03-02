# Apache Iceberg :

## Overview
Apache Iceberg is an open table format for huge analytic datasets. This day focuses
on Iceberg’s design and how it improves upon traditional Hive/Hive‑format tables.
(In Hive the table metadata and data files are often mixed, whereas Iceberg
separates them cleanly.)

Iceberg offers rich features – schema evolution, hidden partitioning, time
travel, snapshot isolation – but those capabilities come at the cost of a larger
metadata footprint and a more complex transaction log.  For very small tables
or write‑heavy workloads the overhead may outweigh the benefits, which is why
lighter formats such as Ducklake (aimed at simplicity) or plain Hive/Parquet
still make sense in some environments.  Be prepared to discuss both the
advantages and the drawbacks of adopting Iceberg compared to simpler
approaches or newer competitors.

You’ll answer six questions chosen by the user that dive deeply into its
architecture and behavior.  Some of the items explicitly compare Iceberg with
other table formats or catalogs.

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

1. **Performance and trade‑offs:**  In which scenarios does Iceberg improve
   query performance, and when might its metadata overhead degrade performance?
   Compare Iceberg’s speed/cost characteristics to Hive tables, Ducklake, or
   other lightweight formats.  Why would a team choose a simpler layout even if
   it means giving up features such as time travel?

2. **What is Apache Iceberg?**  Explain the problems it solves compared to
   Hive tables (schema evolution, partitioning, consistency, performance),
   and outline the drawbacks or additional complexity it introduces.  Where
   does the extra metadata and transaction log become acceptable versus
   excessive?

3. **Describe the Apache Iceberg table architecture.**  Explain metadata
   files, manifest files, data files, and snapshots and how they relate to
   each other.

4. **What is an Iceberg catalog, and what is its role?**  Explain what a
   catalog manages (table namespace, metadata pointers, commits), why it’s
   required, and how it differs from a metastore.  Clarify that the catalog –
   not the format – mediates concurrency.  List Iceberg catalog
   implementations (Hive Metastore, Nessie, HadoopCatalog, REST/Polaris, AWS
   Glue, Databricks Unity Catalog, Delta Lake’s proprietary catalog, etc.)
   and note that catalogs from other systems (e.g. Delta, Hive) can be used
   with Iceberg tables as well; performance and locking behavior will vary.

5. **How does Iceberg handle concurrent reads and writes?**  Explain snapshot
   isolation, atomic commits, optimistic concurrency control, and conflict
   detection.  Emphasize again that these guarantees come from the catalog
   layer; the Iceberg format itself simply appends metadata files and leaves
   coordination to whatever catalog is in use.  Mention that different catalogs
   (Nessie/Delta/Hive) may provide slightly different semantics.

6. **What maintenance operations does Iceberg require, and why?**  Discuss
   compaction, snapshot expiration, orphan file cleanup, and metadata cleanup.
   In your answer you may also comment on how these maintenance tasks can
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

