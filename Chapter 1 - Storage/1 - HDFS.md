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

### ⏳ Timeline
Estimated Duration: 3 Days
- Day 1-3: Learn the concepts of HDFS; spent time on what is it? on fault tolernce, on failover process and on how reads and writes are being done?
    - Have a Q&A session at the third day and in between sessions each day

## Core Concepts

Consider the following five questions to cover the major HDFS topics:

1. **Architecture & Roles:**  Describe HDFS’s overall architecture, including NameNode(s), DataNodes, blocks, and how the namespace and metadata are managed. Don’t forget the role of ZooKeeper in coordinating HA and keeping track of leases.
2. **Storage & Fault Tolerance:**  Explain how HDFS divides files into blocks, uses replication (default factor three), and how it detects and recovers from node failures.
3. **Topology Awareness & Performance:**  What is rack awareness and why does HDFS replicate across racks? Discuss how block placement, snapshots, and checksums contribute to performance and data integrity.
4. **High Availability :**  Outline HDFS High Availability (Active/Standby NameNode, JournalNodes). How do these features improve scalability and uptime?
5. **Protocol & Operations:**  Describe how clients read and write data to HDFS via RPC, how they locate NameNodes and DataNodes, how DataNodes send block reports, and why these mechanisms matter for everyday operations. Cover the runtime behaviour of leases and pipeline formation.

## Core Concepts - Answers :elephant::elephant::elephant:

1. **Architecture & Roles:**
HDFS stands for Hadoop Distributed Filesystem.\
HDFS architecture works in a master-slave pattern.
- Name Node (master) - Master server that manages file system namespace and regulate access to files by clients. The name node is responsible for all client operations in the cluster. It does not store block locations persistantly, because this information is reconstructed from datanodes when the system starts.\
Namenode keeping the entire metadata in the memory, while Fsimage and editlogs in the disk for rebuilding RAM state.
- Data Nodes (slaves) - serves read or write requests, it also creates, deletes, and replicates blocks based on the instructions from the name node. They report back to the namenode periodically with lists of blocks that they are storing.\
Datanodes stores the blocks of the actual data.
- Metadata management - The metadata is managed entirely by the namenode to optimize performance and scalability. It allows clients to quickly locate and access data blocks across the cluster. In context of HDFS, metadata would be file and directory names, block mapping, file size, block size, replication factor, ownweship and permissions, modification timestamps, quotas. The metadata can be stored in 3 storage components:
    1. fsimage - a snapshot of the entire file system metadata, stored on disk.
    2. edit log - a transaction log of all changes made since the last fsimage checkpoint
    3. In-memory storage - The NameNode loads the combined fsimage+edits into RAM for fast access.
- namespace - The namnode is also responsible for the HDFS namespace in the cluster. The namespace is set at the file level, meaning all files are hierarchical and follow a tree structure. Namenode keeps a reference to every file and block in the filesystem in memory, which means that on very large clusters with many files, memory becomes the limiting factor for scaling. This was a new change in HDFS 2.x of HDFS federation. It allows the clusters to add namenodes, each of which manages a portion of the filesystem namespace. Under federation, each namenode manages a namespace volume, which is made up of the metadata for the namespace, and metadata of it own block pool (set of block that belongs to a single namespace). Namespace volumes are independent of each other, which means namenodes do not communicate with one another and does not impact when one fails.
- Leases - Before a client can write an HDFS file, it must obtain a lease, which is essentially a lock. This ensures the single-writer semantics. The lease must be renewed within a predefined period of time if the client wishes to keep writing. If a lease is not explicitly renewed or the client holding it dies, then it will expire. When this happens, HDFS will close the file and release the lease on behalf of the client so that other clients can write to the file. This process is called lease recovery.

