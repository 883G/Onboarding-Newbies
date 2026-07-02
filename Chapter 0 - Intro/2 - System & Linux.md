# Linux & Infrastructure Foundations 💻💾

Linux is the foundation of modern infrastructure, servers, cloud platforms, containers, and distributed systems.

Understanding Linux fundamentals helps engineers troubleshoot systems, manage resources, automate operations, and understand how modern platforms work internally.

---

### ⏳ Timeline

Estimated Duration: 1 Day

Linux & Infrastructure Core Concepts:

* Linux Architecture & Kernel Basics
* File Systems & Inodes
* Processes, Daemons & Privileges
* System Initialization (systemd)
* cgroups & namespaces
* Root File System & Mounting
* Basic GNU/Linux Utilities
* Vim & Nano Basics

---

### 📚 Resources

* [Linux Journey](https://linuxjourney.com/?utm_source=chatgpt.com)
* [The Linux Documentation Project](https://tldp.org/?utm_source=chatgpt.com)
* [systemd Documentation](https://systemd.io/?utm_source=chatgpt.com)
* [GNU Core Utilities Manual](https://www.gnu.org/software/coreutils/manual/coreutils.html?utm_source=chatgpt.com)
* [Vim Documentation](https://www.vim.org/docs.php?utm_source=chatgpt.com)
* [Intro to OS mini book](https://fantastic-couscous-vjv74gqjj9w2wq74.github.dev/)

---

# Linux & Infrastructure Core Concepts

### ❓ Guide Questions

1. **What are the layers of an operating system, and how do they interact with each other?**

   Explain:
   * The hardware, kernel, system services, and user-space layers
   * How these layers work together to provide a complete operating system
   * What the kernel does and why it is the core of the OS
   * The difference between system services and applications
   * The role of kernel modules and device drivers

2. **Choose a Linux topic from this chapter that interests you most, research it deeply, and explain how an application request becomes a kernel action and translates back to an application response.**

   Possible topics to explore:
   * Filesystems and I/O operations
   * Process management and scheduling
   * Memory management and virtual memory
   * Networking and network stacks
   * Security and permission models
   * cgroups and resource isolation
   
   For your chosen topic, explain:
   * The layers involved from application to kernel and back
   * How system calls bridge user-space and kernel-space
   * The role of interrupts, context switches, and scheduling
   * Real examples using tools like `strace`, `ltrace`, or `perf` to trace the flow
   * Why this interaction pattern matters for system performance and reliability

3. **How do processes and daemons work in Linux, and how do threads fit into this model?**

   Explain:
   * Processes vs daemons
   * Process lifecycle and basic process attributes such as PID and PPID
   * Privileges, the root user, and why permissions matter
   * Threads and how they differ from processes
   * Signals such as `SIGTERM`, `SIGKILL`, and `SIGHUP`
   * How to inspect processes with `ps`, `top`, `htop`, and `pstree`
   * How services are started and managed with `systemd` and `systemctl`

4. **How does Linux isolate workloads and control resources?**

   Explain:
   * cgroups and namespaces
   * CPU, memory, and I/O isolation
   * Why containers rely on these mechanisms
   * Practical examples such as `systemd-run --scope`, `unshare`, and `nsenter`
   * Network namespaces and virtual interfaces
   * Resource monitoring and troubleshooting basics

5. **What are the different types of filesystems, and how do they differ? Then focus on Linux filesystems for a deeper understanding.**

   Explain filesystem types across operating systems:
   * Common filesystem types and their use cases
   * How different operating systems organize files and directories
   
   Then dive deep into Linux filesystems:
   * How Linux filesystems work in practice
   * Inodes, directory entries, and why metadata matters
   * Root filesystem (`/`), mount points, and `/etc/fstab`
   * Linux filesystem examples such as `ext4`, `xfs`, `btrfs`, `tmpfs`, and `vfat`
   * Permissions, ownership, and the Linux permission model (`rwx` for user/group/others)
   * Special permissions such as the sticky bit, setuid, and setgid
   * Basic commands such as `mount`, `df`, `stat`, `chmod`, and `chown`

6. **What are the essential Linux commands for everyday system management and basic navigation?**

   Explain and demonstrate basic usage of:
   * Navigation and file handling: `ls`, `cd`, `pwd`, `mkdir`, `cp`, `mv`, `rm`, `touch`, `cat`
   * Viewing and searching files: `head`, `tail`, `grep`, `sed`, `awk`, `sort`, `uniq`
   * System administration basics: `systemctl`, `journalctl`, `ps`, `top`, `df`, `du`
   * File transfer and remote access: `ssh`, `scp`, `rsync`, `curl`
   * Package management basics with `apt`, `yum`, or `dnf`
   * Basic shell concepts such as piping, redirection, environment variables, and simple scripting

---
> ⚠️ The lab should be done after answering the Guide Questions

### Free Hands-On Lab 🧪

https://overthewire.org/wargames/bandit/bandit0.html
---
### 🔄 Alternatives

Assignment: Compare Linux-related approaches:

* Vim vs Nano
* systemd vs traditional init systems

Deliverable:

* 1–2 sentences comparison
* Include a simple use case for each

---

### 🎯 User Story & Scenario

Assignment: Describe a simple real-world Linux administration scenario.

Possible examples:

* Investigating disk usage on a server
* Restarting a failed service
* Troubleshooting a full filesystem
* Managing permissions for an application

Deliverable:

* 2 paragraphs describing the issue and solution approach

