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

2. **Consistency & Watches:**
- Zookeeper guarantee sequential consistency - sequential consistency means that updates from a client will be applied in the order that they were sent. ZooKeeper uses a special atomic messaging protocol called ZAB. ZAB protocol is atomic, so the protocol guarantees that updates either succeed or fail. In Zookeeper every write goes through the leader and leader generates a transaction id (called zxid) and assigns it to this write request. The zxid represents the order in which the writes are applied on all replicas. A write is considered successful if the leader receives the ack from the majority.
- Watches - simple mechanism for the clients (registered by the client when there is a session) to get notifications about the changes in a ZooKeeper ensemble. Any client can set a watch on data and will be notified once it detects the changes (not the information of the change only there is a change). Examples of changes can be configuration changes, leader changes, new znode child, etc.
- one-time triggers - the watches of the zookeeper are one-time triggers. If I get a watch event and I want to get notified of future changes, I must set another watch. Changes to that znode trigger the watch and then clear the watch. For example, if a client does a getData("/znode1", true) and later the data for /znode1 is changed or deleted, the client will get a watch event for /znode1. If /znode1 changes again, no watch event will be sent unless the client has done another read that sets a new watch. Zookeeper creates one-time trigger watches and not permanent watches because its more simple for distributed systems and prevents many problems and unreliability if the client has disconnected for examle.
- Prevent cache invalidations - Clients pull information from the zookeeper and cache it locally. Without the mechanism of watches they can keep using a stale data or polling from the zookeeper constantly over and over again which is inefficient. The solution is using watches and after the client is notified by a change, pull the data and update the cache.

3. **Sessions & Failure Handling:**
- Zookeeper session - The session is then created between a client and server by assigning a unique id to the client. The lifetime of an ephemeral znode is as long as the session is active, when the session has closed or expired the ephemeral znode automatically will be deleted. (Thats why ephemeral znodes cant have a child znodes)
- Heartbeats - There is a timeout period for a session which is specified by the application. The timeout depends on the nature of the application and cluster environment. The session gets expired automatically when the connection remains idle for more than the specified timeout period.
The session remains active by sending a heartbeat signal to the ZooKeeper service. 
- In case a session expires, the authentication fails, or a connection gracefully closes.

4. **Common Patterns:**
- Leader election - All servers in an ensemble participate in the leader election algorithm with the LOOKING state.  The idea is to have a znode, say "/election", such that each znode creates a child znode "/election/guid-n_" with both flags SEQUENCE|EPHEMERAL. With the sequence flag, ZooKeeper automatically appends a sequence number that is greater than anyone previously appended to a child of "/election". The process that created the znode with the smallest appended sequence number is the leader.
- Distributed locks - distributed systems in typical scenarios needs to ensure that only one node of the cluster is allowed to carry out an operation in a time. for example, write to a shared database or a file. In this case, a session is created and then clients create an ephemeral + sequential znode with increasing counter and when they are the smallest number in the counter (gets a notification by the watch) thay proceeding their operations.
- Configuration storage

5. **Operational Concerns:**
- deploy an ensemble - 
- handle scaling - 
- manage snapshots & transaction logs - 


### Kerberos – five guiding questions
1. **Protocol Flow:**  Walk through the Kerberos authentication flow from initial login (kinit) to obtaining service tickets.  Include AS, TGS, and ticket caches.
2. **Key Concepts:**  Define principals, realms, KDC components, tickets (TGT vs service ticket), and how encryption keys are derived and used.
3. **Security Properties:**  Why is Kerberos considered secure?  Discuss mutual authentication, replay protection, time sensitivity, and the role of the ticket lifetime.
4. **Administration & Tools:**  What are common Kerberos administration tasks?  Describe commands like `kadmin`, `kinit`, `klist`, `kdestroy`, and how to add principals or change passwords.
5. **Integration & Troubleshooting:**  How do services (Hadoop, HTTP, SSH) integrate with Kerberos?  What are typical issues (clock skew, wrong realm, keytab problems) and how do you diagnose them?

### Kerberos - Answers

1. **Protocol Flow:**\
KDC - key distribution server\
TGS - ticket granting server\
SS - service server\
AS - authentication server\
TGT - ticket granting ticket
    1. Client Authentication Request: The client sends an authentication request to the AS, encrypted with the user’s password hash.
    2. Ticket Granting Ticket (TGT): If the client is authenticated successfully, the AS issues a Ticket Granting Ticket (TGT) and a session key. The TGT is encrypted with the KDC’s secret key.
    3. TGT Request: The client sends the TGT to the TGS to request access to a specific service.
    4. Service Ticket: If the TGT is valid, the TGS issues a service ticket and a session key for the requested service. The service ticket is encrypted with the service’s secret key.
    5. Service Request: The client sends the service ticket to the application server along with an authenticator (encrypted with the session key) to prove its identity.
    6. Service Access: If the service ticket and authenticator are valid, the application server grants access to the requested service.
    A Kerberos ticket cache is a secure, local storage area on a client machine where a user’s Kerberos tickets and session keys are temporarily stored.

