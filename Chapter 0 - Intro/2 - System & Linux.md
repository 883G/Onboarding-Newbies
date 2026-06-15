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

---

# Linux & Infrastructure Core Concepts

### ❓ Guide Questions

1. **What is the Linux kernel and how does Linux separate kernel space from user space?**

   Explain:
   * What the kernel is and how it forms the core of a Linux system
   * Kernel responsibilities and how user-space programs differ from kernel-space code
   * What makes the Linux kernel unique compared to other operating systems
   * Open source aspect: how distributions build on a shared kernel with different userland stacks
   * User space vs kernel space
   * System calls and how programs request services from the kernel
   * Why isolation matters
   * Examples of common system calls (open, read, write, execve)
   * Kernel modules and drivers

2. **How does the Linux filesystem work and how is data organized?**

   Explain:
   * File systems and directory hierarchy
   * Inodes
   * Root filesystem (`/`)
   * Mount points
   * `/etc/fstab`
   * `mount` and `df` commands
   * Filesystem types and use-cases (ext4, xfs, btrfs, tmpfs, vfat, ntfs)
   * LVM and logical volume management concepts
   * Permissions, ownership, and Linux permission model (user/group/others, rwx)
   * Special permission modes (sticky bit, setuid/setgid)
   * Inode structure vs directory entries
   * Journaling, fsck, and safe recovery practices
   * Basic commands: `lsattr`, `chown`, `chmod`, `stat`

3. **How are processes and services managed in Linux?**

   Explain:
   * Processes vs daemons
   * Process lifecycle
   * Privileges and root user
   * systemd and init systems
   * Service management basics
   * Process primitives: PID, PPID, sessions, process groups
   * Signals (SIGTERM, SIGKILL, SIGHUP) and how to send/handle them (`kill`, `trap`)
   * Inspecting processes: `ps`, `top`, `htop`, `pstree`
   * Journaling and logs: `journalctl`, `/var/log/*`
   * Runlevels/targets and unit file basics for systemd (`.service`, `.socket`)
   * Basic system services: ntpd (network time protocol), DHCP, DNS services
   * Init.d and service initialization basics
   * Starting, stopping, and managing services with `systemctl` and `/etc/init.d/`

4. **How does Linux isolate and control resources?**

   Explain:
   * cgroups
   * namespaces
   * CPU/memory isolation
   * Container foundations
   * Why containers rely on these primitives
   * Practical tools: `cgcreate`, `systemd-run --scope`, `unshare`, `nsenter`
   * Network namespaces and virtual interfaces (veth)
   * Resource monitoring: `cgroupfs`, `systemd-cgls`

5. **What are the essential GNU/Linux command-line tools and editing utilities?**

   Explain and demonstrate basic usage of:
   * `ls`
   * `cd`
   * `cat`
   * `cp`
   * `rm`
   * `touch`
   * `head`
   * `tail`
   * `du`
   * Vim basics
   * Nano basics
   * Searching and text processing: `grep`, `awk`, `sed`, `sort`, `uniq`
   * File transfer and networking: `ssh`, `scp`, `rsync`, `curl`
   * Package management basics (apt, yum, dnf) and checking versions
   * Shell basics: environment variables, piping, redirection, and simple scripting

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

