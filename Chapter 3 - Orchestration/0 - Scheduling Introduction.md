# Orchestration Fundamentals:
## Overview
This section will go over the fundamentals of _orchestration_, consisting of _scheduling_ and _resource management_.

**We will focus on general concepts such as scheduling algorithms, preemptive vs non-preemptive scheduling and prioritization.**

## Goals
- Develop a foundational understanding of how scheduling is done.
- Learn the common terminology used by most schedulers.
- Practice planning a self-study day and estimating time for learning.

:warning: **Note:**
- This is a self-study day. Independence and time management are essential.
- Many newcomers struggle with self-study; take a moment to plan your day and stick to it.
- Understand the **big picture** of each concept. If you can't explain it, you probably haven't learned it.
- Be prepared to describe how concepts relate to one another and to real-world scenarios.
- When in doubt about what you need to learn, ask your mentor.

### Core Concepts

Think through the following questions; by answering them you’ll touch every major topic listed above:

1. **Scheduling Basics:** Why can’t we just use a simple sleep() command or a basic cron job to manage a modern data workflows? What is the difference between a Time-based trigger and an Event-based trigger? Give a real-world data example for each, In general scheduling, why do we use a DAG to represent a workflow instead of just a simple list of instructions?

2. **Scheduling Algorithms & Types:** Compare First-In-First-Out (FIFO) and Shortest Job First (SJF), how do they handle varying workflows? Define Preemptive vs. Non-preemptive scheduling, If a "Critical" job enters the queue while a "Low" priority job is already running, what happens in both scenarios? What is "Starvation" in priority scheduling, and how does the concept of Aging fix it? what are other common algorithms to fix starvation?

3. **Scheduling & Priorities:** Explain the difference between Pessimistic Scheduling (Priority Blocking) and Optimistic Scheduling (Resource Maximization), If a "High Priority" job needs 100 CPUs but only 80 are available, how does a Pessimistic scheduler treat the remaining 20 "Low Priority" jobs in the queue compared to an Optimistic one? How do Resource Pools (or Slots/Concurrency limits) help a scheduler "sandbox" different types of work?

4. **Resource Allocation & Scheduling:**Explain Dominant Resource Fairness (DRF). Why is it more "fair" to look at CPU and RAM usage rather than just task count? What is Capacity Scheduling, and how does it provide "guaranteed lanes" for different departments? Compare Static Allocation to Dynamic Allocation. Which one is safer for the system, and which one is more efficient for the cluster?

5. **Users Perspective:** Why is Idempotency the most important concept for a developer to understand when writing scheduled jobs? what is an Exponential Backoff when jobs fail? What is Backfilling, and how does it relate to the "Optimistic" approach of keeping resources busy?


### Real-World Context
Rather than focusing on one technology, think about how these ideas show up in schedulers, such as the linux scheduler or the trino task scheduler.

## Wrapping Up :trophy:
Discuss your answers and any areas of confusion with your mentor. Reflect on how these general concepts will help when you later when using scheduled jobs.

## Additional Topics from Review
- A deep dive into sheduling algorithms.
- What are the different obsolescence algorithms widely used? where could they also be implemented? what are some scheduling algorithms without preemption and aging that solve starvation?

## Action Items
- Review your notes and identify topics you want to explore deeper.
- Collect a list of real-world schedulers and their algorithms.
- Prepare questions for the upcoming mentor Q&A session.

## Recommemded Resources
- [Priority Scheduling Slurm](https://slurm.schedmd.com/priority_multifactor.html)
- [Operating Systems Scheduling Stanford University](https://web.stanford.edu/~ouster/cgi-bin/cs140-spring14/lecture.php?topic=scheduling)
