# Zookeeper, Kerberos & LDAP :lock:

## Overview
This session focuses on the components that provide coordination and authentication in distributed systems.  Zookeeper acts as the lightweight coordination service, while Kerberos and LDAP handle secure identities and directory information.  These technologies are commonly paired in Hadoop and other big‑data ecosystems.

**Study the key components, design decisions, and how they work together to enable secure, reliable clusters.**

## Goals
- Learn Zookeeper’s architecture and core features.
- Understand the Kerberos authentication flow and the purpose of LDAP directories.
- See how these systems integrate with each other and with Hadoop.
- Practice organizing a self‑study day and managing your time.
- Prepare to discuss your findings with your mentor.

:warning: **Note:**
- This is a self‑study session; independence and time management are critical.
- Focus on grasping the full picture of each concept – if you can’t explain it, you haven’t learned it.
- When in doubt, ask your mentor which topics deserve deeper attention.

### ⏳ Timeline
Estimated Duration: 1 Day
- Day 1: Spent no more than third a day on each of the following: LDAP, ZOOKEEPER,Kerberos, Hint read a bit about Active Directory As well;
    - Have a Q&A session right after

## Core Concepts

### Zookeeper – five guiding questions
1. **Architecture & Data Model:**  Describe a Zookeeper ensemble, the role of the leader and followers, the znode hierarchy, and how znodes store data and metadata.
2. **Consistency & Watches:**  How does Zookeeper guarantee sequential consistency?  Explain watches, one‑time triggers, and how clients use them for cache invalidation.
3. **Sessions & Failure Handling:**  What is a Zookeeper session, how are heartbeats maintained, and what happens when the session expires?  Discuss how ephemeral and sequential nodes relate to this.
4. **Common Patterns:**  Explain how leader election, distributed locks, and configuration storage are implemented on top of Zookeeper primitives.
5. **Operational Concerns:**  Outline how to deploy an ensemble, handle scaling, manage snapshots and transaction logs, and troubleshoot typical issues (e.g., split‑brain, latency).

### Zookeeper - Answers
1. **Architecture & Data Model:**\
Apache zookeeper is a distributed cootdination service for managing configuration, synchronization and leader election across distributed systems. Its an external tool that distributed systems can use to recover from partial failures in the cluster.
- Zookeeper ensamble - The group of servers (at least three) is called an ensemble. All servers in the ensemble keep a copy of the data. The data contains transaction logs and snapshots which are used for synchronization purposes and data watches.
- Leader role - A Leader is a server node that is elected at startup and performs automatic recovery if a node fails.
- Followers role - All the server nodes except the leader, are referred to as followers. The followers share their status with each other for ZooKeeper replication.
- Zookeeper data model - The Zookeeper stores the data in the memory but it follows a file system like hierarchichal namespace starting from the "/". In the namespace there are nodes called znodes which can store data or has a child znode (because its a tree, each level is a zookeeper node in the tree).
- Znode structure - znode has a stat structure contains data (optional) and meta data. Data - string. max 1Mb recommended to be much small. Metadata - included version number (how many time the data has changed),acl (access control list which limits who can read/write data), timestamps (ctime, creation time & mtime, last modified time).

