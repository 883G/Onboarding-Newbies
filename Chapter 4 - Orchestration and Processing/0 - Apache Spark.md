# Spark Fundamentals:
## Overview
This section will go over the fundamentals of _apache spark_.

**We will focus on general concepts such as the spark architecture, optimizations, caching and data geometry.**

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

1. **Spark Architecture & Execution:** what are the main components of spark? why do we have each? what are their roles? what is the difference between a transformation and an action? how does spark achieve fault tolerance? what is lazy execution in spark? go over [this](./where_do_i_run.py) and for each line, comment where it runs.

2. **Spark Planning & Optimization:** Logical vs Physical Planning: Walk through the transition from Logical Plan to Physical Plan; What is the fundamental difference between Rule-Based (RBO) and Cost-Based Optimization (CBO), what are the common kinds of optimizations used? What is the AQE? Why is running ANALYZE TABLE recommended for performant CBO? and what is whole-stage code generation?

3. **Spark Shuffle & Joins:** Compare the different kind of joins, and when will spark use each? how can we tell spark to prefer one over the other? what is join reordering? and why is "broadcasting" considered a high-risk, high-reward optimization? What is a _Narrow_ transformation, and _Wide_ transformation? Why do some operations require shuffle? what exactly is written in shuffle?

4. **Tungsten & Resources in Spark:** What is an RDD? Why did Spark move away from RDDs in favor of DataFrames/Datasets? Explain how Tungsten uses off-heap memory to avoid Garbage Collection pauses. Why is it a bad idea to give one executor a lot of resources (the "Fat Executor" problem)? What is the difference between Execution/Storage memory and the overhead memory? What happens when a task exceeds its allotted execution memory?

5. **Spark Skew, Partitioning & Caching:** What is data skew? how can it be solved? what is the difference between `repartition(n)` and `coalesce(n)`? What are the spark `StorageLevel`s? what is the difference between `cache` and `persist`? why are udf's (expecially in python) bad? how does spark solve the serde bottleneck with udf's?


### Real-World Context
Rather than focusing on one technology, think about how these ideas show up in distributed processing frameworks, how they are used by other procerssing frameworks and what are the core concepts of processing.

## Wrapping Up :trophy:
Discuss your answers and any areas of confusion with your mentor. Reflect on how these general concepts will help when you later write code and help clients.

## Additional Topics from Review
- A deep dive into spark internals: what are other optimizations that are implemented in spark? what is java off-heap memory? how does spark's memory allocation work?
- What are other well known processing frameworks? what are the use cases spark meets? when should I NOT use spark?

## Action Items
- Review your notes and identify topics you want to explore deeper.
- Collect a list of real-world file systems you’d like to examine in future chapters.
- Prepare questions for the upcoming mentor Q&A session.
- Continue the Day 01 challenge by mapping these ideas to future chapters.

