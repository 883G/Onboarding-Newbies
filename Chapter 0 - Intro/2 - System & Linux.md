# System, Linux & Security Fundamentals :computer:

## **Topics Covered**
- Linux directory hierarchy (`/`, `/etc`, `/var`, `/proc`, etc.)
- Process model and scheduling
- Kernel I/O path and page cache
- Authentication vs. authorization; Kerberos, LDAP, SSSD
- Basic shell usage and GNU utilities
- User/group management and service control (`systemd`)
  - *Other init systems*: initd, OpenRC, runit, etc. (historical/alternative)

> ⚠️ **Note:**
> This chapter is a roadmap, not a lesson.  You’ll enter the mock course we’ve prepared with your mentor’s help and work through it together.  Ask your mentor for guidance before diving into any of the material.

### ⏳ Timeline
Estimated Duration: 1 Day
- Day 1: Spent this day as your mentor instructs you;
    - Have a Q&A session right after

## Overview
These are the high‑level areas you should be familiar with when starting on our platform.  The actual content will be explored during the mock training session with your mentor; use the list above as a checklist.

> Note: while some environment uses `systemd` for service management, other init systems like **initd**, **OpenRC**, and **runit** exist and may be encountered in alternative distributions. Understanding the basic concept of an init system is more important than knowing the specific implementation.

## Wrapping Up :trophy:
Discuss the topics with your mentor and make sure you can describe each one at a basic level.  Don’t worry about memorizing commands—focus on understanding what the topics are and why they matter.

## Linux Questions & Answers

1. מה ההבדל בין מערכת הפעלה למערכת קבצים?
Operation system is a software (kernel) that manages and handles hardware and resources of a computing device. In contrast to file system which responsible of how the data is stored (hierarchical directories under root), organized and manage data on storage devices such as hard drives, SSDs.
2. מה ההבדל בין User Space ל-Kernel Space?
userspace is the environment where user applications run and cannot directly access the system's hardware resources. They must make a syscalls (interfaces that allow userspace to interact with the kernel) to use the kernel space and request access to these resources. Kernel space is where the kernel operates with unrestricted access to the system's hardware resources for performing  its essential tasks such as scheduling processes, managing resources and handling interrupts.
3. מהו תהליך mount בלינוקס?
The process of attaching a filesystem (a storage device such as USB or disk) to a specified directory in the file system hierarchy.
To mount a file:
- Setup the filesystem device
- Run the mount command: mount [-t <type>] [-o <options>] <device> <mount_point>
- run df -h to verify
4. אילו סוגי מערכות קבצים נפוצות קיימות בלינוקס?
ext4, XFS
5. מה זה fstab?
6. אילו סוגי mount קיימים?
7. באיזו פקודה בודקים ניצולת דיסק?
df -h
8. מה זה הרשאות מסוג acl?
9. איך בודקים פורטים פתוחים?
10. מה זה RAID?
11. איך בודקים לוגים?
/var/log
12. איך מאבחנים בעיית דיסק מלא?
13. איך מאבחנים עומס על המערכת?
ps -ef / top / htop
14. מה זה cgroups?
Control groups. Enables the limitation of system resources like CPU, memory, I/O, network bandwidth.
Example flow of memory cgroups usage, creating a memory cgroup (cgcreate) -> restricting a memory by defining its limiter (cgset) -> executing process with the resource limit (cgexec, can also be in a namespace)
15. מה זה namespaces?
Namespaces create isolated environments for processes. They provide a process with its own isolated view of the system, such as its own fs, network, hostname. (uses unshare command)
16. מה זה sssd?
System Security Services Deamon is a service that enables authentication mechanisms. With sssd I have the ability to connect with remote identity and authentications providers for example LDAP. I can login to the server as a user according to my LDAP credentials. 