2. **Consistency & Watches:**\
- Zookeeper guarantee sequential consistency - sequential consistency means that updates from a client will be applied in the order that they were sent. ZooKeeper uses a special atomic messaging protocol called ZAB. ZAB protocol is atomic, so the protocol guarantees that updates either succeed or fail. In Zookeeper every write goes through the leader and leader generates a transaction id (called zxid) and assigns it to this write request. The zxid represents the order in which the writes are applied on all replicas. A write is considered successful if the leader receives the ack from the majority.
- Watches - simple mechanism for the clients (registered by the client when there is a session) to get notifications about the changes in a ZooKeeper ensemble. Any client can set a watch on data and will be notified once it detects the changes (not the information of the change only there is a change). Examples of changes can be configuration changes, leader changes, new znode child, etc.
- one-time triggers - the watches of the zookeeper are one-time triggers. If I get a watch event and I want to get notified of future changes, I must set another watch. Changes to that znode trigger the watch and then clear the watch. For example, if a client does a getData("/znode1", true) and later the data for /znode1 is changed or deleted, the client will get a watch event for /znode1. If /znode1 changes again, no watch event will be sent unless the client has done another read that sets a new watch. Zookeeper creates one-time trigger watches and not permanent watches because its more simple for distributed systems and prevents many problems and unreliability if the client has disconnected for examle.
- Prevent cache invalidations - Clients pull information from the zookeeper and cache it locally. Without the mechanism of watches they can keep using a stale data or polling for the zookeeper constantly over and over again which is inefficient. The solution is using watches and after the client is notified by a change, pull the data and update the cache.


### Kerberos – five guiding questions
1. **Protocol Flow:**  Walk through the Kerberos authentication flow from initial login (kinit) to obtaining service tickets.  Include AS, TGS, and ticket caches.
2. **Key Concepts:**  Define principals, realms, KDC components, tickets (TGT vs service ticket), and how encryption keys are derived and used.
3. **Security Properties:**  Why is Kerberos considered secure?  Discuss mutual authentication, replay protection, time sensitivity, and the role of the ticket lifetime.
4. **Administration & Tools:**  What are common Kerberos administration tasks?  Describe commands like `kadmin`, `kinit`, `klist`, `kdestroy`, and how to add principals or change passwords.
5. **Integration & Troubleshooting:**  How do services (Hadoop, HTTP, SSH) integrate with Kerberos?  What are typical issues (clock skew, wrong realm, keytab problems) and how do you diagnose them?

### LDAP – five guiding questions
1. **Directory Structure:**  Explain how LDAP organizes information in a hierarchical tree (DN, RDN), common object classes, and attributes for users and services.
2. **Protocols & Operations:**  Describe basic LDAP operations – bind, search, modify, add, delete – and the difference between simple and SASL binds.
3. **Schema & Extensibility:**  What is an LDAP schema?  How do object classes, attribute types, and syntax rules define what data can be stored?  Mention extending schemas.
4. **Authentication & Authorization:**  How is LDAP used for authentication and authorization?  Cover binding with credentials, password policies, and group lookups.
5. **Deployment & Security:**  Outline how to install/configure an LDAP server (e.g., OpenLDAP), secure it with TLS, replicate data, and troubleshoot common errors (referral loops, access controls).

### 🔄 Alternatives
Assignment: You are required to research and write a comparative analysis between Zookeeper, Kerberos & LDAP and an industry alternative.
- Deliverable: A written summary (minimum 1 or 2 sentences).
- Focus: Compare performance, architecture, and specific "pain points" this tool solves compared to legacy systems or competitors.
- Goal: You must be able to justify why the department uses this tool for our specific environment.

### 🎯 User Story & Scenario
Assignment: Based on your research and understanding of the department's pipeline, define a concrete Use Case for this technology.
- Deliverable: A written summary example/story (two paragraphs approx.).
- Requirement: Describe a real-world scenario (e.g., a specific client requirement) where this technology is the optimal solution.
- Data Flow: Map out the data flow and explain how this tool integrates with other components in the Data Pipeline.

## Wrapping Up :trophy:
Review your answers with your mentor and discuss any unclear points.  Relate each concept back to actual deployments you might encounter.

## Action Items
- Note topics you want to investigate further.
- Prepare questions for the mentor Q&A session.
- Document any commands or configuration steps you used during research.

## Recommended Resources
- [Apache Zookeeper Documentation](https://zookeeper.apache.org/)
- [Kerberos: The Network Authentication Protocol](https://web.mit.edu/kerberos/)
- [LDAP: RFC 4511 Overview](https://datatracker.ietf.org/doc/html/rfc4511)
- *Hadoop Security* chapter in any modern Hadoop book for integration examples.
