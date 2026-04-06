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

2. **Structured, unstructured, and semi‑structured data**
- Structured Data - Based on relational database table with rows and columns. Structured schema which is less flexible for changes and all the rows must follow it. (sql, csv)
- Unstructured Data - Data without a predefine data model. It is more flexible and there is absence of schema or a constant format. (images, videos, word)
- Semi-structured Data - Sits between structured and unstructured data. It has a fixed format but doesn't have a fixed schema. This gives it greater flexibility compared to structured data while retaining more organization and validations than unstractured data.(json, xml)

3. **ETL vs. ELT**\
Two approaches which commonly used to move data.
- ETL (extract, transform, load) - extract raw data, immediately transformed as required, then load it into the data warehouse where the users can access it.
- ELT (extract load transform) - extract raw data, load it into the data warehouse, then performs data transformations directly within the data warehouse itself. Unlike ETL, where data is transformed before loading, and raw data may not be retain. In addition its eliminating the need for staging processes.

4. **NoSQL vs. SQL databases**
- SQL databases are relational and stands for structured query language. NoSQL databases are non-relational and stands for not only SQL.
- SQL databases are table-based, while NoSQL databases are document, key-value, graph, or wide-column stores.
- SQL databases use structured query language and have a predefined schema. NoSQL databases have dynamic schemas for unstructured data.
- NoSQL databases are scalable horizontally, meaning you can scale out by adding nodes. SQL databases in most situations are vertically, meaning you can scale up by adding more resources.

5. **OLAP vs. OLTP**\
Two primary data processing systems or accsess patterns.
- OLTP (online transactional processing) - access pattern which optimized to day-to-day transactions methods with low latency. Supports ACID properties. Focuses on smooth interations and many seamless transactions for the users experience.\
read - mostly with indices\
write - one or several rows.
- OLAP (Online analytical processing) - access pattern which optimized to querying data for wide analysis, statistics, conclusions, and desicion making processes with high latency.\
update - will be very expensive operation.\
Focuses on small amount of read operations happening concurrently.

6. **Batch processing vs. stream processing**\
Two methods used for processing large volumes of data.
- Batch processing - refers to processing data in blocks (batches) at scheduled intervals or after accumulating a certain amount of data. Data is collected over a period and processed all at once with high throughput where immediate action is not necessary. Resource efficient.
- Stream Processing - continuously processing data in real-time as it arrives. Used when immediate action is required based on the incoming data. Resource intensive.

7. **Data warehouse vs. data lake**
- Data warehouse - stores structured or semi structured data which already processed, optimized to query and analyze effciently. Schema on write, high performance for complex queries with indexing and partitioning strategies. data integration, combined from multiple sources to a cohensive dataset for analysis.
- Data lake - designed to store vast amount of raw data in its native format. This approach allows to load data from different sources without the need for immediate transformation. Store data as-is, apply schema on read, designed to handle large volumes of data in expensively. Store first.

8. **Distributed file systems**\
DFS is a networked architecture that allows manage files accross various machines. Instead of storing data on a single sever, DFS spreads files across multiple locations.DFS provides data redundancy (replicates data across multiple servers), scalability, consistency (ensures to syncronize data across the replicas), data partitioning (splitting files to smaller pieces for efficient storage) and load balancing.

9. **Data governance**\
Data governance is a subset of data management that focuses on controlling data assets for having quality, security, efficiency and availibility of the data. helps ensure data integrity and data security by defining policies and access (RBAC) and monitoring. 

10. **Data visualization**\
Data visualization is the representation of data through the use of graphics, charts, plots.It can help you communicate ideas quickly and draw new insights from data. Data visualization tools fot example are grafana or kibana.

11. **Data analytics**\
Data analytics is the process of collecting, transforming, and organizing data in order to draw conclusions, make predictions, and drive informed decision-making.

12. **Data ownership**\
Data Ownership refers to the responsibility associated with managing, controlling, and ensuring the security of data within an organization. Defines the legal rights and control over the data.

13. **Data quality**\
Like a restaurant who wants to serve food with high quality ingredients, a data management team want to provide data with high quality.\
Data quality measures how well a dataset meets criteria for accuracy (current vs reality), completeness (no missing values), validity, consistency (uniformed data from different sources), uniqueness (duplications), and it is critical to all data governance initiatives. 

14. **CDC (Change Data Capture)**\
Change Data Capture (CDC) is a technique used to detect and record changes such as inserts, updates, and deletes in a database. CDC improves data efficiency by capturing only changed records. CDC looks for shifts in a database, and when it finds one, it records it. This record is later stored either in the same database or in external applications. In practice, CDC is often used to replicate data between databases in real-time. CDC instantly and automatically syncs databases as soon as the source data changes. (concept in many databases, mongo, cassandra postgress)

15. **Data catalog**\
A centralized inventory that stores metadata related to the data assets which can be datasets, tables, databases and files. It provides data discovery and search functionalities based on keywords, tags, filters and more. Data lineage, data governance support and collaboration features. Data catalog collects and indexes the metadata from a variety sources.

16. **Data lifecycle management**\
A data as a lifecycle, with several phases:\
collection, storage, share, use, archive, deletion.\
With DLM you achive availability, integrity and security. 

