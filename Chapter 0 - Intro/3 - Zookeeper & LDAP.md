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

## Core Concepts

### Zookeeper – five guiding questions
1. **Architecture & Data Model:**  Describe a Zookeeper ensemble, the role of the leader and followers, the znode hierarchy, and how znodes store data and metadata.
2. **Consistency & Watches:**  How does Zookeeper guarantee sequential consistency?  Explain watches, one‑time triggers, and how clients use them for cache invalidation.
3. **Sessions & Failure Handling:**  What is a Zookeeper session, how are heartbeats maintained, and what happens when the session expires?  Discuss how ephemeral and sequential nodes relate to this.
4. **Common Patterns:**  Explain how leader election, distributed locks, and configuration storage are implemented on top of Zookeeper primitives.
5. **Operational Concerns:**  Outline how to deploy an ensemble, handle scaling, manage snapshots and transaction logs, and troubleshoot typical issues (e.g., split‑brain, latency).

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