2. **Storage & Fault Tolerance:**
- how HDFS divides files into blocks - A disk  has a block size, which is the minimum amount of data that it can read or write. HDFS, too, has a concept of a block, but it much larger - 128MB by default (normally a disk block is 512 bytes). A file that is smaller than a single block does not occupy a full block's, its uses 1MB of disk space. HDFS blocks are large compared to disk blocks, because it minimized the cost of seeks.
- HDFS Replication - HDFS is designed to reliably store very large files across machines in a large cluster. It stores each file as a sequence of blocks. All blocks in the same size. The blocks of a file are replicated for fault tolerance. The block size and replication factor are configurable per file. An application can specify the number of replicas of a file. The replication factor can be specified at file creation time and can be changed later. The NameNode makes all decisions regarding replication of blocks. It periodically receives a Heartbeat and a Blockreport from each of the DataNodes in the cluster. A Blockreport contains a list of all blocks on a DataNode. 
- Safemode - On startup, the NameNode enters a special state called Safemode. Replication of data blocks does not occur when the NameNode is in the Safemode state. The NameNode receives Heartbeat and Blockreport messages from the DataNodes. Each block has a specified minimum number of replicas. A block is considered safely replicated when the minimum number of replicas of that data block has checked in with the NameNode. After a configurable percentage of safely replicated data blocks checks in with the NameNode (plus an additional 30 seconds), the NameNode exits the Safemode state. The NameNode then replicates the blocks that still have fewer then the specified number to other DataNodes. The default factor of replication is 3 I explain it in question 3.
- how it detects and recovers from node failures - 
Each DataNode sends a Heartbeat message to the NameNode periodically. A network partition can cause a subset of DataNodes to lose connectivity with the NameNode. The NameNode detects this condition by the absence of a Heartbeat message, marks them as dead. This cause the replication factor of some blocks to fall below their specified value. The necessity for re-replication may arise due to many reasons: a DataNode may become unavailable, a replica may become corrupted, a hard disk on a DataNode may fail, or the replication factor of a file may be increased.

3. **Topology Awareness & Performance:** 
- What is rack awareness and why does HDFS replicate across racks? HDFS is used in clustered environment where we have clusters, each cluster will have multiple racks, each rack will have multiple datanodes.
rack - group of datanodes (around 30-40). hdfs uses feature called rack awareness to improve speed and efficiency. It means the NameNode knows where each DataNode is located (which rack) and uses this to decide where to store data and its copies. There are Rack  Awareness policies to decide where these replicas go. Rack Awareness Rules Followed Here:
    - No more than 1 replica is placed on the same DataNode.
    - No more than 2 replicas of a block are on the same rack.
    - Replicas are distributed across multiple racks for fault tolerance.

So to make HDFS fault tolerant in your cluster you need to consider following failures-
    - DataNode Failure
    - rack failure
So you need to recover from both situations:
    - if one DataNode fails, you can get the same data from another DataNode.
    - If the entire Rack fails, you can get the same data from another Rack

So thats why we need rack awarness and it's policies and a replication factor of at least 3, so that not to replicas goes to the same datanode and at least 1 replica goes to different rack to fullfil the fault-tolerance.
- how do block placement, snapshots, and checksums contribute to performance and data integrity?
    - checksums - It is possible that a block of data fetched from a DataNode arrives corrupted. This corruption can occur because of faults in a storage device, network faults, or buggy software. The HDFS client software implements checksum checking on the contents of HDFS files. When a client creates an HDFS file, it computes a checksum of each block of the file and stores these checksums in a separate hidden file in the same HDFS namespace. When a client retrieves file contents it verifies that the data it received from each DataNode matches the checksum stored in the associated checksum file. If not, then the client can opt to retrieve that block from another DataNode that has a replica of that block. 
    - snapshots - Snapshots support storing a copy of data at a particular instant of time. One usage of the snapshot feature may be to roll back a corrupted HDFS instance to a previously known good point in time. 
    - block/replica placement - first replica on the same node of the client, if the client is outside the cluster so randomly. Second replica is off-rack (a different rack), chosen randomly. Third replica is placed on the same rack as the second, but on a different node chosen randomly.

