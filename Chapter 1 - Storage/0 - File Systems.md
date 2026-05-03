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

### ⏳ Timeline
Estimated Duration: 0.5 Day
- Day 1: Spent no more than hlaf a day on file systems;
    - Have a Q&A session right after


### Core Concepts

Think through the following questions; by answering them you’ll touch every major topic listed above:

1. **Hierarchy, Metadata & Lookup:**  Describe how a file system organizes files in a namespace, how it separates metadata from content (e.g. using inodes), and explain the steps taken to resolve a path like `/home/user/docs/report.txt` to the underlying data.

2. **Storage & Allocation:**  Explain block allocation strategies (contiguous, linked, indexed, extent‑based), discuss what internal and external fragmentation are, and outline how performance is impacted by file size and access patterns (small vs. large files, sequential vs. random).

3. **Directories, Indexing & Permissions:**  Compare different directory indexing methods (linear lists, hash tables, B‑trees) and why efficient lookup matters. Then describe common permission models such as UNIX mode bits and ACLs, and how access control integrates with directory lookup.

4. **Consistency, Journaling & Caching:**  Why do file systems employ journaling or copy‑on‑write logs? What problems do these techniques address, and how do caching and write buffering interact with crash recovery and power‑failure scenarios?

5. **Performance Trade‑offs & Distributed Extensions:**  Discuss the key trade‑offs between throughput, latency, and reliability in file systems. Finally, briefly explain how additional concepts like replication, failover, and namespace servers extend these ideas in distributed systems (HDFS, Ceph) without re‑inventing the core principles.

### Core Concepts - Answers
1. **Hierarchy, Metadata & Lookup:**
- How FS organizes files in a namespace?\
A namespace is, literally, a space in which to store some names. The FS is responsible to organize user's data in files through a hierarchy of named directories. Its an abstraction layer from how the data actually looks like in the physical layer (stores in blocks) to an api for the users presents the data with tree structure. A logical collection of files, directories, named pipes, links, and other UNIX items and metadata that are arranged in a hierarchy.
- How FS seperates metadata from content?\
A typical FS conosists from layers, while each layer responsible for specific tasks. Different layers responsible to each subject. The file system layers & steps to resolve path `/home/user/docs/report.txt`:
    1. Application Layer (User Interface Layer) - execute commands or programs by the user for the next layers, cli\gui tools. For example `cat /home/user/docs/report.txt`
    2. Logical File System (Metadata Management Layer) - checks if the file exists in the directory structure or not. If the file is presented then it finds the location of the logical block number of the file. In linux th logical FS arranges in file structure of inodes (index node) which stores metadata of the location of the file, timestamp, pointers, permissions, etc. From the inode the information about the pointers of the file goes to the next layer.
    3. File Organization Module (Logical Block Mapping Layer) - gets the logical block number and map it to physical block number (the exact blocks which the file is wrriten in).
    4. Basic File System (Storage Interface Layer) - order commands like read/write to which blocks for the next layer. Implements system calls for low-level disk operation. In this example `read()`
    5. I/O Control Layer (Device Driver Layer) - contains device driver files. Convert generic command of `read block 5` into device specific instructions.
    6. Devices - represents actual storage devices (HDDs, SSDs, USBs, etc)\

