# File Systems Fundamentals :
## Overview
This session introduces the basic ideas that apply to most file systems, whether they run on a single machine or across a cluster. The goal is to understand how data is organized, managed, and accessed so you can speak intelligently about storage technologies.

**We will focus on general concepts such as hierarchy, metadata, block allocation, and performance trade-offs.**

## Goals
- Develop a foundational understanding of how file systems work.
- Learn the common components and terminology used by most file systems.
- Practice planning a self-study day and estimating time for learning.

:warning: **Note:**
- This is a self-study day. Independence and time management are essential.
- Many newcomers struggle with self-study; take a moment to plan your day and stick to it.
- Understand the **big picture** of each concept. If you can't explain it, you probably haven't learned it.
- Be prepared to describe how concepts relate to one another and to real-world scenarios.
- Review the [Exercise](#exercise) before diving in so you know what to focus on.
- When in doubt about what you need to learn, ask your mentor.

### Core Concepts

Think through the following questions; by answering them you’ll touch every major topic listed above:

1. **Hierarchy, Metadata & Lookup:**  Describe how a file system organizes files in a namespace, how it separates metadata from content (e.g. using inodes), and explain the steps taken to resolve a path like `/home/user/docs/report.txt` to the underlying data.

2. **Storage & Allocation:**  Explain block allocation strategies (contiguous, linked, indexed, extent‑based), discuss what internal and external fragmentation are, and outline how performance is impacted by file size and access patterns (small vs. large files, sequential vs. random).

3. **Directories, Indexing & Permissions:**  Compare different directory indexing methods (linear lists, hash tables, B‑trees) and why efficient lookup matters. Then describe common permission models such as UNIX mode bits and ACLs, and how access control integrates with directory lookup.

4. **Consistency, Journaling & Caching:**  Why do file systems employ journaling or copy‑on‑write logs? What problems do these techniques address, and how do caching and write buffering interact with crash recovery and power‑failure scenarios?

5. **Performance Trade‑offs & Distributed Extensions:**  Discuss the key trade‑offs between throughput, latency, and reliability in file systems. Finally, briefly explain how additional concepts like replication, failover, and namespace servers extend these ideas in distributed systems (HDFS, Ceph) without re‑inventing the core principles.

### Real-World Context
Rather than focusing on one technology, think about how these ideas show up in common operating systems (ext4, NTFS, APFS), networked storage (NFS, SMB), and cloud offerings (S3, Azure Blob). Your task is to recognize the underlying principles across implementations.

## Wrapping Up :trophy:
Discuss your answers and any areas of confusion with your mentor. Reflect on how these general concepts will help when you later study specific systems such as HDFS.

## Additional Topics from Review
- The I/O path: what happens when an application calls `read()` or `write()`? Understand the kernel I/O path, page cache, and block layer.
- Mounting & abstraction layers: what “mounting a filesystem” means, and the separation between filesystem, block device, partition, volume manager. These ideas are essential later for containers, cloud disks, distributed storage, RAID/LVM.

## Action Items
- Review your notes and identify topics you want to explore deeper.
- Collect a list of real-world file systems you’d like to examine in future chapters.
- Prepare questions for the upcoming mentor Q&A session.
- Continue the Day 01 challenge by mapping these ideas to future chapters.

