# Isilon OneFS (PowerScale) 🗄️

## Overview
We have migrated our Data Lake from a traditional Cloudera HDFS ecosystem to Dell PowerScale (Isilon). Unlike HDFS, OneFS uses a symmetric architecture where every node is identical and the "NameNode" functionality is distributed across the entire cluster, rather than living on one or two dedicated machines.

**Study how OneFS replaces a centralized NameNode with a fully symmetric, distributed architecture — and how that change ripples through metadata, data protection, and the HDFS protocol layer our Spark clients actually talk to.**

## Goals
- Understand OneFS's symmetric architecture and why it makes traditional "data locality" obsolete.
- Learn how OneFS tracks billions of objects without a centralized, RAM-based NameNode (Inodes, LINs, B-Trees).
- Understand OneFS's data protection model (Forward Error Correction / erasure coding) and how it compares to HDFS's 3x replication.
- Learn how the Job Engine keeps a cluster self-healing and balanced (FlexProtect, AutoBalance, SmartDedupe, SmartPools).
- Understand how OneFS manages identity, security, and quotas across multiple protocols (HDFS, NFS, SMB).
- Learn how clients connect to OneFS and how the HDFS protocol is translated at the presentation layer (SmartConnect, Access Zones).

:warning: **Note:**
- This onboarding contains a lot of material — not all of it is mandatory. Use the topics below to gauge where to focus, and manage your time accordingly.
- This is a self-study topic; independence and time management matter.
- Focus on grasping the full picture of each concept; if you can't explain it, you haven't learned it.
- When in doubt, consult your mentor about what to study.
- **Only if AI was allowed**: AI chat bots are useful for quizzing yourself and fact-checking, but they can be mistaken — ask them to cite Dell documentation wherever possible and to list a bibliography of the sources used.

### ⏳ Timeline
Estimated Duration: 3 Days
- Day 1: Foundation (hardware & architecture) and the logic of storage (metadata & layout).
- Day 2: Data protection (FEC & resilience) and storage efficiency (the Job Engine).
- Day 3: Identity, security & quotas, and connectivity (SmartConnect & the HDFS protocol).

