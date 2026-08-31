## Onboarding Final Exercise 🚀

This exercise is about designing and presenting a complete data pipeline architecture using the department stack: **Airflow, Kafka, NiFi, Spark, Trino, S3/HDFS, Git/VCS, Helm, and Argo**.  
The main focus is the pipeline and the technologies behind it.  
Each trainee must choose a project idea from the **mentor-provided list only**. You are not allowed to pick your own topic or invent a project.  
The business scenario is only there to justify the technology choices, not the other way around.  
This is a **design exercise only**. You are expected to explain the architecture, reasoning, and trade-offs, but you are not required to build the actual code, jobs, or deployment.  
Please avoid using AI tools or looking at previous members’ project documents for examples.  

---
### ⏳ Timeline
Total duration: **1 week + 1 day presentation**

#### **Week 1: Planning and Design**
- Identify the minimal business context that justifies the stack.  
- Define the data types, volume, frequency, and latency requirements.  
- Sketch the full end-to-end pipeline, including ingestion, storage, processing, orchestration, and querying.  
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
   - **Kafka / NiFi**: data movement, ingestion, buffering, streaming, reliability, and decoupling.  
   - **Airflow**: orchestration, dependencies, retries, and scheduling.  
   - **Spark**: distributed processing, transformations, and aggregations.  
   - **Trino**: analytics, joins, aggregations, and partition pruning.  
   - **S3/HDFS**: storage, partitioning, and cost-performance trade-offs.  
   - **Git / VCS**: version control, collaboration, and change tracking.  
   - **Helm**: packaging and deployment consistency across environments.  
   - **Argo**: GitOps delivery, environment promotion, and continuous deployment.  
   - **One additional technology not covered in the training**: include one technology outside the formal training materials and explain why it fits into the architecture. This should be chosen with mentor guidance and justified clearly in the design.  
3. **The project idea must come only from the mentor’s list**.  
4. **The scenario should only be used to justify the pipeline design**, not to become the main focus.  
5. **Trade-offs and decisions must be documented clearly**, including performance, scaling, and operational complexity.  
6. **Operational considerations must be included**, such as monitoring, alerting, retries, and failure handling.  
7. **There is no RDBMS requirement in this exercise**. The focus is on modern data movement, storage, analytics, and deployment patterns.  

---
### 🎯 User Story and Minimal Scenario

The scenario should be brief and only provide the business context needed to explain the pipeline and technology choices.

You can define it by:
- choosing a fictional organization or business domain
- identifying a problem that requires a data pipeline
- describing the type of data generated, how often it arrives, and why it needs to be processed

The goal is not storytelling. The main goal is to explain why the architecture makes sense.

The scenario should stay minimal, because the exercise is focused on the architecture and technology choices, not the business narrative.

Example scenarios include:
- event analytics for a digital platform
- daily ETL for reporting
- operational monitoring or log analytics

The data flow should be clear:  
**Kafka / NiFi → S3/HDFS → Spark → Trino**  
The design should also show how **Git/VCS, Helm, and Argo** support deployment and delivery.

The key point is to explain the technology decisions, not to build a story around them.

> **Tip:** focus on design, trade-offs, and operational decisions.

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

1. **Data Movement Layer** – Kafka / NiFi design for ingestion, streaming, buffering, and reliability
2. **Airflow Orchestration** – DAG design with scheduling, retries, and monitoring logic
3. **Spark Processing Layer** – data processing design with transformations and aggregations
4. **Storage Layer Design** – file formats, partitioning, and retention strategies
5. **Query Layer (Trino)** – analytics design, query approach, and optimization considerations
6. **VCS and DevOps Layer** – Git/VCS workflow, Helm packaging, and Argo deployment strategy
7. **Additional Untrained Technology** – one technology not covered in the training, introduced and justified as part of the architecture
8. **Operational Considerations** – monitoring, alerting, logging, and failure recovery
9. **Trade-offs and Design Decisions** – clear reasoning behind the architecture choices

The emphasis is on architecture, reasoning, and technical explanation rather than building or deploying a real system.

---

### 🎯 Key Points to Remember
- The pipeline is the main focus.
- All required technologies should appear in the architecture: Kafka, NiFi, Airflow, Spark, Trino, S3/HDFS, Git/VCS, Helm, Argo, and one additional untrained technology.
- Project selection is controlled by the mentor.
- This is a design and presentation exercise, not a coding assignment.
- Be clear about the trade-offs around scale, reliability, and complexity.

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
  - Kafka / NiFi ingestion and data movement patterns  
  - Spark transformation and distributed processing  
  - Airflow orchestration and failure handling  
  - Trino optimization and partition pruning  
  - S3/HDFS partitioning, cost, and performance  
  - Git/VCS workflow and release management  
  - Helm packaging and Argo deployment strategy  
  - the additional untrained technology and why it fits the architecture  
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