17. **Data lineage**\
Data lineage is the process of recording, tracking and visualizing data over time. Uncovers the life cycle of data, it aims to show the complete data flow, from start to finish. Validate data accuracy and consistency to ensure data quality and discover anomalies. Data lineage techniques can be by tagging by pattern and more.

18. **Store‑first approach**\
The approach of "throwing" the raw data to a storage service (for example s3), without any transformations (ELT). It provides a single source of truth for the raw data which can re-extracted / reprocess in case of pipline failure or data corruption. In addition it enables immediate access to the data.

19. **Data serialization**\
Data serialization is the concept od converting data objects into a fitted and valid format as the requirments of the database / api. The reverse process is called desserialization.

20. **Data compression**\
The idea of reducing the size of the data and stores it in a compact form. It also increases the speed of algorithms and transmissions methods. Compression is achieved by removing redundancy, that is repetition of unnecessary data with multiple techniques.

21. **Scale‑out vs. scale‑up**\
Both are approaches of handling data volume and growth in the amount of data / utilization. scale up represents vertical growth by adding resources to the existing node (cpu, ram, storage). In contrast to scale out which represents a horizontal increasing of components like nodes or workloads.

22. **High availability**\
One of the three properties that are crucial in distributed data systems according to the CAP theorem. Means the system always responds to requests, even if it's not the latest data.

23. **Master‑slave vs. masterless architectures**
- Master-slave architecture has a master node that guides and coordinates the activities of several slave nodes. The master gets the commands from the user and the slaves executes them. It has to main problems:\
Consistency - It has to have a data copying stratgy to ensure that the slave servers are up-to-date, can cause problems of replication lags. Optional solution is  write through cache and use an asynchronous replication methods with alerting systems.\
master fails - In case a master fails it depends of the architecture. Optinal solutions is a replication manager which automatically switch a slave node to be the master. (hadoop).
- Masterless architecture - every node in the database can provide the exact same fuctionality as any other node. These nodes communicate with one another through a protocol called gossip, which is a process of computer peer-to-peer communication. (cassandra)

24. **Apache data stack**\
The Apache Software Foundation (ASF) manages over 350 open-source projects under the apache license, ensuring they remain free, scalable, and enterprise ready. Known for its community driven, collaborative approach.
Some tools from the Apache data stack: Hadoop, Hbase, Hive, Zookeeper, kafka, impala, airflow, iceberg.

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

## Q&A Answers

1. Stream processing usecases:
- Fraud Detection - process of identifying fraudulent activities or attempts. Stream processing allows financial institutions to monitor transactions in real time. This helps identify and flag suspicious activities immediately, which helps in preventing fraud effectively. Pros of real time insights, but increase complexity.
- Network Monitoring - Network monitoring tools use stream processing to analyze network traffic and performance, ensuring optimal operation and identifying potential issues. By providing real-time insights into network performance, stream processing allows for more efficient troubleshooting and quicker resolution of network issues. Pros of event-driven operations, but limited historical context.
- Healthcare Monitoring Systems - use stream processing to analyze patient data in real-time, By providing real-time alerts and notifications, stream processing can increase patient safety, improve patient outcomes, and reduce costs.\

2. Batch processing usecases:
- End of day processing - Financial institutions rely on batch processing to compile and process transactions accumulated throughout the day. This enables the generation of comprehensive reports used for compliance, auditing, and performance analysis.
Cons of delayed outcomes, but very cost effective resource usage once in a day.
- Payroll processing - Organizations handle payroll in batches by collecting employee hours, calculating compensation, and issuing payments in one streamlined process. Streamlined workflows.
- Data warehousing - Organizations use batch processing to update data warehouses periodically. Large volumes of data are collected and processed in batches, ensuring that the data warehouse is up-to-date with the latest information for analytical purposes.

3. Data warehousing is the process of collecting, integrating, storing and managing data from multiple sources in a central repository. It enables organizations to organize large volumes of current and historical data for efficient querying, analysis and reporting. Data warehouse technologies: azure microsoft, snowflake, postgresql.

4. A data lakehouse is a modern data architecture that combines the scalability of a data lake with the structure and performance of a data warehouse. It allows organizations to store raw and structured data in one system while enabling fast analytics, governance, and machine learning on large datasets.\
At its core, the data lakehouse is not a single product but an architectural pattern. It blends the scalability and openness of data lakes with the transactional reliability and governance of data warehouses. You can combine iceberg with trino to achieve  data lakehouse same as spark with snowflake but there is no one technology which can provide the full capabilities of data lakehouse.

5. Linux File Hierarchy structure is the name that defines the directory structure and directory contents in linux and the data.\
Inode - index node is the data structure which stores metadata on file or directory (permissions, timestamps, file size and types, access control settings, etc).

6. Additional File Systems:
- NTFS stands for New Technology File System, the default file system for modern Windows versions.
- FAT32 is the 32-bit version of the file allocation table (FAT) file system. A file system specifies the protocol for storing and organizing data on a hard drive with file names and certain permissions. Before the advent of the new technology file system (NTFS). FAT32 is still a necessary file system for USB drives and computers with operating systems not compatible with exFAT or NTFS.

7. The information about file permissions exists in the inode.

## Action Items
- Identify areas you want to explore more deeply.
- Ask for recommended resources for further learning.
