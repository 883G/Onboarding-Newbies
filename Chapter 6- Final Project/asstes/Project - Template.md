
## 1. Project Overview
**Project Name:Stocks Analysis and forecast**  
**Date:20/04/2026**  

**Scenario / Story:**  
For anyone who is interested or involved in investing, and especially for
beginners that want to get into investing, stocks can get very complicated.
Understanding when to invest and where can be confusing for someone who never
studied it.
There are so many stocks and so many trends, in today's society a stock can get 
hyped up and forgotten the next week.
That's why there's a need of a service that does the job for you, one system that
lets you see all major stocks updated to the current time at one place (spark), 
lets you query them by top 10/50/etc , or by a type of stock (trino)
gives you reports on a regular basis , and alerts you when an unusual event happened
like a drastic rise or fall of a stock (airflow)
when all stocks and their data are stored in s3 or hdfs.


**Core Requirements:**  
The goals of the pipeline are:
- Stream large amount of stocks data (kafka) and save it on storage (s3/hdfs). 
- Provide updated data to the client. 
- Ad-hoc : alert when an unusual event has happened.
- Provide reports every determined amount of time (spark).
- Consider a forecast of the stocks for the future.
  

---

## 2. Data Characteristics
- **Data Types:** 
Using Finnhub API, stocks are returned as JSON encoded responses.
We'll store them as encoded JSON files, with an option to compact them to larger
parquet files.

- **Data Volume:**
One response from the Finnhub API will include a message type, last stock's 
price, it's symbol, volume and timestamp in JSON format.
that is pretty small, a request like the one below from the Finnhub API is only
about 88B.
{
  "data": [
    {
      "p": 7296.89,
      "s": "BINANCE:BTCUSDT",
      "t": 1575526691134,
      "v": 0.011467
    }
  ],
  "type": "trade"
}
If we take that as an average response, and there are about 8400-16000 us and canadian
stocks, were talking about 1.5GB a second, which is approx 5TB an hour.

- **Arrival Frequency:**   
We will need streaming as stocks update every second of the day.
Once a day (00:00) we will generate a report of the day before (batch).
Once a month (31/30.x.xxxx) we will generate a report of the previous month.
Once a year (1.1.xxxx,00:00) we will generate a report of the previous year.

- **Latency Requirements:**  
Latency is a very important subject that we have to deal with, when we talk about 
streaming that is done non-stop with this type of data, we need to have as minimal
latency as possible. Both on the client side and the server side since it has direct
affect on the client side (a latency in processing will cause a delay on the client
side.)
The batch processing (reports) can "suffer" higher latency since it will have less
of an impact, its not a real-time output but a scheduled once-a-day one.

---

## 3. Pipeline Architecture
**End-to-End Diagram:**  
> Include diagram showing data flow.  

**Components & Responsibilities:**

- **Ingestion:
    With flink we do stream processing, and get the stocks data in real time with
    Finnhub API.**

- **Storage (S3/HDFS):
    We will use s3 as storage, since our files are considered small, and compaction
    is needed frequently, s3 is a better choice handling compactions and small files 
    better than hdfs. 
    Also, s3 use of tiers can help us with faster access for frequently accessed files.**

- **Processing (Spark):
    With spark we will do batch processing to create reports one a day of the stocks
    market status, that includes top stocks, biggest rises/falls etc...**

- **Orchestration (Airflow):
    With airflow we'll orchestrate the reports.** 

- **Query Layer (Trino + SQL):
    We'll use trino to query the current stocks by top stocks, biggest rise, certain
    types of stocks, etc...**  


---

## 4. Storage Design

- **Partitioning Strategy:**


- **File Formats:** (Parquet/ORC/etc.)  
Files that were processed by flink in the stream processing will be stored as JSON 
files since that is the response format the Finnhub API returns them as.
After compaction, they will be in parquet format.
The compaction would happen after files are stored, that way there isn't such high 
latency (which we don't want), but after displaying the data at the current moment
we don't need it in real time anymore so the compaction process won't hurt us.


- **Lifecycle Policies / Retention:**
A file will include the stocks name, the stocks details like open/close/low/high
and volume.
Since we are using s3 the version will be saved with the stock which will allow us
to know the timestamp of the stock.
Since we talk about stocks an expiration of 5 years should be enough, that way the 
client can see the stats of the stock from a satisfied amount of time before, but
we don't overload the storage with data from 30 years back.

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
