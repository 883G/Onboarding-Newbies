# Airflow Fundamentals:
## Overview
This section will go over the fundamentals of _`Apache Airflow`_, consisting of the client side, and the backend.

**We will focus on general concepts of Airflow, the flow of the tasks and how does client code look like.**

## Goals
- Master the fundamental Airflow abstractions and authoring models.
- Understand the core backend architecture, the responsibilities of each component, and how they evolve from Airflow 2 to Airflow 3.
- Trace the end-to-end lifecycle of a `Dag` and `TaskInstance`, from code parsing and `Dag` synchronization (including `DAGBundles`) to `Scheduler` critical loops and `Worker` execution.
- Evaluate the mechanics of data and state passing, distinguishing between metadata sharing, global configuration, and resource-efficient patterns.
- Compare Airflow’s orchestration approach against industry alternatives to justify its usage in production data pipelines.

### :warning: **Note:**
- This is a self-study day. Independence and time management are essential.
- Many newcomers struggle with self-study; take a moment to plan your day and stick to it.
- Understand the **big picture** of each concept. If you can't explain it, you probably haven't learned it.
- Be prepared to describe how concepts relate to one another and to real-world scenarios.
- When in doubt about what you need to learn, ask your mentor.

### Core Concepts

Think through the following questions; by answering them you’ll touch every major topic listed above:


1. **Airflow User API & Concepts:** Explain the difference between a DAG and a DagRun? How do tasks share small metadata versus global configuration? What is Jinja Templating, and why would you use {{ ds }} instead of Python's datetime.now()? Contrast the TaskFlow SDK with Classic Operators. How does the TaskFlow SDK handle XComs differently than the old xcom_pull method? What are Assets? What types of Operators exist? Why is it not recommended to run any time consuming code in top level dag code? How does this affect the DAG Processor's performance? What is a Hook? what is the connection between Hooks, Connections and Operators?

2. **Airflow Backend & Architecture:** What are the different components in the Airflow architecture? Define the roles of each component. Why is the `Executor` considered a mechanism/logic rather than a standalone service? Explain the `Deferrable Operator`. Which component makes these possible, and how do they save money/resources in a Big Data stack? What are `Airflow Providers`? and what are the main changes between Airflow 3 and Airflow 2?

3. **Airflow Security:** How does the airflow security model look like? both arcihtecture-wise and client-wise? how can I integrate airflow with different authentication backends and types? (as if LDAP or SSO), what are the available permissions that exist in airflow (find place in docs)?

4. **Airflow Task Lifecycle:** What is the full flow of a Dag from being written to being run? What happens when the `Dag Processor` encounters your file? How is `Jinja` parsing different in Dag processing than execution time? At which state does the `Scheduler` stop managing the task, and hand it over to the `Executor`? What is the flow when a task gets to a `Worker`? When does it start running?

5. **Airflow Critical Sections:** What is the `'Critical Section'` of the `Scheduler`? Describe the 4 primary `Critical Sections` (`Dag Run` Creation, `Dag Run` Scheduling, `TaskInstance` Creation, `Task` Scheduling).

### Real-World Context
Rather than focusing on one technology, think about how data workflows are scheduled, and think about when running and orchestrating data workflows.

## 🔄 Alternatives

Assignment: You are required to research and write a comparative analysis between Airflow and an industry alternative.

    Deliverable: A written summary (minimum 1 or 2 sentences).
    Focus: Compare performance, architecture, and specific "pain points" this tool solves compared to legacy systems or competitors.
    Goal: You must be able to justify why the department uses this tool for our specific environment.

## 🎯 User Story & Scenario

Assignment: Based on your research and understanding of the department's pipeline, define a concrete Use Case for this technology.

    Deliverable: A written summary example/story (two sentences approx.).
    Requirement: Describe a real-world scenario (e.g., a specific client requirement) where this technology is the optimal solution.
    Data Flow: Map out the data flow and explain how this tool integrates with other components in the Data Pipeline.


## Wrapping Up :trophy:
Discuss your answers and any areas of confusion with your mentor. Reflect on how these general concepts will help when you later when using scheduled jobs.

## Additional Topics from Review
- A deep dive into the Airlfow database and the inner workings of Airflow.
- A deep dive into bugs solved and unsolved inside Airflow.

## Action Items
- Review your notes and identify topics you want to explore deeper.
- Collect a list of real-world schedulers and their algorithms.
- Prepare questions for the upcoming mentor Q&A session.

## Completion Checklist

- You understand the airflow architecture and can explain in detail what each component does
- You understand airflow on the applicative side, where you know how to author dags
- You understand how airflow manages it's security
- You understand what happens to the task from start to end
- You understand at each tasks state what happens to it and can tell where it is stuck if it is

## Recommemded Resources
- [Airflow Docs](https://airflow.apache.org/docs/)