### 📚 Resources
Start here, then search for anything the questions below don't fully answer:
- [Dell InfoHub – Product Documentation](https://infohub.delltechnologies.com/en-sg/t/product-documentation/) – primary documentation hub (non-PDF).
- [Nick Trimbee's Technical Blog](https://infohub.delltechnologies.com/en-us/author/c50944a4-9f36-4bf7-ac51-f69af379ad37/Nick-Trimbee/) – shortened, engineering-focused deep dives from a lead OneFS engineer.

## Core Concepts

Consider the following questions, grouped by area, to cover the major OneFS topics:

### 1. The Foundation: Hardware & Architecture
OneFS uses a symmetric architecture: every node is identical, and there is no dedicated NameNode.

1. **Symmetric Architecture:** How does OneFS's symmetric, "everything is everywhere" design differ from HDFS's NameNode/DataNode split? Why does this make traditional "data locality" obsolete? You don't need to dive deep into the back-end InfiniBand/Ethernet fabric itself — just understand the concept and the role it plays.
2. **Quorum & Group State:** In a 10-node cluster, what is the minimum number of nodes required to maintain a **Write Quorum** ($\lfloor N/2 \rfloor + 1$)? If the cluster splits into two 5-node partitions due to a back-end switch failure, what state does the file system enter?

### 2. The Logic of Storage: Metadata & Layout
Without a centralized RAM-based NameNode, OneFS still needs to track billions of objects.

1. **Inodes & LINs:** What is a **LIN (Logical Inode Number)**, and how do static/dynamic inode structures and B-Trees (the Metatree and LIN Tree) replace the HDFS `FsImage`? If you move a file between directories, does its LIN change, and how does that affect B-Tree lookups?
2. **Data Inlining:** What is Data Inlining, and why is it an optimization for small files (<128KB)? If a file is 8KB and the cluster uses 8KB inodes, how many disk I/O operations are required to read its data and metadata, compared to a 256KB file?

### 3. Data Protection: FEC & Resilience
OneFS replaces HDFS's 3x replication with Forward Error Correction (erasure coding).

1. **FEC & Stripe Width:** How does $N+M$ Forward Error Correction protection work, and why do larger clusters achieve higher usable capacity (80%+) from it? Why does a `+2n` protection policy cost ~50% overhead on a 4-node cluster but only ~11% on a 20-node cluster?
2. **The Write Path:** What are **Neighborhoods** and **Protection Partners**, and how do they manage fault domains in large clusters? When an HDFS client receives a write "ACK" from an Isilon node, where is the data physically located at that moment — RAM, local Journal, remote Journal, or disk? What roles do the Initiator and Participant nodes play?

### 4. Storage Efficiency & the Job Engine
Background jobs keep the cluster self-healing and balanced without manual intervention.

1. **Job Engine & FlexProtect:** What does the Job Engine do, and how do impact policies let background jobs throttle themselves? If you add a single node to a healthy cluster, which process redistributes the data — and does this happen at the block or file level?
2. **AutoBalance & SmartDedupe:** How does AutoBalance rebalance data across nodes as they're added? When SmartDedupe finds a duplicate block and moves it to a **Shadow Store**, what happens to that block if the original file is later deleted — does the space return to the cluster immediately?
3. **SmartPools & Caching:** How do File Pool Policies let SmartPools move data between SSD and HDD tiers? What's the difference between L2 (Global) cache and L3 (SmartFlash) cache, and which one matters more for accelerating HDFS metadata lookups?

### 5. Identity, Security & Quotas
OneFS is a multi-protocol environment (HDFS, NFS, SMB) that must reconcile different identity models.

1. **Identity Management:** A user writes a file via NFS using `UID 501`. A Spark job later reads that file via HDFS using the Kerberos principal `user@REALM`. What OneFS component is responsible for proving these are the same identity?
2. **Smart Quotas:** How does OneFS track **Quota Domains** and enforce quotas without a central NameNode checking every write? What's are the types of Quotas?

### 6. Connectivity & the HDFS Protocol
This is the layer our Spark/Hadoop clients actually interact with.

1. **SmartConnect:** You are connnecting to a SmartConnect zone named `hdfs.datalake.com`, what components do you pass in order to get the node you read a file from?
2. **HDFS Translation & Access Zones:** Since OneFS has no fixed-size "blocks" in the traditional 128MB HDFS sense, how does it respond to an HDFS `getBlockLocations` request? 

### 🔄 Alternatives
Assignment: You are required to research and write a comparative analysis between OneFS (Isilon/PowerScale) and an industry alternative (e.g. traditional HDFS, NetApp, or another scale-out NAS/object platform).
- Deliverable: A written summary (minimum 1 or 2 sentences).
- Focus: Compare performance, architecture, and specific "pain points" this tool solves compared to legacy systems or competitors.
- Goal: You must be able to justify why the department uses this tool for our specific environment.

### 🎯 User Story & Scenario
Assignment: Based on your research and understanding of the department's pipeline, define a concrete Use Case for this technology.
- Deliverable: A written summary example/story (two paragraphs approx.).
- Requirement: Describe a real-world scenario (e.g., a specific client requirement) where this technology is the optimal solution.
- Data Flow: Map out the data flow and explain how this tool integrates with other components in the Data Pipeline.

## Wrapping Up :trophy:
Review your answers with your mentor and discuss any unclear points. Relate these concepts back to how our Spark and Hadoop clients actually read and write data day-to-day.

## Action Items
- Note topics you want to investigate further.
- Prepare questions for the mentor Q&A session.
- Keep a short bibliography of the sources you used — it makes fact-checking with your mentor much faster.

## Recommended Resources

**Foundation & Architecture**
- [OneFS Technical Overview](https://www.delltechnologies.com/asset/en-us/products/storage/industry-market/h10719-wp-powerscale-onefs-technical-overview.pdf) – the primary source for the symmetric architecture.
- [Cluster Composition, Quorum & Group State](https://www.delltechnologies.com/asset/en-us/products/storage/industry-market/h17364-wp-powerscale-onefs-group-state-quorum.pdf) – how the cluster stays consistent during failures.

**Metadata & Layout**
- [OneFS Metadata Explained](https://infohub.delltechnologies.com/en-us/p/onefs-metadata/) – inodes, B-Trees, and the LIN Table.
- [Data Inlining: Performance and Monitoring](https://infohub.delltechnologies.com/en-uk/p/onefs-data-inlining-performance-and-monitoring/) – small-file optimization internals.

**Data Protection**
- [High Availability and Data Protection](https://www.delltechnologies.com/asset/nl-nl/products/storage/industry-market/h10588-wp-powerscale-onefs-data-protection.pdf) – Reed-Solomon erasure coding and resilience.
- [The OneFS Write Process](https://infohub.delltechnologies.com/en-uk/p/onefs-writes/) – Initiator/Participant roles during a write.

**Storage Efficiency & the Job Engine**
- [OneFS Job Engine White Paper](https://www.delltechnologies.com/asset/en-us/products/storage/industry-market/h12570-wp-powerscale-onefs-job-engine.pdf) – FlexProtect, AutoBalance, and impact policies.
- [OneFS Caching Hierarchy](https://infohub.delltechnologies.com/en-uk/p/onefs-caching-hierarchy/) – L1/L2/L3 caching layers.

**Identity, Security & Quotas**
- [Multiprotocol Security Untangled](https://www.delltechnologies.com/asset/en-us/products/storage/industry-market/h13115-wp-emc-isilon-onefs-multiprotocol-security-untangled.pdf) – identity mapping across HDFS/NFS/SMB.
- [SmartQuotas Overview](https://infohub.delltechnologies.com/en-sg/l/storage-quota-management-and-provisioning-with-dell-powerscale-smartquotas-1/overview-4171/) – quota domains and advisory vs. hard quotas.

**Connectivity & the HDFS Protocol**
- [SmartConnect & Network Design](https://infohub.delltechnologies.com/en-sg/l/dell-powerscale-network-design-considerations/smartconnect-multi-ssip-3/) – DNS delegation and the SSIP.
- [OneFS HDFS Reference Guide](https://dl.dell.com/content/docu105997_PowerScale%20OneFS%209.3.0.0%20HDFS%20Reference%20Guide.pdf) – the definitive HDFS protocol translation reference.