4. **High Availability :**
Without the namenode, the filesystem cannot be used, all the files on the filesystem would be lost since there would be no way knowing how to reconstruct the files from the blocks on the datanodes. To solve this there are two mechanisms: Backup up files that make up the persistent state of the filesystem metadata. Can be written to local disk as well as remote NFS mount.
Another way is a secondery namenode which also called the standby node. The standby node reads the changes made to edit logs and applies it to its own namespace in a consistent manner. In event of a failover the standby node will ensure that it has read all the edits before promoting itself to the active state. This is a manual process which has to be performed by admin unless you have a zookeeper which manages failovers automatically with failover controllers. The zookeeper periodically managing health checks to the namenode and when the master will marked as unhealthy a new name node will be elected.
To manae HA there are few changes that needs to be configure:
    - The namenodes must use highly avalible shared storage to share edit logs.
    - Datanodes must send block reports to both namenodes because the block mappings are stored in a namenode’s memory, and not on disk.
    - Clients must be configured to handle namenode failover, using a mechanism that is transparent to users.
    - The secondary namenode’s role is subsumed by the standby, which takes periodic checkpoints of the active namenode’s namespace.

The first point of HA shared storage is recommanded to be solved with QJM (Quorum journal manager). It runs a group of journal nodes and each edit must be written to a majority of the journal nodes. Its does not use zookeeper. The edit logs are written to the local namenode and to the journalnode, but an operation will be committed only with the quorum of the journal nodes.

5. **Protocol & Operations:**
- how clients read and write data to HDFS via RPC?\
RPC - Remote Procedure Call, is a way for a program to run a function on another computer in a network as if it were local. The client sends the request (with arguments) to the server, the server executes the function, and the result is sent back.\
    - Read to HDFS - 
        1. open - The client requests from DFS to open() a file.
        2. get block locations - The DFS calls the namenode using RPC to get block locations (to each block - the addresses of the datanodes that have a copy of that block orders by proximity to the client)
        3. read to stream - client calls read() on the FSDataInputStream.
        4. read to first datanode - Data is streamed from the datanode back to the client which calls read() repeatedly on the stream.
        5. read next datanodes - When the end of the block is reached, it finds the best datanode for the next block.
        6. close() the stream from FSDataInputStream.
    - Write to HDFS -
        1. create - on DFS.
        2. create to NameNode - DFS makes an RPC call to the namnode for create. NameNode doinf checks that the file isnt already exist and right permissions. If passes the namenode make a record of the new file.
        3. write to FSOutputStream - The client requests to write().
        4. write packets - Data is split into packets and streamed through a pipeline of DataNodes, where each node stores the data and passes it to the next for replication.
        5. ack packet - A packet is removed from the ack queue only when it has been acknowledged by all the datanodes in the pipeline.
        6. close - the client calls close()
        7. complete - after finished all acks to  signal complete and after that the namenode return succecfully.
- how they locate NameNodes and DataNodes?
The client locates Namenodes via api of HDFS creating a DFS object, needs to go through authentication of kerberos. Then the namenodes return the relevant block for the client and it does it operations with an input\output streamer. Because of the kereberos authentication it cannot connect the datanodes directly.
- how DataNodes send block reports?
The DataNodes send the block reports to the NameNodes just like they send their heartbeats. The block reports have information about list of blocks, block metadta and block health. Useful to track block locations, detect missing replicas, etc.

### 🔄 Alternatives
Assignment: You are required to research and write a comparative analysis between HDFS and an industry alternative.
- Deliverable: A written summary (minimum 1 or 2 sentences).
- Focus: Compare performance, architecture, and specific "pain points" this tool solves compared to legacy systems or competitors.
- Goal: You must be able to justify why the department uses this tool for our specific environment.

### 🎯 User Story & Scenario
Assignment: Based on your research and understanding of the department's pipeline, define a concrete Use Case for this technology.
- Deliverable: A written summary example/story (two paragraphs approx.).
- Requirement: Describe a real-world scenario (e.g., a specific client requirement) where this technology is the optimal solution.
- Data Flow: Map out the data flow and explain how this tool integrates with other components in the Data Pipeline.


