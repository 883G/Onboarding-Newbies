# Spark Fundamentals

## Overview
This is a self-study day on the fundamentals of **Apache Spark** — the compute layer of our datalake platform.

**You'll focus on general concepts: Spark's architecture and execution model, planning & optimization, shuffle & joins, memory management, and how Spark is configured and tuned in our environment (PySpark on Kubernetes).**

The goal is not to memorize definitions. For each concept, aim to explain the **big picture in your own words** and connect it to the others — in the oral exam you'll be asked to reason, not recite.

## Goals
- Build a foundational mental model of how Spark **plans and executes** a job.
- Learn the core terminology (Driver, Executor, Job/Stage/Task, DAG, Shuffle, Catalyst, partition…) well enough to use it fluently.
- Understand how Spark **manages memory** and how it's **configured** — especially in a multi-tenant, PySpark-on-Kubernetes setup.
- Practice planning a self-study day and estimating your own learning time.

:warning: **Note:**
- This is a self-study day. Independence and time management are essential.
- Many newcomers struggle with self-study; take a moment to plan your day and stick to it.
- Understand the **big picture** of each concept. If you can't explain it, you probably haven't learned it.
- Be prepared to describe how concepts relate to one another and to real-world scenarios.
- Skim the [assignments](#-alternatives) and the exercise in Core Concept 1 before diving in, so you know what to focus on.
- When in doubt about what you need to learn, ask your mentor.

### Core Concepts

Think through the following. Treat them as a **rough map of the territory**, not a checklist — they point you at the areas to research, and in the oral exam the examiner will drill deeper into each. If you've truly done the research you'll be able to follow those deeper questions; if you only skimmed the outline, it will show.

1. **Spark Architecture & Execution:** What are the main components of Spark, and what is the role of each? Where can the Driver and Executors run, and what does `spark-submit` do? What is the difference between a transformation and an action? What is lazy execution in Spark? What happens between calling an action and work running on the executors — how does the work break down, and what causes those boundaries? What is a DAG, and how does Spark use it, both to schedule work and to achieve fault tolerance? What is the difference between `SparkContext` and `SparkSession`? Go over [this file](assets/where_do_i_run.py) and, for each line, comment on where it runs.

2. **Spark Planning & Optimization:** Logical vs. Physical Planning — walk through the transition from Logical Plan to Physical Plan. What is the fundamental difference between Rule-Based (RBO) and Cost-Based (CBO) optimization, and what are the common kinds of optimizations used? What is AQE? Why is running `ANALYZE TABLE` recommended for performant CBO? And what is whole-stage code generation?

3. **Spark Shuffle & Joins:** Compare the different kinds of joins — when will Spark use each, and how can we tell Spark to prefer one over another? What is join reordering? Why is "broadcasting" considered a high-risk, high-reward optimization? What is a *Narrow* transformation and a *Wide* transformation? Why do some operations require a shuffle? What exactly is written in a shuffle?

4. **Tungsten, Abstractions & Memory:** What is an RDD? Why did Spark move away from RDDs in favor of DataFrames/Datasets? Explain how Tungsten uses off-heap memory to avoid Garbage-Collection pauses. Why is it a bad idea to give one executor a lot of resources (the "Fat Executor" problem)? What is the difference between Execution/Storage memory and overhead memory, and what happens when a task exceeds its allotted execution memory? In PySpark specifically, where does the Python worker's memory live relative to the JVM heap — and why can heavy Python UDFs cause memory trouble the JVM heap won't show? On Kubernetes, how does all of this relate to `memoryOverhead` and to a pod being `OOMKilled`?

5. **Spark Skew, Partitioning & Caching:** What is data skew, and how can it be solved? What is the difference between `repartition(n)` and `coalesce(n)`? What are the Spark `StorageLevel`s? What is the difference between `cache` and `persist`? Why are UDFs (especially in Python) bad, and how does Spark address the serde bottleneck with UDFs?

6. **Configuration & Tuning:** What configs would you expect to set for a typical job, and how do they shape its parallelism and memory? What is dynamic allocation, and what does it rely on (keeping in mind there is no external shuffle service on Kubernetes)? When the same setting is defined in more than one place — in the SparkSession, injected by Airflow, and in `spark-defaults` — how does Spark decide which one wins, and which settings can't be changed once the application has started? If a tenant sets a config and it seems to have no effect, how would you investigate — and how do you check what configuration a running application actually has?

### Real-World Context
Rather than focusing on one technology in isolation, think about how these ideas show up across distributed processing frameworks — how other engines handle the same problems, and what the *core concepts* of distributed processing are.

## :arrows_counterclockwise: Alternatives

Assignment: research and write a short comparative analysis between Spark and an industry alternative.

- **Deliverable:** a written summary (a sentence or two).
- **Focus:** compare performance, architecture, and the specific "pain points" Spark solves. Cover **Trino** specifically — it's the ad-hoc / analytical query engine that sits alongside Spark in our datalake — and, for historical context, how Spark improved on **MapReduce**.
- **Goal:** be able to justify **when we reach for Spark vs. Trino** in our environment — and when you would *not* use Spark at all.

## :dart: User Story & Scenario

Assignment: based on your research and understanding of the department's pipeline, define a concrete Use Case for this technology.

- **Deliverable:** a written example/story (~two sentences).
- **Requirement:** describe a real-world scenario (e.g. a specific client requirement) where Spark is the optimal solution.

## Wrapping Up :trophy:
Discuss your answers and any areas of confusion with your mentor. Reflect on how these general concepts will help when you later write code and support clients.

## Additional Topics from Review
- A deeper dive into Spark internals: what other optimizations does Spark implement? How does Spark's memory allocation work end to end?
- What other well-known processing frameworks exist? Which use cases does Spark fit — and when should you *not* use it?

## Action Items
- Review your notes and identify topics you want to explore deeper.
- Collect a list of real-world use cases for Apache Spark.
- Prepare questions for the upcoming mentor Q&A session.

## Recommended Resources
- [Apache Spark Documentation](https://spark.apache.org/documentation.html)