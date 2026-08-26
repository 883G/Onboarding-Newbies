# Introduction to Core Data Concepts :baby:

## Goals

- Understand the data landscape and its core concepts.
- Explain the trade-offs involved in storing, processing, and serving data.
- Understand the CAP Theorem and apply it to distributed-system design decisions.
- Connect the concepts in this chapter into a realistic end-to-end data pipeline.
- Explain how data operations support reliable business decisions.

## **Overview**
Today’s session lays the foundation for your journey into data operations. You will examine the core concepts that underpin the modern data landscape and gain insight into data management, processing, and analysis. The emphasis is on appreciating how data drives business decisions and shapes the strategic direction of an organization.

> ⚠️ **Note:**  
> This is your first day in the world of data operations. Don’t worry about diving deeply into every topic; focus on understanding the big picture and the major concepts.

### ⏳ Timeline
Estimated Duration: 1 Day
- Day 1: Spend this day getting acquainted with the world of big data.
    - Hold a Q&A session immediately afterward

## 1. Understanding the Data Landscape

Research the following topics and look for real‑world examples. Discuss your findings with your mentor to deepen your understanding and clarify any questions. Keep a high‑level perspective, and consider the drawbacks of each concept as well as alternatives.

1. **The five V’s of Big Data**
2. **Structured, unstructured, and semi‑structured data**
3. **ETL vs. ELT**
4. **NoSQL vs. SQL databases**
5. **OLAP vs. OLTP**
6. **Batch processing vs. stream processing**
7. **Data warehouse vs. data lake**
8. **Distributed file systems**
9. **Data governance**
10. **Data visualization**
11. **Data analytics**
12. **Data ownership**
13. **Data quality**
14. **CDC (Change Data Capture)**
15. **Data catalog**
16. **Data lifecycle management**
17. **Data lineage**
18. **Store‑first approach**
19. **Data serialization**
20. **Data compression**
21. **Scale‑out vs. scale‑up**
22. **High availability**
23. **Master‑slave vs. masterless architectures**
24. **CAP Theorem**

These topics are meant to guide your research. Don’t hesitate to look up other relevant concepts.
</br>
> Note✅: Reinforce your understanding by relating the concepts to real‑world scenarios.

### CAP Theorem

In a distributed data system, a network partition can prevent nodes from communicating. During that partition, consider these three guarantees:

- **Consistency:** every read receives the latest successful write or an error.
- **Availability:** every request receives a non-error response, although it may not contain the latest data.
- **Partition tolerance:** the system continues operating despite communication failures between nodes.

Because real distributed systems must tolerate partitions, the practical trade-off during a partition is usually between consistency and availability. Research examples of systems that favor each side of this trade-off. Explain how the business requirements of a pipeline influence the choice; avoid treating CAP as a fixed label for a product in every situation.

## 2. Practical Assessment: Design a Data Pipeline

### Scenario

An online retailer receives orders through a transactional database and clickstream events from its website. Operations needs a near-real-time dashboard showing sales and failed payments. Finance needs an accurate daily revenue report. Data volume is growing quickly, events may arrive late or more than once, and the service must continue operating through temporary network failures. Customer data must be governed and retained according to company policy.

Design a high-level pipeline for this scenario. A diagram is recommended. You do not need to select specific products or write code; focus on the concepts, data flow, and design trade-offs.

Your pipeline should cover:

1. **Sources and data types:** Identify the structured, semi-structured, or unstructured data produced by each source and relate it to the five V's.
2. **Ingestion:** Decide where CDC, batch processing, or stream processing should be used. Explain how duplicate, missing, and late events are handled.
3. **Storage:** Decide whether the operational and analytical workloads need SQL or NoSQL storage, a data lake, a data warehouse, or a combination. Explain serialization, compression, and the store-first approach where relevant.
4. **Processing:** Choose ETL or ELT for each important flow and describe the transformations and data-quality checks.
5. **Serving and analytics:** Explain how the operational dashboard and daily finance report use the processed data and why their OLTP or OLAP needs differ.
6. **Scale and resilience:** Explain scale-up vs. scale-out, high availability, distributed storage, and leader-follower vs. leaderless design choices.
7. **CAP trade-off:** Describe a realistic network partition. State whether the dashboard, order processing, and finance report should favor consistency or availability during the partition, and justify each decision.
8. **Governance:** Identify the data owner and describe cataloging, lineage, access, quality, and lifecycle or retention requirements.

### Practical Summary Conversation

Walk your mentor through the pipeline as if you were proposing it to an engineering team. The mentor should challenge the design with questions such as:

- What happens from the moment an order or click event is created until it appears in a report?
- Which paths are streaming and which are batch, and why?
- Where is raw data retained, and how could the pipeline recover or replay it?
- How do you prevent duplicate or late events from producing incorrect results?
- Which component owns the source of truth for orders?
- What fails during a network partition, and what remains available?
- Where are data quality, lineage, ownership, and retention enforced?
- How would the design change if volume increased tenfold?
- Which decision involves the most important trade-off, and what alternative did you reject?

Revise the pipeline after the conversation and record the decisions or assumptions that changed.

## 3. Chapter Completion Checklist

Before marking the chapter complete, confirm that you can answer **yes** to each item:

- [ ] I can define every core concept in my own words and give a real-world example.
- [ ] I can compare the main alternatives, including ETL/ELT, SQL/NoSQL, OLTP/OLAP, batch/stream, warehouse/lake, and scale-up/scale-out.
- [ ] I can explain the CAP Theorem without claiming that a distributed system can simply choose all three guarantees during a partition.
- [ ] I created an end-to-end pipeline showing sources, ingestion, storage, processing, serving, and consumers.
- [ ] I explained how data moves through the pipeline and how the concepts in this chapter fit together.
- [ ] I addressed duplicates, late data, failures, recovery, scaling, and high availability.
- [ ] I justified consistency and availability choices for different workloads during a partition.
- [ ] I identified data ownership, quality checks, cataloging, lineage, access, and retention requirements.
- [ ] I can explain the most important trade-offs and alternatives in my design.
- [ ] I reviewed the pipeline with my mentor and updated it based on feedback.
- [ ] I recorded remaining questions and topics that require deeper study.

## 4. Mentor-Led Oral Summary

The **Apache Data Stack is not part of the self-study learning material or written assessment in this chapter**. Keep it as a short mentor-led summary during the oral exam. The mentor may use familiar Apache projects only to illustrate how the chapter's concepts can map to categories such as ingestion, storage, processing, orchestration, governance, and analytics.

The trainee is not expected to memorize an Apache technology list. The goal is to explain the role of each category, trace data through a platform, and connect technologies back to the concepts and trade-offs covered in the chapter.

Finish with an open Q&A session to clarify remaining questions and identify topics to revisit later in the onboarding program.
