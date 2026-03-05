## Onboarding Final Exercise 🚀

This exercise focuses on **designing and presenting a complete data pipeline architecture** using the department’s stack: **Airflow, Spark, Trino, S3/HDFS, SQL**.  
The **pipeline and technologies are the core** of this exercise.  
The scenario/story exists **only to justify the usage of these technologies**, not the other way around.  

---

### ⏳ Timeline
Total Duration: 2 Weeks + 1 Day Presentation

#### **Week 1: Planning & Design**
  - Identify minimal business context that justifies each technology in the stack.  
  - Define data types, volume, arrival frequency, and latency requirements.  
  - Sketch **end-to-end pipeline** including ingestion, storage, processing, orchestration, and query layers.  
  - Decide **S3/HDFS layout, partitioning, file formats**, and lifecycle policies.  
  - Define **Spark job structure**, transformations, dependencies, and failure handling.  
  - Draft Airflow DAGs: scheduling, dependencies, retries, and monitoring.  

#### **Week 2: Execution & Refinement**
  - Finalize pipeline architecture diagrams.  
  - Model **Trino tables and queries** with optimizations for partitioning, joins, and aggregations.  
  - Validate pipeline: simulate workflow orchestration, scaling, and failure scenarios.  
  - Document pros/cons of each design decision within the stack.  
  - Refine architecture and operational strategies.  
  - Prepare **team-focused discussion points** emphasizing design choices and trade-offs.  

#### ** Last Day: Presentation**
- Create **full pipeline architecture** to the team.  
- Lead **technical discussion**:
  - Explain why each technology is used and how it integrates.  
  - Show **data flow**, orchestration, and query execution.  
  - Discuss scalability, fault tolerance, and operational strategies.  
  - Highlight limitations, trade-offs, and future improvements.  

---

### 📚 Resources
Utilize the resources listed below and master the skill of searching the internet for questions that are not answered by the added documentation.
- [Project Template](./asstes/Project%20-%20Template.md)
- [Presentation Template](./asstes/Presentation%20Template.pptx)
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/) – distributed data processing, transformations, and performance tuning  
- [Apache Airflow Documentation](https://airflow.apache.org/docs/) – DAG design, scheduling, retries, and monitoring  
- [Trino Documentation](https://trino.io/docs/current/) – distributed SQL engine, query optimization, partition pruning  
- [AWS S3 Docs](https://docs.aws.amazon.com/s3/index.html) 
- [HDFS Design Docs](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html) – data lake storage, partitioning, lifecycle  

> **Tip:** Focus on **design, trade-offs, and pipeline operation**

---

### 🏗 Core Exercise Requirements
1. **Pipeline must be central** – show all steps !
2. **Technologies must be justified**:  
   - **Airflow**: orchestrate dependencies, retries, scheduling.  
   - **Spark**: distributed processing, transformations, aggregations.  
   - **Trino**: query analytics, joins, aggregations, partition pruning.  
   - **S3/HDFS**: scalable storage, partitioning, cost-performance balance.  
   - **SQL**: schema definition, querying, and integration with Trino.  
3. **Scenario/story** exists **only to justify pipeline design**.  
4. **Trade-offs & decisions** must be clearly documented: scaling, performance, operational complexity.  
5. **Operational considerations** must be included: monitoring, alerting, retries, failure handling.

---

### 🎯 User Story & Minimal Scenario
- Scenario must **justify pipeline design**, e.g., event analytics, daily ETL for reporting, operational monitoring.  
- Show **data flow** clearly: ingestion → S3/HDFS → Spark → Trino → SQL queries.  
- Emphasize **technology choices**, not storytelling.  
---

### 📝 Architecture Deliverables
- **Pipeline Diagram**: end-to-end data flow and interactions between components  
- **Storage Design**: partitioning, file formats, lifecycle  
- **Processing Design**: Spark job structure, transformations, retries, backfills  
- **Orchestration Design**: Airflow DAG structure, scheduling, monitoring  
- **Query Layer Design**: Trino tables, optimizations, partition pruning  
- **Operational Design**: monitoring, alerting, automated recovery  
- **Trade-offs & Limitations**: pros/cons of design decisions  
- **Future Improvements**: scaling, performance, operational automation  

---

### 🔎 Technical Discussion Focus
- **Explain why each technology is mandatory** for this pipeline.  
- **Show data flow** from ingestion to query.  
- **Discuss scalability** and **fault tolerance**.  
- **Highlight trade-offs** between performance, maintainability, and operational complexity.  
- **Show failure handling**: retries, backfills, monitoring.

---

### 🎨 Presentation Tips
- Diagrams should illustrate **data flow and component interactions**.  
- Focus on **design decisions and architecture**, not scenario narrative.  
- Prepare for questions on:
  - Spark transformations and distributed processing  
  - Airflow DAG orchestration and failure handling  
  - Trino query optimizations and partition pruning  
  - S3/HDFS partitioning, cost, and performance  
  - SQL integration with Trino  
  - Pipeline scaling and operational complexity