The metadata exists in the Logical FS layer which responsible on managing metadata of files. In windows it stores in file allocation tables (FAT) and in unix in inodes. Inode (index node) is the file structure which represents logical files that contains information about the files (file size, owner, permissions, timestamps, file type - in the attribute section). Inode structure has the following components. Direct block, refers to pointers stores directly in the inode. Single indirect block - for larger files, Instead of directly pointing to data blocks, the inode stores a pointer to another block called the indirect block. Double indirect block - for even larger files. the inode points to a block that contains pointers to single indirect blocks. Triple indirect block - For extremely large files, the triple indirect block is used. It points to a block that contains pointers to double indirect blocks. These, in turn, contain pointers to single indirect blocks, and the single indirect blocks finally point to the data blocks.\
Logical block addresses provide an abstraction for the software to interact with storage devices, while physical block addresses represent the actual hardware locations. (logical address block #2, actual physical address on disk #2885).\
Definition for myself: ooffset refering to the exact position inside a block.

2. **Storage & Allocation:**
- The allocation methods defines how the files are stored in the diskk block. Block Allocation Strategies:
    - contiguous - each file is wrriten on contiguous blocks on disk. simple metadata: "base & limit" - starting location and size of file. Pros: easy to implement, low storage overhead, Fast sequential access because of contiguous blocks. Cons: suffers from external and internal fragmantations while creating and removing files over time. Difficult to grow file because of contiguous requirement. Pros: very simple algorithm with minimal number of seeks.
    - linked - All data blocks are part of a linked list. Reserve some metadata bytes at the beginning of the data block for next pointer. (for example bolck of 512 bytes. 4 bytes of metadata and 508 bytes of actual data). In the file allocation table you have content of filename, start block and end block. Pros: No external fragmentation since blocks can be linked from anywhere, files can be easiliy grown without limit. Cons: Large storage overhead (one pointer per block). Potentially slow sequential access: lots of seeking since blocks need not be contiguous. Difficult to compute random access.
    - indexed - In the file allocation table there is the filename and its index block. In the index block there is an array of pointers (index) to data blocks. File size is limited by number of pointers [array_length]. Allocate blocks on demand (pointers are marked as invalid (-1) until they are allocated). Pros: no external fragmentation, files can be easily grown until index block limits. Fast random access. Cons: Large storage overhead for index. Used for very small files while the indexed allocation would keep one wntire block (the index block) for the pointers which is inefficient comparing to linked allocation.\ When it comes to inodes a single index block won't be enough and thats why there is the inode structure as I described before.
    - extent-based - Multiple contiguous regions per file (like segmentation). Metadata is an array of extents, where each extend has a start and size. Easier to grow files compared to contiguous allocation, but still suffers from external fragmentation.
- fragmentations:
    - Internal fragmantation - Internal fragmentation occurs when allocated memory contains unused space within a block. It happens when the size of the allocated memory block is larger than the actual memory required by a process. For example, if a system allocates a 64 KB memory block to a process that requires only 40 KB, the remaining 24 KB remains unused, resulting in internal fragmentation.
    - External fragmentation - External fragmentation occurs when free memory or storage space is divided into many small, non-contiguous blocks. It is caused by frequent allocation and deallocation of processes or files over time. As a result, files or processes must be stored in multiple smaller blocks, increasing access time.
- Performance impacting by file size & access patterns
    - sequential I/O vs random I/O - Sequential I/O involves reading or writing data in contiguous blocks. Great for large chunks of data need to be processed in order (videos streaming). Much faster than random reads. Random I/O, on the other hand, involves accessing data from arbitrary locations. Its slower but unavoidable (OLTP, file system metadata updates). Increase disk activity, system lag or even a sound while the HDDs are seeking. SSDs hadle it much better.
    - small vs large files - smaller file are familiar with randomly access with inode lookup, lots of seeks, overhead, slower, causes internal fragmantation. large files are familiar with sequential access, high throughput and fewer seeks.

3. **Directories, Indexing & Permissions:**  
- Directory indexing methods - 
    - linear lists - list of file names and pointers to their data blocks. Very straight forward. Linear searching, simple but long O(n).
    - hash tables - A hash table is a data structure that stores data in key–value pairs, making lookups, insertions, and deletions extremely fast — typically in ~ O(1) time on average. It uses a hash function to convert a key into an index in an internal array, where the corresponding value is stored. May cause collision. (EXT4)
    - B‑trees - self-balancing tree. Each node contains key of the file name and value of the inode. They automatically adjust themselves to maintain balace as data is inserted or deleted. All leaf nodes are in the same level, ensuring consistent access times. Order m: max m children per node. Each node has between m/2 and m children.  Contains between m/2-1 and m-1 keys. (NTFS, EXT4) O(log n).
- Why efficient lookup matters - Lookup refers to the process of searching for specific information or data within a particular system or database. It improves performance, minimizes latency, reduces I/O operations which are very expenssive and seeking operations, preventing I/O or metadata searching the file location bottlenecks.
- how access control integrates with directory lookup -  When a user requests to access data or a resource object, the operating system reads the ACL for the user’s entry. It determines whether they have access rights and the authority to perform the requested operation in the logical file system layer, the metadata layer, the inode stores the data of the access controll and unix mode bits permissions.

4. **Consistency, Journaling & Caching:** 
- Why do file systems employ journaling or copy‑on‑write logs?\
sophisticated solution to the problem of file system inconsistency in operating systems.
    - journaling - any changes made to the filesystem are written sequentially to a journal, also called a transaction. Once a transaction is written to a journal, it is written to an appropriate location on a disk. In the case of a system crash, the filesystem replays the journal to see whether any transaction is incomplete. When the transaction has been written to its on-disk location, it is removed from the Journal. Its making the file system more reliable and preserving its structure in system crashes and hardware failures. Journaling improves performance when it is enabled by having fewer seeks to the physical disks as data is only when a journal is committed or when the journal fills up. For example, in intense meta-data operations like recursive operations on the directory and its content, journaling improves performance by reducing frequent trips to disks and performing multiple updates as a single unit of work.\
    Copy-on-write (CoW) - When file is created it has two pointers to its inode but only when it modifies the file is duplicated for modification (efficient for snapshots) and the original file is still access to the rest of the processes. After it finishes the modification it updates the inode to point the new block. Page sharing is a fundamental aspect of CoW. When multiple processes start, instead of each process getting its own copy of the data, they all initially point to the same physical memory pages. These pages are marked as read-only. If a process tries to modify a page, a “page fault” occurs. This fault triggers the CoW mechanism, which then creates a private copy of the page for the process that wants to write to it. All other processes continue to use the original, shared page. This approach maximizes memory utilization and reduces the amount of physical memory required. (btrfs, zfs).
- What problems do these techniques address?\
CoW problems -\
Write Performance Overhead - The initial write to shared data incurs additional operations, such as allocating new memory and updating metadata, which can introduce latency.\
Data Fragmentation - Since modifications are written to new locations, data can become fragmented over time, potentially impacting read/write performance.
- how do caching and write buffering interact with crash recovery?
cache consists of in-memory buffers that hold copies of disk blocks. The system keeps a directory that tracks which items are currently in the cache. When a buffer needs to be replaced, it may be flushed to make space. Each buffer has a dirty bit (flag which notify that the data still not saved to disk) that indicates whether it has been modified. Dirty buffers must be written to disk before they are replaced. A pin or unpin bit determines whether a page in the buffer is free to be written back to disk.
- how do caching and write buffering interact with power‑failure scenarios? In caching data may exists only in the memory so it will be lost. In write buffering there might be a scenerio when the power is off before the data flashed and then the data will be lost and the disk will remain in the old state or may lead to corrupion if it was in the middle of writing to disk operation.

5. **Performance Trade‑offs & Distributed Extensions:**
- trade‑offs between throughput, latency, and reliability in file systems - Increasing throughput by batching or journaling can raise latency due to wait time. In distributed microservices, adding more services (parallelism) improves throughput but can increase inter-service latency due to networking overhead. Reliability can improved with more methods of replication, caching, journaling, CoW while increasing latency. Journaling improves throughput by writing the full operation at a time.
- replication, failover, and namespace servers extend these ideas in distributed systems\
replication - improves throughput (parallelism)\
failover - DFS Failover is the process of automatically switching data access to a backup location during a disaster. High availability and reliability.\
namespace servers - A namespace server hosts a namespace. The namespace server can be a member server or a domain controller. Higher latency by having the all relevant data in one namespace.


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

