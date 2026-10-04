# Hadoop Distributed File System (HDFS) :elephant:

## Overview
This session focuses on the core concepts of HDFS, the distributed storage layer of the Hadoop ecosystem. Understanding its architecture will help you appreciate how big data clusters store and manage massive datasets across many machines.

**Study the key components, design decisions, and how they work together to provide fault-tolerant, scalable storage.**

## Goals
- Learn the architecture and roles of HDFS components (NameNode, DataNode, etc.).
- Understand how HDFS handles storage, replication, and availability.
- Understand the disadvantages of HDFS, including potential bottlenecks, performance issues, and other possible challenges.
- Practice planning a self-study day and managing your time.

:warning: **Note:**
- This is a self-study day; independence and time management matter.
- Focus on grasping the full picture of each concept; if you can’t explain it, you haven’t learned it.
- When in doubt, consult your mentor about what to study.

### ⏳ Timeline
Estimated Duration: 3 Days
- Day 1-3: Learn the concepts of HDFS: purpose, historical context, architecture, fault tolerance and the client protocol: how reads and writes are performed.
    - Have a Q&A session on the third day and in between sessions every day

## Core Concepts

Consider the following five questions to cover the major HDFS topics:

1. **Architecture & Roles:**  Describe HDFS’s overall architecture, including NameNode(s), DataNodes, blocks, and how the namespace and metadata are managed. Explain how DataNodes send block reports, and why these mechanisms matter for everyday operations.
   
Blocks: קובץ HDFS מחולק למקטעים של 128 מגהבייט, הנקראים "בלוקים" (blocks), וככל הניתן, כל מקטע מאוחסן ב-DataNode שונה.
DataNodes: מאחסנים את המידע עצמו ב-HDFS בצורת blockים, העבדים.
NameNode: מאחסן metadata כגון מספר הblock, ובאיזה rack ואיזה DataNode(-ים) מאוחסן המידע עצמו, הmaster.
How namespaces are managed: NameNode מנהל את מרחב השמות של מערכת הקבצים. כל שינוי במרחב השמות או במאפייניו נרשם על ידי NameNode.
What are block reports: דוח שהDataNodes בcluster של Hadoop שולחים לNameNode, המכיל metadata על blocks הנשמרים באותו node.
מרווח הזמן של block reports נקבע על ידי ההגדרה dfs.blockreport.intervalMsec; כברירת מחדל - 6 שעות.
    משתמש בBlock reports למטרות הבאות
עיבוד block reportראשוני: עבור דוח ראשון מ-DataNodes שנרשמו זה עתה, המערכת מוסיפה את כל הreplicas התקינים.
עדכון מידע על blockים: המיפוי המקשר בין DataNode לבין הBlockים שלו מתעדכן ב-NameNode.  
    הblock report החדש מושווה לדוח הקודם, והמידע מתעדכן בהתאם.
DataNode Protocol over TCP/IP
   
2. **Storage & Fault Tolerance:**  Explain how HDFS divides files into blocks, uses replication (default factor three), and how it detects and recovers from node failures.
   
משתמש בשכפול (default factor 3),  
לקוח כותב נתונים לקובץ HDFS עם replication factor של 3, הNameNode שולף רשימה של DataNodes, רשימה זו מכילה את הDataNodes שיארחו עותק של אותו block.
לאחר מכן, הלקוח כותב לDataNode הראשון:
הDataNode הראשון מתחיל לקבל את הנתונים בחלקים, כותב כל חלק למאגר המקומי שלו ומעביר את אותו חלק לDataNode השני ברשימה.
הDataNode השני, מתחיל לקבל כל חלק של block, כותב אותו למאגר שלו, ואז מעביר אותו לDataNode השלישי.
הDataNode השלישי כותב את הנתונים למאגר המקומי שלו.
כך, DataNode יכול לקבל נתונים מהDataNode הקודם בpipeline ובו-זמנית להעביר נתונים לDataNode הבא בpipeline.
באופן זה, הנתונים מועברים בשיטת pipelining מDataNode אחד לשני.

