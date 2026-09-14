## Onboarding Final Exercise 🚀

This exercise is about designing and presenting a complete data pipeline architecture using the department stack: **ingestion layer, Airflow, Spark, Trino, S3/HDFS, and Hive/Iceberg table format**.  
The main focus is the pipeline and the technologies behind it.  
Each trainee must choose a project idea from the **mentor-provided list only**. You are not allowed to pick your own topic or invent a project.  
The business scenario is only there to justify the technology choices, not the other way around.  
This is a **design exercise only**. You are expected to explain the architecture, reasoning, and trade-offs, but you are not required to build the actual code or jobs.  
Please avoid using AI tools or looking at previous members’ project documents for examples.  

---
### ⏳ Timeline
Total duration: **1 week + 1 day presentation**

#### **Week 1: Planning and Design**
- Identify the minimal business context that justifies the stack.  
- Define the data types, volume, frequency, and latency requirements.  
- Sketch the full end-to-end pipeline, including ingestion, storage, processing, orchestration, and querying.  
- Design the relevant SQL queries that will be used for analytics and reporting, and include them in the final design package.  
- Decide on storage layout, partitioning, file formats, and lifecycle policies.  
- Define the Spark processing flow, transformations, dependencies, and failure handling.  
- Draft the Airflow DAG design, including scheduling, dependencies, retries, and monitoring.  

#### **Last Day: Presentation**
- Prepare a presentation with the full architecture.  
- Lead a technical discussion covering:  
  - why each technology is used and how they fit together  
  - the data flow and orchestration path  
  - scalability, fault tolerance, and operational strategy  
  - trade-offs, limitations, and future improvements  

---
### 🏗 Core Requirements
1. **The pipeline should be the central part of the exercise** and all stages should be clearly visible.
2. **All technologies in the stack must appear in the design**:  
  - **Ingestion Layer**: data movement, ingestion, buffering, streaming, reliability, and decoupling.  
   - **Airflow**: orchestration, dependencies, retries, and scheduling.  
   - **Spark**: distributed processing, transformations, and aggregations.  
   - **Trino**: analytics, joins, aggregations, and partition pruning.  
   - **S3/HDFS**: storage, partitioning, and cost-performance trade-offs.  
  - **Hive/Iceberg table format**: table management, schema evolution, and metadata handling.
 
5. **Trade-offs and decisions must be documented clearly**, including performance, scaling, and operational complexity.  
6. **Operational considerations must be included**, such as monitoring, alerting, retries, and failure handling.  
7. **The trainee must design and include SQL queries** that match the business questions, transformations, and reporting layer of the pipeline.  


---
### 🎯 User Story and Minimal Scenario

The scenario should be brief and only provide the business context needed to explain the pipeline and technology choices.
---

## 🧩 Project Selection and Planning

### ⚠️ Mentor-Approved Project Ideas Only

Before starting the final project, speak with your mentor and ask for the official project ideas list.  
You must choose exactly one project from that list.  

Rules:
1. Do not propose your own idea.
2. Do not choose a project outside the mentor list.
3. Use the mentor’s guidance to select the most suitable option.
4. Discuss the scope and constraints with your mentor before you begin.

Your mentor can help you with:
- understanding the business context
- defining the technical scope
- making sure the architecture covers the required stack
- reviewing your design decisions and trade-offs

---

### 📋 Required Design Deliverables

Once you have selected a project from the mentor list, the final submission should be a design-focused presentation that includes:

1. **Data Movement Layer** – ingestion layer design for ingestion, streaming, buffering, and reliability
2. **Airflow Orchestration** – DAG design with scheduling, retries, and monitoring logic
3. **Spark Processing Layer** – data processing design with transformations and aggregations
4. **Storage Layer Design** – file formats, Hive/Iceberg table format, partitioning, and retention strategies
5. **Query Layer (Trino)** – analytics design, query approach, optimization considerations, and the required SQL queries for the use case
6. **Operational Considerations** – monitoring, alerting, logging, and failure recovery
7. **Trade-offs and Design Decisions** – clear reasoning behind the architecture choices
8. **SQL Query Design** – include the relevant SQL queries the trainee designed to answer business questions and support reporting/analytics

The emphasis is on architecture, reasoning, and technical explanation rather than building or deploying a real system.

---

### 📞 Mentor Support
Your mentor is the main source of feedback for:
- project selection and validation
- architecture review
- clarifying technical expectations
- design validation before submission

Ask your mentor early and often.

---

### 🎨 Presentation Tips
- Use diagrams to show data flow and component interaction.  
- Focus on design decisions and architecture rather than story writing.  
- Be ready to answer questions on:
  - Ingestion layer data movement patterns  
  - Spark transformation and distributed processing  
  - Airflow orchestration and failure handling  
  - Trino optimization and partition pruning  
  - S3/HDFS partitioning, cost, and performance  
  - Hive/Iceberg table format, schema evolution, and metadata management  
  - pipeline scalability and operational complexity

[Template for Presentation](./asstes/Presentation%20Template.pptx)

### 📚 Resources
Use the following resources and practice searching the internet when the documentation is not enough.
- [Project Template](./asstes/Project%20-%20Template.md)
- [Presentation Template](./asstes/Presentation%20Template.pptx)
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/) – distributed data processing, transformations, and performance tuning  
- [Apache Airflow Documentation](https://airflow.apache.org/docs/) – DAG design, scheduling, retries, and monitoring  
- [Trino Documentation](https://trino.io/docs/current/) – distributed SQL engine, query optimization, and partition pruning  
- [AWS S3 Docs](https://docs.aws.amazon.com/s3/index.html) 
- [HDFS Design Docs](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html) – storage, partitioning, and lifecycle  