## Wrapping Up :trophy:
Review your answers with your mentor and discuss any unclear points. Relate these concepts back to real-world usage scenarios you might encounter.

## Action Items
- Note topics you want to investigate further.
- Prepare questions for the mentor Q&A session.
- Continue the Day 01 challenge by linking these HDFS concepts to other chapters.

## Recommended Resources
- [Official HDFS User Guide](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsUserGuide.html)
- [Hadoop: The Definitive Guide (O'Reilly)](https://piazza-resources.s3.amazonaws.com/ist3pwd6k8p5t/iu5gqbsh8re6mj/OReilly.Hadoop.The.Definitive.Guide.4th.Edition.2015.pdf)

## HDFS Q&A Answers
1. Describe the difference between file and directory? How the filesystem knows it directories?
A directory is technically just a file containing file names, their inode numbers, and attributes. for example a client wants to read a file in the path /directory/file:
    - Scan the directory / looking for an item named "directory". Get the associated inode number.
    -  Scan the directory /directory looking for an item named "file" and get the associated inode number.
    - Read the inode and get the file's metadata, permission bits, data location, etc.
2. Commodity Hardware - sometimes known as off-the-shelf hardware, is a computer device or IT component that is relatively inexpensive, widely available and basically interchangeable with other hardware of its type.
3. why we need HDFS? (instead of s3). Performance, data is stored and processed on the same machines, access and processing speed are faster.
4. HDFS federation - multipule namespaces. The prior HDFS architecture allows only a single namespace for the entire cluster. In that configuration, a single Namenode manages the namespace. HDFS Federation addresses this limitation by adding support for multiple Namenodes/namespaces to HDFS. Block pool - is a set of blocks that belong to a single namespace. Datanodes store blocks for all the block pools in the cluster. A Namespace and its block pool together are called Namespace Volume. Key-Benefits: scalability and isolation. Generic storage service - block pool abstraction allows applications to built directly on the block storage layer without the need to use a file system interface.
5. What is a block? How can I see block of HDFS?
A block in hdfs is a file, I can go to the path of the blocks.
6. How much metadata memory is allocated per file?
As a rule of thumb, each object occupies approximately 150 bytes.
7. What are the differences between 1 file of 1024MB to 8 files of 128MB and 1024 files of 1MB?
the equation is: metadata of a file is = 150 bytes * (1 file inode + (number of blocks * replication factor))\
1 scenrio: 150 *(1 + (2 * 3)) =  1050 bytes\
2 scenrio: 150*(8 + (4*3)) = 3000 bytes\
3 scenrio: 150 * (1024 + (1024*3)) = 614400 bytes\
Great Article, writing it for me: https://www.cloudera.com/blog/technical/small-files-big-foils-addressing-the-associated-metadata-and-application-challenges.html
8. Rack awareness default is to split 3 replicas in 3 different servers and thats because we have only 1 rack. How to configure rack awarness? According to Shabi we only have one rack, so the rack awareness aims to replicates the files in three different datanodes. To enable rack awareness in your Hadoop cluster, you can map hosts to racks and run a user-defined script to determine the mapping, enabling the data replicas to be placed intelligently. If a script is not specified, all hosts are mapped to a single network location, called /default-rack. 
9. What happens if datanode fail in a middle of writing? 
    - The write is interrupted. 
    - The client is notified of the failure. 
    - HDFS automatically excludes the failed DataNode. - The NameNode reconstructs a new pipline with other healthy datanodes.
    - The client retries the block write from where it left off.
10. Quota in HDFS - quota in hdfs can be name quotas, space quotas, storage type quotas. 
    - name quota - hard limit on the number of file and directory names in the tree rooted at that directory. File and directory creations fail if the quota would be exceeded. 
    - space quota - The space quota is a hard limit on the number of bytes used by files in the tree rooted at that directory.
    - The storage type quota is a hard limit on the usage of specific storage type (SSD, DISK, ARCHIVE) by files in the tree rooted at the directory. 
11. - fsimage - a file that represents a point-in-time snapshot of the filesystem’s metadata.
    - edit-logs - the NameNode maintains a log of all the changes made to the file system, called the edit log. The edit log can become quite large over time, which can slow down the performance of the NameNode.
    - audit-logs - HDFS has two different audit logs, hdfs-audit.log for user activity and SecurityAuth-hdfs.audit for service activity. Both of these logs are implemented with Apache Log4j, a common and well known mechanism for logging in Java.
12. How they are implemented in the read write operations?
- audit-logs - in write and read
- edit-logs - on writing when the file system has changed.
- fsimage - periodically.
13. Checkpoints -  Checkpointing is a process that takes an fsimage and edit log and compacts them into a new fsimage. This way, instead of replaying a potentially unbounded edit log, the NameNode can load the final in-memory state directly from the fsimage. This is a far more efficient operation and reduces NameNode startup time. Checkpointing allows the NameNode to merge the edit log with the file system, which reduces the size of the log and improves the performance of the NameNode.
14. How HDFS reads in a pararallize way?
It reads from multipule blocks from different nodes in the same time. The FSDataInputStream from the client framework level is resposible of it. The data is spread in different blocks so it can be read with multipule threads (for example using Spark for processing). 
15. Fencing mechanism in journal nodes - The journal nodes works in a way that only on node can write edit log in specific time.
16. What additional information is sent in the heartbeat? The heartbeat also carries information lke total storage capacity, the usage of storage, and the number of data transfers currently in progres.
17. Which component is doing the checkpoints? and when? the checkpoint is performed by standby nameNode or SeconderyNameNode (legacy). It happends by triggers. fs.checkpoint.period controls how often this reconciliation will be triggered. fs.checkpoint.size is a size threshold, which, if reached by edits, will trigger an immediate checkpoint regardless of time elapsed since the last checkpoint. 

## Studing for Q&A 2
1. Startup Process of NameNode (safemode) - 
    - loaded its fsimage to memory
    - replayed edit log
    - received enough block reports from the datanodes and getting out of safemode.
2. Automatic failover - Adds two new components to the HDFS. ZooKeeper Quorum & ZKFailoverController.
    - Health monitoring - the ZKFC pings its local namenode periodically with healch-check command. If the node crashed, or otherwise entered an unhealthy state and marked as unhealthy.
    - Failover Detection - When the machine craches, the session with the zookeeper is expired, notifying hte other NameNode that a failover should be triggered.
    - Active NameNode Election - Having election the other namenode succeed by creating a zookeeper lock and become the next active.
Manually failover - in order to do manual failover we need to run this command hdfs haadmin -failover -forceactive namenode1(active) namenode1(standby).
In hadoop 1 the seconderyNameNode was only used for checkpoints. So the administrator would have to manually restart the NameNode. In hadoop 2 we need to run the command.
3. Fencing - A fencing method is a method by which one node can forcibly prevent another node from making continued progress. This might be implemented by killing a process on the other node or by denying the other node's access to shared storage.
Is a mechanism used to prevent or resolve split-brain scenarios, to ensure that only one namenode in the cluster remain active. Zookeeper provides a distributed locking mechanism that allows the active Hadoop NameNode to obtain a lock, while other NameNodes are fenced off in case of a network partition or failure.
4. nameservice - instead of checking for active namenode host and port combination, we should use nameservice as, nameservice will automatically transfer client requests to active namenode. Acts like a proxy among NameNodes which always transfers the HDFS requests to the active namenode. Needs to be configured in the hdfs-site.xml.
5. zookeeper responsibilities - 
- failover controller - leader election
- fencing - locking mechanism
- configuration managment - ZooKeeper maintains configuration information, ensuring all nodes in a distributed system have consistent settings.

