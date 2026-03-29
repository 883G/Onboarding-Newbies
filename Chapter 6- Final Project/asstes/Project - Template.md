
## 1. Project Overview
**Project Name:**  
**Date:**  

**Scenario / Story:**  
> Minimal description to justify using the stack (Airflow, Spark, Trino, S3/HDFS, SQL).  

**Core Requirements:**  
> Briefly describe the goal of the pipeline (e.g., event analytics, ETL for reporting, operational monitoring).  

---

## 2. Data Characteristics
- **Data Types:** (e.g., events, logs, CSV files)  
- **Data Volume:** (e.g., GB/day, millions of rows)  
- **Arrival Frequency:** (e.g., batch, streaming, hourly)  
- **Latency Requirements:**  

---

## 3. Pipeline Architecture
**End-to-End Diagram:**  
> Include diagram showing data flow.  

**Components & Responsibilities:**  
- **Ingestion:**  
- **Storage (S3/HDFS):**  
- **Processing (Spark):**  
- **Orchestration (Airflow):**  
- **Query Layer (Trino + SQL):**  

---

## 4. Storage Design
- **Partitioning Strategy:**  
- **File Formats:** (Parquet/ORC/etc.)  
- **Lifecycle Policies / Retention:**  
- **Include ERD (SQL)**

---

## 5. Processing Design (Spark)
- **Job Structure / Pipelines:**  
- **Transformations / Aggregations:**  
- **Retries / Failure Handling:**  
- **Scalability Considerations:**  

---

## 6. Orchestration Design (Airflow)
- **DAG Structure / Dependencies:**  
- **Scheduling:**  
- **Retries & Backfills:**  
- **Monitoring & Alerting:**  

---

## 7.Trino
- **Query Patterns:**  
- **Optimizations (joins, partition pruning, aggregations):**  
- **Trade-offs / Limitations:**  

---

## 8. Operational Considerations
- **Monitoring / Logging:**  
- **Failure Recovery:**  
- **Scaling:**  

---

## 9. Trade-offs & Limitations
- **Pros:**  
- **Cons:**  
- **Alternative Designs Considered:**  

---

## 10. Future Improvements
- **Scaling Strategies:**  
- **Performance Tuning:**  
- **Automation / Observability:**  
- **Other Enhancements:**  

---
