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

1. מה ההבדל בין מערכת הפעלה למערכת קבצים?\
Operation system is a software (kernel) that manages and handles hardware and resources of a computing device. In contrast to file system which responsible of how the data is stored (hierarchical directories under root), organized and manage data on storage devices such as hard drives, SSDs.

2. מה ההבדל בין User Space ל-Kernel Space?\
userspace is the environment where user applications run and cannot directly access the system's hardware resources. They must make a syscalls (interfaces that allow userspace to interact with the kernel) to use the kernel space and request access to these resources. Kernel space is where the kernel operates with unrestricted access to the system's hardware resources for performing  its essential tasks such as scheduling processes, managing resources and handling interrupts.

3. מהו תהליך mount בלינוקס?\
The process of attaching a filesystem (a storage device such as USB or disk) to a specified directory in the file system hierarchy.
To mount a file:
- Setup the filesystem device
- Run the mount command: mount [-t <type>] [-o <options>] <device> <mount_point>
- run df -h to verify

4. אילו סוגי מערכות קבצים נפוצות קיימות בלינוקס?\
ext4 - the default file system for many linux distributions.\
Btrfs (B-Tree file system) - modern, advanced designed filesystem, with features of snapshoting, data deduplication, RAID.\
XFS - high performance, journaling file system that excels in handling large files and massive storage volumes.

5. מה זה fstab?
File system table. /etc/fstab is a static file system information. When I mount a disk by the mount command, and then reboot the server, the mount will be gone and I'll have to do it again in order to access the disk. To prevent from mounting over and over again I want to make a persistent mounted disk by adding the disk details as a row to the fstab file.

6. אילו סוגי mount קיימים?
mount types:
- local disk - a disk which was added to the machine and we want to use it.
- NFS - a network file sytem that allows remote hosts to mount file systems over the network nd interact with those file systems as though they are mounted locally.
- virtual file system - like tmpfs which stores data in the system's virtual memory as temporary storae of all files. You can configure it in the fstab but still everything is temporary wrriten on the ram and not on the disk for high performance.

7. באיזו פקודה בודקים ניצולת דיסק?\
df -h

8. מה זה הרשאות מסוג acl?\
ACLs (acsses control lists) provide an extended permission mechanism that allows you to set specific permissions for individual users or groups beyond standard rwx permissions.
- Allow permission control for specific users/groups without changing group membership. (setfacl -m "u:user:permissions" /path/to/file)
- ACLs on directories inherit specified permissions automatically
- You can identify that a file has ACL entry by the "+" sign in ls -l output
- It doesnt overrides the unix permissions, however it works alongside it.

9. איך בודקים פורטים פתוחים?\
Checking a specific connection to server and port:\
telnet <hostname | ip > <port>\
Checking open ports:
- netstat -lntu (linux networking subsystem command)
- ss -lntu (socket tool command)
- sudo lsof -i -P -n | grep LISTEN

10. מה זה RAID?\
RAID is a technique that combines multiple hard drives or SSDs into a single system to improve performance, data safety or both. If one drive fails, data can still be recovered from the others.
I'll explain the most popular levels:
- RAID 0 - striping. splitting data into smaller "blocks" and spreading them across multiple disks. Enables parallel read/write operations but provides no redundancy or fault tolerance.
- RAID 1 - mirroring. Creating an identical copy of each data block on seperate disks.
- RAID 10 - first mirrors the data (RAID-1) and then stripes across mirrored pairs (RAID-0).
- RAID 5 - block level stripping with distributed parity (a calculated value is stored to allow data recovery in case of failure)
- RAID 6 - block level stripping with distributed two parity bits to recover from failure of up to two disks simultaneously but imapcts write performances.

11. איך בודקים לוגים?\
/var/log

12. איך מאבחנים בעיית דיסק מלא?\
df -h (disk free) to see which of my disk is full.
du -h (disk usage) <path of the problematic disk> to see which directories are causing the problem.

13. איך מאבחנים עומס על המערכת?\
ps -ef / top / htop

14. מה זה cgroups?\
Control groups. Enables the limitation of system resources like CPU, memory, I/O, network bandwidth.
Example flow of memory cgroups usage, creating a memory cgroup (cgcreate) -> restricting a memory by defining its limiter (cgset) -> executing process with the resource limit (cgexec, can also be in a namespace)

15. מה זה namespaces?\
Namespaces create isolated environments for processes. They provide a process with its own isolated view of the system, such as its own fs, network, hostname. (uses unshare command)

16. מה זה sssd?\
System Security Services Deamon is a service that enables authentication mechanisms. With sssd I have the ability to connect with remote identity and authentications providers for example LDAP. I can login to the server as a user according to my LDAP credentials. 
