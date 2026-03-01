# System, Linux & Security Fundamentals :computer:

## **Goals**
- Understand Linux core concepts and the kernel I/O path.
- Explore authentication and authorization (Kerberos, LDAP) used in our environment.
- Learn about Apache ZooKeeper and its role in coordination.
- Gain familiarity with basic shell usage (`bash`) and system administration.

> ⚠️ **Note:** 
> This material will live in Git; you will be expected to track your notes here. If your mentors are running a mock course, ask them how to join it and how this repo fits into your workflow.

## Overview
This session covers foundational system topics that are critical for working with our data platform. You will review Linux concepts, security mechanisms, and coordination services used across the cluster.

**Emphasis is on understanding the "why" behind the tools rather than memorizing commands.**

### Core Concepts
Answer the following questions to guide your self-study:

1. **Linux Fundamentals:**  Describe the kernel/user space split, how processes are scheduled, the Linux filesystem hierarchy, and the I/O path from application to disk (system calls, page cache, block layer).
2. **Shell & Tools:**  What are common shell builtins and utilities you’ll use? How does the `bash` environment handle variables, job control, and simple scripting?
3. **Authentication & Authorization:**  Explain how Kerberos tickets work, how LDAP is used for user and group information, and why we prefer centralized directory services. Include an overview of how to obtain a ticket and verify a principal.
4. **ZooKeeper & Coordination:**  What is Apache ZooKeeper, and how do services like Hadoop, HBase, and others use it for configuration, leader election, and coordination? Describe its data model (znodes) and basic operations.
5. **Security Practices:**  Why should you avoid pasting GPT-generated answers into onboarding documents? What are some general security best practices when working on a shared cluster (e.g., never store plaintext credentials, lock screens, etc.)?

## Wrapping Up :trophy:
Review your answers with your mentor. Make sure you can explain each concept in your own words and relate them to the broader platform.

## Action Items
- Collect commands you find useful and add them to a personal cheat sheet in this repo.
- Practice obtaining a Kerberos ticket and exploring ZooKeeper with `zkCli.sh` (if you have access).
- Ask your mentor for recommended reading or tutorials on Linux administration and security.



