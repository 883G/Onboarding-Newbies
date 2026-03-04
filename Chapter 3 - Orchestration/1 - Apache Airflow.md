# Orchestration Fundamentals:
## Overview
This section will go over the fundamentals of _Apache Airflow_, consisting of the client side, and the backend.

**We will focus on general concepts of airflow, the flow of the tasks and how does client code look like.**

## Goals
- Develop a foundational understanding of how scheduling is done.
- Learn the common terminology used by most schedulers.
- Practice planning a self-study day and estimating time for learning.

:warning: **Note:**
- This is a self-study day. Independence and time management are essential.
- Many newcomers struggle with self-study; take a moment to plan your day and stick to it.
- Understand the **big picture** of each concept. If you can't explain it, you probably haven't learned it.
- Be prepared to describe how concepts relate to one another and to real-world scenarios.
- Review the [Exercise](#exercise) before diving in so you know what to focus on.
- When in doubt about what you need to learn, ask your mentor.

### Core Concepts

Think through the following questions; by answering them you’ll touch every major topic listed above:

Question 1: The User’s Blueprint & Dynamic Logic

In Airflow, we write "Workflows as Code," but that code needs to adapt to different execution dates.

    Definitions: Explain the difference between a DAG and a DagRun. Why is this distinction important when backfilling data?

    Communication: How do tasks share small metadata (like a file path) versus global configuration (like an API key)? (XComs vs. Variables).

    The Magic of Jinja: What is Jinja Templating, and why would you use {{ ds }} instead of Python's datetime.now() inside an operator's parameters?

    Modern vs. Classic: Contrast the TaskFlow SDK (decorators) with Classic Operators. How does the TaskFlow SDK handle XComs differently than the old xcom_pull method?

    The New Guard: What are Assets (Datasets), and how do they shift Airflow from "time-based" scheduling to "event-driven"?

Question 2: The Anatomy of the Engine (System Components)

Airflow is a distributed system where responsibilities are strictly separated.

    The Services: Define the roles of the Scheduler, API Server, Triggerer, and DAG Processor.

    The "Not-a-Service": Why is the Executor considered a mechanism/logic rather than a standalone service?

    Efficiency: Explain the Deferrable Operator. Which component makes these possible, and how do they save money/resources in a Big Data stack?

Question 3: Code Delivery & Evolution (Syncing & Bundles)

Getting your code from your IDE to the production cluster has evolved significantly.

    The Airflow 2 Way: How were DAGs typically synchronized to the Scheduler and Workers in Airflow 2 (e.g., Git-Sync)? What was the main risk of this approach?

    The Airflow 3 Innovation: What is a DAG Bundle, and how does it solve the "version mismatch" problem between the Scheduler and the Worker?

    Independence: How do Bundles allow different teams to manage their own code dependencies without affecting the core Airflow installation?

Question 4: The Lifecycle of a Task (The "Green Box" Journey)

Trace the path of a task from a git push to a successful run.

    Deployment: What happens when the DAG Processor encounters your file? How does it handle Jinja templates during the parsing phase versus the execution phase?

    The State Machine: Walk through the transitions: None → Scheduled → Queued → Running → Success.

    The Hand-off: At which exact state does the Scheduler stop managing the task and hand it over to the Executor?

Question 5: The "Critical Section" & Performance

The Scheduler is a high-performance loop. If it stalls, your data pipeline stalls.

    The Heartbeat: What is the "Critical Section" of the Scheduler?

    Internal Loops: Describe the three primary "loops" or critical sections:

        DagRun Creation: (Checking start dates and schedules).

        Task Instance Creation: (Evaluating dependencies/upstreams).

        Task Prioritization: (Moving tasks from scheduled to queued).

    The Golden Rule: Why is it dangerous to perform a heavy Big Data operation (like a df.read()) at the top level of a DAG file? How does this affect the DAG Processor's performance?

### Real-World Context
Rather than focusing on one technology, think about how these ideas show up in schedulers, such as the linux scheduler or k8s scheduler.

🔄 Alternatives

Assignment: You are required to research and write a comparative analysis between Airflow and an industry alternative.

    Deliverable: A written summary (minimum 1 or 2 sentences).
    Focus: Compare performance, architecture, and specific "pain points" this tool solves compared to legacy systems or competitors.
    Goal: You must be able to justify why the department uses this tool for our specific environment.

🎯 User Story & Scenario

Assignment: Based on your research and understanding of the department's pipeline, define a concrete Use Case for this technology.

    Deliverable: A written summary example/story (two sentences approx.).
    Requirement: Describe a real-world scenario (e.g., a specific client requirement) where this technology is the optimal solution.
    Data Flow: Map out the data flow and explain how this tool integrates with other components in the Data Pipeline.


## Wrapping Up :trophy:
Discuss your answers and any areas of confusion with your mentor. Reflect on how these general concepts will help when you later when using scheduled jobs.

## Additional Topics from Review
- A deep dive into spark internals: what are other optimizations that are implemented in spark? what is java off-heap memory? how does spark's memory allocation work?
- What are the different obsolescence algorithms widely used? where could they also be implemented?

## Action Items
- Review your notes and identify topics you want to explore deeper.
- Collect a list of real-world schedulers and their algorithms.
- Prepare questions for the upcoming mentor Q&A session.

## Recommemded Resources
- [Starvation and Aging GFG](https://www.geeksforgeeks.org/operating-systems/starvation-and-aging-in-operating-systems/)
- [Hadoop Capacity Scheduler](https://hadoop.apache.org/docs/stable/hadoop-yarn/hadoop-yarn-site/CapacityScheduler.html)
- [AWS Exponential Backoff and Jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/)
- [Priority Scheduling Slurm](https://slurm.schedmd.com/priority_multifactor.html)
- [Operating Systems Scheduling Stanford University](https://web.stanford.edu/~ouster/cgi-bin/cs140-spring14/lecture.php?topic=scheduling)