כשל ב-NameNode:
במערכות Hadoop מודרניות, קיימים שני NameNodeים: active וstandby.
הstandby NameNode מבצע checkpoint תקופתית של מרחב השמות namespace של הactive NameNode.
הNameNodes חייבים להיות מסונכרנים זה עם זה בכל עת ולהחזיק באותם metadata.
זיהוי כשל בNameNode מתרחש כאשר הDataNode אינו מקבל תגובה לheartbeat שהוא שולח מדי 3 שניות (פרמטר הניתן להגדרה).
במקרה שבו ה-NameNode הפעיל קורס או מפסיק לפעול, ה-NameNode הסביל ייקח על עצמו את האחריות למתן שירות ללקוחות, ללא כל הפרעה.

כשל ב-DataNode:
DataNode שולח באופן רציף heartbeat לNameNode, מדי 3 שניות.
אם הNameNode אינו מקבל אות "heartbeat" מDataNode הactive במשך 10 דקות (כברירת מחדל), הוא יחשיב את אותו node כמת.
בשלב הזה, הNameNode יבדוק אילו נתונים היו באותו צומת כושל ויזום תהליך של replication.
3. **Block Placement & Performance:** How does HDFS replicate across nodes? Discuss how block placement, snapshots, and checksums contribute to performance and data integrity.
מדיניות המיקום של HDFS קובעת שיש למקם עותק אחד במכונה המקומית אם הכותב נמצא על DataNode, או בDataNode אקראי באותו rack שבו נמצא הלקוח, אם אינו נמצא על DataNode.  
עותק נוסף בDataNode הנמצא בrack מרוחק, ואת העותק האחרון בDataNode אחר באותו rack.

Snapshots בHDFS הם עותקים של מערכת הקבצים - במצב Read only - המשקפים את מצבה בנקודת זמן מסוימת.
ניתן ליצור snapshots עבור subtree של הfs או עבור המערכת כולה.  
שימושים נפוצים בsnapshots כוללים גיבוי נתונים והתאוששות מערכת.
כאשר לקוח יוצר קובץ ב-HDFS, הוא checksum עבור כל block בקובץ ומאחסן סכומים אלו בקובץ נסתר נפרד, באותו namespace של HDFS.
בעת שליפת תוכן הקובץ, הלקוח מוודא שהנתונים שהתקבלו מכל DataNode תואמים לchecksum המאוחסן, אם אין התאמה, הלקוח יכול לבחור לשלוף את הblock מDataNode אחר המחזיק בreplica של אותו block.
   
4. **High Availability:**  Outline HDFS High Availability (Active/Standby NameNode, JournalNodes). How do these features improve scalability and uptime? Don’t forget the role of ZooKeeper in coordinating HA and keeping track of leases. 

Active/Standby NameNode: ראה שאלה 2 - "כשל ב-NameNode"  
כדי שהStandby NameNode ישמור על סנכרון, שני הNameNodeים מתקשרים עם קבוצה של daemons הנקראים JournalNodes (או JNs).
כאשר הActive NameNode מבצע שינוי כלשהו בnamespace, הוא מתעד את השינוי באופן durably ברוב הJNs הללו.
הStandby NameNode מסוגל לקרוא את הedits מהJNs, והוא עוקב אחריהם באופן רציף כדי לזהות שינויים, עם קבלת השינויים, הStandby NameNode מחיל אותם על הNamespace המקומי שלו.
במקרה של failover, הStandby NameNode יוודא שקרא את כל השינויים מהJN לפני שיעבור למצב פעיל.

התכונות האלו מאפשרים לנו סקלביליות ואת הuptime של המערכת באמצעות זה ש:
1. אנחנו מוודאים שאין לנו single point of failure בכך שיש Standby Nodes
2. אנחנו יכולים לגרום לסנכרון בין כמה Active NameNodes
מה שמאפשר לנו גם סקלביליות וגם באותו הזמן משפר את הuptime של המערכת בכך שהיא שרידה לתקלות בNameNodes ולא רק בDataNodes [איפה שיש שכפול מידע].
בנוסף, יש לנו את ניהול הsessions בZooKeeper - כאשר הNameNode המקומי תקין, מחזיק גם znode מיוחד המשמש כ"נעילה".
   
