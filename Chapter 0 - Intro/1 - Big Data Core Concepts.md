# Introduction to Core Data Concepts :baby:

## **Goals**
- Understand the data landscape and its core concepts.
- Explore the importance of data operations and the role of data in guiding business decisions.
- Gain a comprehensive overview of the data lifecycle and its implications for the organization.

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
24. **Apache data stack**

These topics are meant to guide your research. Don’t hesitate to look up other relevant concepts.
</br>
> Note✅: Reinforce your understanding by relating the concepts to real‑world scenarios.

## Answers

1. **The five V's of Big Data**\
The five V's of big data is 5 characteristics which help us define the big data concept and how to manage it.
- Velocity - the speed of how data is creating and moving.
- Volume - Refers to the enormous amount of data that exists and keeps growing.
- Value - the benefits that big data can provide. Having a bulk of data is nothing, unless you turn it into something useful, with value. 
- Variety - variety of data types and structures. the challenge in variety concerns the standardization of all data being collected.
- Veracity - refers to the quality, reliability and accuracy of the data. The level of trust there is in the collected data.

2. **Structured, unstructured, and semi‑structured data**\
- Structured Data - Based on relational database table with rows and columns. Structured schema which is less flexible for changes and all the rows must follow it. (sql, csv)
- Unstructured Data - Data without a predefine data model. It is more flexible and there is absence of schema or a constant format. (images, videos, word)
- Semi-structured Data - Sits between structured and unstructured data. It has a fixed format but doesn't have a fixed schema. This gives it greater flexibility compared to structured data while retaining more organization and validations than unstractured data.(json, xml)

3. **ETL vs. ELT**\
Two approaches which commonly used to move data.
- ETL (extract, transform, load) - extract raw data, immediately transformed as required, then load it into the data warehouse where the users can access it.
- ELT (extract load transform) - extract raw data, load it into the data warehouse, then performs data transformations directly within the data warehouse itself. Unlike ETL, where data is transformed before loading, and raw data may not be retain. In addition its, eliminating the need for staging processes.

4. **NoSQL vs. SQL databases**\
- SQL databases are relational and stands for structured query language. NoSQL databases are non-relational and stands for not only SQL.
- SQL databases are table-based, while NoSQL databases are document, key-value, graph, or wide-column stores.
- SQL databases use structured query language and have a predefined schema. NoSQL databases have dynamic schemas for unstructured data.
- NoSQL databases are scalable horizontally, meaning you can scale out by adding nodes. SQL databases in most situations are vertically, meaning you can scale up by adding more resources.


## Wrapping Up


### Reflection
Take a few minutes to reflect on what you have learned:
- Write down key takeaways and examples
- Note any questions or uncertainties
- Discuss real-world use cases with your mentor

### Mentor Discussion
Talk through the following with your mentor:
- Clarify concepts that remain unclear
- Share your findings and insights
- Discuss real‑world use cases and implications for your work

## Q&A Session :raising_hand:
Participate in an open Q&A session with your mentor to address any questions about specific tools, technologies, or practices.

## Action Items
- Identify areas you want to explore more deeply.
- Ask for recommended resources for further learning.
