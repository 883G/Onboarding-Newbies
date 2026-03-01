# Hadoop Distributed File System (HDFS) :elephant:

## Overview
This session focuses on the core concepts of HDFS, the distributed storage layer of the Hadoop ecosystem. Understanding its architecture will help you appreciate how big data clusters store and manage massive datasets across many machines.

**Study the key components, design decisions, and how they work together to provide fault-tolerant, scalable storage.**

## Goals
- Learn the architecture and roles of HDFS components (NameNode, DataNode, etc.).
- Understand how HDFS handles storage, replication, and availability.
- Practice planning a self-study day and managing your time.

:warning: **Note:**
- This is a self-study day; independence and time management matter.
- Focus on grasping the full picture of each concept; if you can’t explain it, you haven’t learned it.
- When in doubt, consult your mentor about what to study.

## Core Concepts

Consider the following five questions to cover the major HDFS topics:

1. **Architecture & Roles:**  Describe HDFS’s overall architecture, including NameNode(s), DataNodes, blocks, and how the namespace and metadata are managed. Don’t forget the role of ZooKeeper in coordinating HA and keeping track of leases.
2. **Storage & Fault Tolerance:**  Explain how HDFS divides files into blocks, uses replication (default factor three), and how it detects and recovers from node failures.
3. **Topology Awareness & Performance:**  What is rack awareness and why does HDFS replicate across racks? Discuss how block placement, snapshots, and checksums contribute to performance and data integrity.
4. **High Availability & Federation:**  Outline HDFS High Availability (Active/Standby NameNode, JournalNodes) and Federation (multiple namespaces). How do these features improve scalability and uptime?
5. **Protocol & Operations:**  Describe how clients read and write data to HDFS via RPC, how they locate NameNodes and DataNodes, how DataNodes send block reports, and why these mechanisms matter for everyday operations. Cover the runtime behaviour of leases and pipeline formation.

## Wrapping Up :trophy:
Review your answers with your mentor and discuss any unclear points. Relate these concepts back to real-world usage scenarios you might encounter.

## Action Items
- Note topics you want to investigate further.
- Prepare questions for the mentor Q&A session.
- Continue the Day 01 challenge by linking these HDFS concepts to other chapters.

## Recommended Resources
- [Official HDFS User Guide](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsUserGuide.html)
- *Hadoop: The Definitive Guide* (O'Reilly) – chapters covering HDFS architecture and administration.