5. **Client Protocol:**  Describe how clients read and write data to HDFS, how they locate NameNodes and DataNodes. Explain the read and write flow in detail: how the client initiates a connection to the cluster, which components it talks to and how ports of communication become known to the client. Explain the protocol alternatives available to the client:
    - What is native API?
    - What is HDFS CLI and what protocol does it utilize?
    - Can you talk to HDFS using REST/HTTP?

    What does a client need to connect to an HDFS cluster using each of the alternatives?
    
    What are the two main types of HDFS operations, and how do they differ in terms of the components they interact with?

Read:
1. הלקוח מבקש לקרוא את הקובץ מהNameNode
2. הNameNode שולח לו מאיזה DataNodeים הוא יכול לקרוא כל block ובאיזה סדר לקרוא.
3. הלקוח קורא את הblock מהDataNode הכי קרוב אליו, או לפי סדר הבלוקים או במקביל*.
Write:
4. הלקוח מבקש מהNameNode ליצור קובץ
5. הNameNode נותן מיקום של DataNode שאפשר ליצור בו את הקובץ
6. הלקוח כותב את הכותב לDataNode, שמפצל את הקובץ לblockים*.
7. הDataNode כותב את אותם blockים ל2 DataNodeים אחרים [הוא כותב לאחד והאחד כותב לאחד נוסף]
8. לאחר סיום כתיבת הקובץ לDataNode הראשון, הוא מחזיר ללקוח שנגמרה הכתיבה
9. הלקוח שולח לNameNode שנגמרת יצירת הקובץ
10. הNameNode מתעדכן מהDataNodes על הmetadata של הקובץ החדש.
-* חשוב לציין כי נעשת בדיקת checksum לולידיות הblock.
Port 50010 פתוח ב-DataNodes וPort 50070 פתוח ב-NameNodes.
הלקוח יוצר חיבור ליציאת TCP במכונת NameNode [פורט configurable].
הוא מתקשר עם הNameNode באמצעות הClientProtocol.
הDataNodes מתקשרים עם הNameNode עם הDataNode protocol.
Abstraction מסוג Remote Procedure Call - RPC, עוטפת את הClientProtocol ואת הDataNode Protocol,חשוב לציין כי NameNode לעולם אינו יוזם קריאות RPC, אלא הוא רק מגיב לבקשות RPC מצד DataNodes או לקוח.
WebHDFS הוא API RESTful של HDFS המבוסס על HTTP.  
HDFSCLI - אינטרפייס CLI לWebHDFS וhttpFS.
אפשר להשתמש בWebHDFS שהוא RESTful.

WebHDFS - Host IP
httpFS - WebHDFS [???]

Read וWrite
בRead נתקשר עם יותר מDataNode אחד לעומת בWrite ש[כנראה] נכתוב רק לDataNode אחד ישירות את הקובץ שלנו והוא יטפל בReplication.
### 🔄 Alternatives
Assignment: You are required to research and write a comparative analysis between HDFS and an industry alternative.
- Deliverable: A written summary (minimum 1 or 2 sentences).
- Focus: Compare performance, architecture, and specific "pain points" this tool solves compared to legacy systems or competitors.
- Goal: You must be able to justify why the department uses this tool for our specific environment.

### 🎯 User Story & Scenario
Assignment: Based on your research and understanding of the department's pipeline, define a concrete Use Case for this technology.
- Deliverable: A written summary example/story (two paragraphs approx.).
- Requirement: Describe a real-world scenario (e.g., a specific client requirement) where this technology is the optimal solution.
- Data Flow: Map out the data flow and explain how this tool integrates with other components in the Data Pipeline.


## Wrapping Up :trophy:
Review your answers with your mentor and discuss any unclear points. Relate these concepts back to real-world usage scenarios you might encounter.

## Action Items
- Note topics you want to investigate further.
- Prepare questions for the mentor Q&A session.
- Continue the Day 01 challenge by linking these HDFS concepts to other chapters.

## Recommended Resources
- [Official HDFS User Guide](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsUserGuide.html)
- [Hadoop: The Definitive Guide (O'Reilly)](https://piazza-resources.s3.amazonaws.com/ist3pwd6k8p5t/iu5gqbsh8re6mj/OReilly.Hadoop.The.Definitive.Guide.4th.Edition.2015.pdf)