2. **Key Concepts:**
- principle - a unique identity. either a user or a service, an application.
- realms - A keberos realm is the domain, the group of systems which kerberos has the authority to authenticate a user to a service. You can have multiple realms and you can interconnect them. within a realm you have principles.
- KDC components - The heart of kerberos. There are two servers in the KDC. The authentication server (AS, confirms a known user is making an access request) and the ticket granting server (TGS, confirms that the user is making an access request to a known service)
- tickets (TGT vs service ticket) -\
TGT - Once the KDC verifies the user’s identity, it sends back a TGT, which is a ticket granting ticket. This ticket is encrypted with the KDC’s master key and contains a session key that can be used to request access to other services on the network.\
Session key - key that is used to encrypt all communications between the client and server. The session key is encrypted using the KDC’s master key and sent with the TGT to the client. The client then decrypts the session key using its own password, allowing it to use the key to encrypt messages sent to the server.
- reusable authentication - Kerberos authentication is durable and reusable. Each user will only have to be verified by the system once. Then throughout the lifetime of the ticket, the user can authenticate without the need to reenter personal information.

3. **Security Properties:**\
Multiple secret keys, third-party authorization, and cryptography make Kerberos a secure verification protocol. Passwords are not sent over the networks, and secret keys are encrypted, making it difficult for attackers to impersonate users or services. You also configure a ticket lifetime, after the end of it the ticket can no longer be used. replay attack prevention - the timestamp mechanism effectively prevents attackers from reusing captured authentication data. Even if an attacker intercepts an Authenticator, it becomes useless after the time window expires.

4. **Administration & Tools:**
 - `kinit` - kinit obtains and caches an initial ticket-granting ticket for principal.
 - `kadmin` - maintenance of Kerberos principals, password policies, and service key tables (keytabs). For example to add priciple of LDAP -> kadmin: addprinc ldap/<hostname> or adding user name bublick -> kadmin: ank -policy users bublick and give hime administrator permissions -> kadmin: ank -policy admin bublick/admin.
 - `klist` - klist lists the Kerberos principal and Kerberos tickets held in a credentials cache, or the keys held in a keytab file.
- `kdestroy` - The kdestroy utility destroys the user’s active Kerberos authorization tickets by overwriting and deleting the credentials cache that contains them. If the credentials cache is not specified, the default credentials cache is destroyed.

5. **Integration & Troubleshooting:**


### LDAP – five guiding questions
1. **Directory Structure:**  Explain how LDAP organizes information in a hierarchical tree (DN, RDN), common object classes, and attributes for users and services.
2. **Protocols & Operations:**  Describe basic LDAP operations – bind, search, modify, add, delete – and the difference between simple and SASL binds.
3. **Schema & Extensibility:**  What is an LDAP schema?  How do object classes, attribute types, and syntax rules define what data can be stored?  Mention extending schemas.
4. **Authentication & Authorization:**  How is LDAP used for authentication and authorization?  Cover binding with credentials, password policies, and group lookups.
5. **Deployment & Security:**  Outline how to install/configure an LDAP server (e.g., OpenLDAP), secure it with TLS, replicate data, and troubleshoot common errors (referral loops, access controls).

### LDAP – Answers

1. LDAP Structure - An LDAP directory has a hierarchical tree-like structure (DIT) and consists of one or more entries. The entries generally represent real world entities such as organizations, users and so on. For an enterprise, for example, the top or root of the tree could represent the organization itself.\ 
entry - a node in the tree
DN - the distinguished name, which contains a path through the directory information tree (DIT) for LDAP to navigate through (For example, cn=Susan, ou=users, o=Company).\
RDN - Relative Distinguished Name, each component in the path within the DN (For example, cn=Susan)
LDAP components -\
dc - domain access component, dns.\
o - organization name.\
ou - organizational unit (ou=users or ou=group).\
cn - common name (cn=developers, cn=some-name).\
attributes - key value rows which are schema defined that belongs to an entry.\
Object classes - are used to indicate what type of object is represented by an entry, and to specify the types of attributes that may be included in the entry.
- Abstract classes: are those that may specify a set of required and optional attribute types. Needs to be extended.
- Structural classes are those that specify the main type of object that an entry represents (e.g., a user, a group, a device, etc.). Structural classes may inherit from abstract or structural object classes, but not from auxiliary classes. 
- Auxiliary classes - may be used to provide information about additional characteristics for an entry. For example, the strongAuthenticationUser object class.\
examples of user attributes - cn, mail, uid.\
examples of service attributes - host, authorizedService, description.

2. **Protocols & Operations:**\
Basic Ldap operations - 
- bind - Authenticate a user and change the identity of the client connection. 
- search - Retrieve entries that match a given set of criteria.
- Create a new entry in the directory. 
- delete - Remove an entry from the directory.\
simple vs SASL bind - In simple authentication, the account to authenticate is identified by the DN of the entry for that account, and the proof identity comes in the form of a password. The password is transmitted without any form of obfuscation, so it is strongly recommended that simple authentication be used only over an encrypted connection. SASL authentication uses the Simple Authentication and Security Layer, SASL is an extensible framework that makes it possible to plug almost any kind of authentication into LDAP (for example, kerberos).

3. **Schema & Extensibility:**

    
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
