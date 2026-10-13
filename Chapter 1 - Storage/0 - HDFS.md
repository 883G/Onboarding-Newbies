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
A:
ארכיטקטורת master slave. יש לנו שני אובייקטים, לפעמים יותר, שהם name nodes. תמיד אחד מהname nodes הוא אקטיבי והשאר פסיבים. הnamenode שהוא אקטיבי אחראי על כל פעולות הלקוח והפסיבי רק מסתנכרן איתו כדי שיוכל להחליף אותו במהירות למקרה שהאקטיבי יפול. בעת פעולת לקוח, הnamenode האקטיבי מוודא שכל המידע שצריך לפעולה הזו טעון ומחולק לבלוקים בתוך slave nodes בשם data nodes. הdata nodes עושים פעולות קריאה וכתיבה ושכפול בהתאם למה שהnamenode אומר להם. הסנכרון בין הnamenodes מתבצע בעזרת edit log משותף. הnamenode הפסבי קורא את הedit log ומסתנכרן לפיו. datanodes צריכים לשלוח block reports לכל הnamenodes, גם האלו הפסיביים, בגלל שהמיפוי של הבלוקים נשמר בזיכרון של namenode ולא בתוך הדיסק. תפקיד נוסף של הפסיביים זה לקחת namespace images, שזה תמונות מצב של כל הfile system namespace ולשמור אותם. המכניזם הזה הוא משמעותי בשביל שמצד אחד המידע יהיה שמור במקרה של קריסת namenode, ומצד שני יהיה סינכרון מספיק טוב בין הnamenodes כך שיהיה לנו high availability וההחלפה תתבצע בצורה מהירה. 

2. **Storage & Fault Tolerance:**  Explain how HDFS divides files into blocks, uses replication (default factor three), and how it detects and recovers from node failures.
A:
בHDFS כמו מערכות קבצים אחרות יש קונספט של בלוקים. במקרה של HDFS, גודל בלוק הוא לרוב 128 MB. ככה שאם יש לי קובץ גדול יותר, הוא יחולק לחלקים בגודל בלוקים שישמרו באופן בלתי תלוי. מה שכן, כן יש פה שכבת אבסטרקציה ככה שאם יש לי קובץ שהוא מתחת לגודל של בלוק, הוא לא בהכרח יתפוס בלוק שלם. כדי לוודא שרידות של הבלוק, כל בלוק משוכפל למספר כלשהו של רכיבים פיזיים שונים, לרוב 3 בסך הכל. ככה גם אם המידע נהיה אבוד או שהרכיב נפגע, עדיין יש לי דרך אלטרנטיבית להשיג את הבלוק הרצוי. גם ניתן להשתמש בrecovery mode, מתחילים את הnamenode בrecovery mode וזה מציע לך אפשרויות שניתן לעשות שאולי בעזרתן ניתן להשיג בחזרה את המידע. זה שיש לנו שני namenodes, אחד אקטיבי ואחד פסיבי מחכה להחליף אותו, במקרה שהאקטיבי נופל אז המעבר הוא חלק ומתבצע בצורה נכונה כי הnamenodes מסונכרנים ביניהם. הnamenode כל הזמן מקבל heartbeats מdatanodes קצת כמו בzookeeper. אם הוא לא קיבל למשך זמן מה (נגיד 10 דקות דיפולטית) אז הוא מכריז עליו כמת ויוצר לו שכפול כך שעדיין יהיו מספר עותקים. 
3. **Block Placement & Performance:**  How does HDFS replicate across nodes? Discuss how block placement, snapshots, and checksums contribute to performance and data integrity.
A:
יש replication ככה שיש את המידע בכמה nodes שונים, דיפולטית 3. יש את הservice בשם הjob tracker, שמזהה אם יש שגיאה באחד משרתי הdat nodes, אז הjob tracker יעביר את העבודה של הבלוק הזה לdata server אחר. כפי שאמרנו, הnamenode יצור גם עותק חדש. בhdfs מתאפשר לנו לעשות snapshotים שזה עותק read-only שמותאם לנקודת זמן ספציפית של הקבצים במערכת הקבצים. ניתן לקחת את זה על תיקייה ספציפית או על כל מערכת הקבצים. הsnapshot מכיל פוינטרים לבלוקים עצמם. במקרה שיש כתיבה, רק אז יש העתקה של הבלוק, כדי לחסוך שכפול מידע כשלא צריך. הפוינטר עדיין מצביע לבלוק המקורי. checksum הוא ערך דטרמיניסטי שניתן לחשב על מידע. הדטרמיניסטיות חשובה, כי משתמשים בו כדי לוודא תקינות של מידע. אם המידע לא השתנה הchecksum אמור להשאר זהה ואם הוא משתנה הchecksum אמור להשתנות, כלומר הוא צריך להיות גם מספיק חח"ע. ככה כשנרצה להכניס מידע תקין, נשווה את הchecksum של המידע לפני ואחרי וכך נדע אם המידע נפגע או לא בזמן ההכנסה. אותו חישוב checksum נעשה גם בקריאה ולא רק בכתיבה. כל הדברים האלו יחדיו עוזרים לנו לשמוור על שלמות מידע תקין שנוכל לגשת אליו גם אם חלק מהמכשירים קורסים. checksum זו דרך מעולה לבדוק תקינות מידע בצורה יעילה, כי לעבור על המידע ידנית היה מאוד פוגע בביצועים. 



4. **High Availability:**  Outline HDFS High Availability (Active/Standby NameNode, JournalNodes). How do these features improve scalability and uptime? Don’t forget the role of ZooKeeper in coordinating HA and keeping track of leases.
A:
כפי שהסברנו יש שני namenodes, אחד אקטיבי ואחד פסיבי. האקטיבי אחראי על פעולות הלקוח והפסיבי מסונכרן איתו ומחכה להחליף אותו במהירות במקרה הצורך. הם נשארים בסינכרון על ידי מקום אחסון משותף שהם כותבים וקוראים ממנו. מימוש נפוץ, QJM שזה quorum journal manager, רץ כאוסף של journal nodes כך שכל שינוי צריך להכתב לרובם. למה לרובם? ככה שאם עד חצי נופלים, אני יודע שהמידע קיים. בדיפולטית יש 3 journal nodes, כל העניין קצת מזכיר את הגישה בzookeeper. אבל פה אין שימוש בzookeeper, בניגוד לתהליך החלפת הactive namenode, שם כן יש שימוש. כשיש מעבר מnamenode אקטיבי לפסיבי, הוא מנוהל על ידי הfailover controller. המימוש הדיפולטי משתמש בzookeeper כדי לוודא שרק namenode אחד הוא אקטיבי. הוא פותח session עם הnamenode ושולח לו פינגים ביחד עם health check. אם משהו בnamenode האקטיבי נהיה לא תקין, הhealth checks תופסים את זה ואז הzookeeper בוחר namenode אחר שיהיה האקטיבי. הדברים האלו מאפשרים סקלביליות וuptime כי אין פחד שעומס יגרום לקריסה שתפגע בנו מאוד, בזכות המעבר המהיר עדיין נוכל להשתמש במערכת בלי חשש לאיבוד מידע רב. 

5. **Client Protocol:**  Describe how clients read and write data to HDFS, how they locate NameNodes and DataNodes. Explain the read and write flow in detail: how the client initiates a connection to the cluster, which components it talks to and how ports of communication become known to the client. Explain the protocol alternatives available to the client:
    - What is native API?
    - What is HDFS CLI and what protocol does it utilize?
    - Can you talk to HDFS using REST/HTTP?

    What does a client need to connect to an HDFS cluster using each of the alternatives?
    
    What are the two main types of HDFS operations, and how do they differ in terms of the components they interact with?
A:

הלקוח פונה אל הnamenode דרך פורט TCP קונפיגורבילי. התקשורת מתבצעת בזכות ClientProtocol. לעומת זאת, הData Nodes משתמשים בDatanodeprotocol כדי לתקשר עם הnamenode. שניהם בתכל'ס זה RPC. נגיד לקוח רוצה ליצור קובץ בHDFS. הלקוח הHDFSי עושה cache למידע של הקובץ והכתיבה מתבצעת לשם עד שהיא סיימה או שהיא עברה גודל של בלוק אחד. ברגע שזה קרה, הלקוח פונה לnamenode שמכניס את שם הקובץ למערכת הקבצים ומקצה עבורו בלוק. הוא מגיב לבקשת הלקוח עם זהות הdatanode הרלוונטי ומיקום הבלוק. הלקוח מכניס את הבלוק הזה שישב בזיכרון אל תוך הdatanode. ברגע שהקובץ נסגר, כל מידע מהקובץ שעוד לא נכנס מהזיכרון לdatanode נכנס. אחרי זה הnamenode מכניס את הקובץ עצמו אל תוך הדיסק.
כשיש כתיבה לHDF, גם פה הכתיבה בהתחלה נעשית אל תוך קובץ בזיכרון. כשהכתיבה לקובץ מסתיימת או שהיא נהיית לפחות בגודל בלוק, הלקוח מקבל מהnamenode רשימה של datanodes שיהיו אחראים על הבלוק ועל העותקים שלו. הלקוח מעביר את הבלוק לdatanode הראשון שמקבל את הבלוק בחלקים קטנים, כותב אותם אצלו ומעביר אותם לdatanode הבא ברשימה עד הסוף. 
מבחינת הקריאה, הלקוח עושה open על אובייקט הFilesystem שקורא לnamenode כדי להשיג את המיקום של הבלוקים הראשונים של הקובץ. לכל בלוק, הnamenode מחזיר את הכתובת של הdatanodes שמחזיקים עותק של הבלוק. הם ממויינים לפי הקרבה ללקוח. מוחזר ללקוח input stream שהוא יכול לקרוא ממנו מידע. מה שהinput stream עוטף בעצם מתחבר לdatanode הכי קרוב של הבלוק הראשון של המידע ומשם המידע מוזרם ללקוח. כשהבלוק נגמר, החיבור עם הdatanode יסגר ויפתח עם הdatanode הכי קרוב לבלוק הבא. כל זה שקוף ללקוח, שמבחינתו רק קורא ברציפות. בסוף הקריאה הלקוח יקרא לclose על הinput stream. 

מבחינת הבדלים בין הפרוטוקולים השונים, native API הוא מהיר אבל הוא לא נוח עבור אפליקציות שהן לא מבוססות Java. לכן HTTP/REST פותר את הבעיה הזו ומקל על אפליקציות מבוססות שפות אחרות, אבל הוא איטי יותר. 
הHDFS CLI הוא עוד אמצעי שאיתו אפשר לעשות פעולות על מערכת הקבצים בעזרת כתיבת פקודות, ניתן להשתמש בfs כדי לכתוב את הפקודות הרלוונטיות בתוך הfilesystem shell. זה בנוי מעל TCP, הלקוח מתקשר בעזרת פורט TCP. 
שני האופרטורים המרכזיים בHDFS הם כתיבה וקריאה. בכתיבה הכתיבה בסופו של דבר מתבצעת לכמה בלוקים שונים שהם רפליקות כשהמידע עובר שרשור, בקריאה אנחנו קוראים רק מבלוק אחד מכל סוג. 



### Skila Questions

1. What is nameservice?
המונח nameservice מתאר את שני הnamenodes שמגדירים את הnamespace, האחד הראשי והאחד בstandby (בגרסה הרגילה). 

2. Who opens the input stream?

האובייקט DistributedFileSystem מחזיר ללקוח את הinput stream שעושה עליו read.
3. How can you implement parallel reading on data blocks?
אפשר שהתוכנת צד לקוח תבקש מDFSInputStream את הבלוק הבא בthreadים שונים שהיא תרוץ בה וככה תקרא את הבלוקים השונים במקביל.

4. Is the default behaviour allocating a whole block for a file way smaller than block size?

לא, מבחינת המרחב שהוא יתפוס בדיסק, זה יהיה הגודל שלו או קירוב שקטן מגודל הבלוק.
5. What is a journal node?
אוסף של nodes שרצים כך שכל השינויים נכתבים בהם, כל שינוי נכתב ברוב הjournal nodes, הסיבה לרוב היא ככה שאם תהיה נפילה של עד חצי, המידע עדיין ישאר איפשהו. באופן דיפולטי יש 3 journal nodes. 
6. When will a failover scenario give back control to the same namenode?
אפשר לעשות failover ידני לnamenode, סוג של ריסטרט. בזמן שהוא לא פעיל בריסטרט הstandby יחליף אותו, וברגע שהוא עולה הוא חוזר להיות הnamenode האקטיבי.

7. Name of the protocol which datanodes communicate through, what are the pros of it and a little bit implementation.
הפרוטוקול הינו פרוטוקול RPC, פרוטוקול remote procedure call. הnode מבצע סיריאליזציה להודעה לתוך binary stream, שולח אותה לnode המרוחק והnode המרוחק מפענח את ההודעה.
יתרונות זה שאפשר לעבוד עם פורמט קומפקטי כדי לעבוד בצורה טובה עם הנפח של הרשת, בנוסף להעביר מידע שעבר סריאליזציה יכול להתבצע בצורה מהירה. מבחינת מימושים, בסריאליזציה יש כמה גישות שונות שאפשר לעבוד איתן. יש את הפורמט Writables שקומפקטי ומהיר אבל קשה יותר לעבוד איתו מחוץ לJava. לכן גם המציאו את הAvro כדי להתמודד עם קשיים של Writables.

8. What is NativeAPI? What implementations does it have?
יש הנגשה של API לעשות פעולות על hdfs כגון ליצור קובץ, למחוק קבצים, לשנות שם של קובץ, לפתוח לקרוא ולכתוב בקבצים ותיקיות, לשנות הרשאות וכו'. מבחינת המימוש, דוגמה למימוש זה הfilesystem shell. 
9. What are snapshots and why are they good?
כתוב בשאלה 3 המקורית מה זה snapshot. מבחינת למה זה טוב, זה נותן לנו גיבוי בלי downtime ולחזור במהרה לגרסאות קודמות של מידע. 

*OPTIONAL: 10. What are federations?

*OPTIONAL: 11. What are fencing?


### New Questions

1. What is short circuit?

המונח short circuit reads מתאר מצב שבו הלקוח קורא ישירות קובץ, בניגוד לאופן הרגיל שבו התהליך מתבצע דרך הDatanode ששולח ללקוח את המידע. כשזה מתאפשר, זה הרבה יותר מהיר.

2. Fault Tolerance in HDFS 1 vs HDFS 2.
בHDFS 1 יש לנו single point of failure ענקי בזה שאם הnamenode הראשי קורס אז הכל הלך, לעומת זאת בHDFS 2 יש לנו namenode שהוא standby ששם להחליף את הnamenode הראשי שצריך. 

3. What different kinds of clients are there?

יש InsecureClient, TokenClient. הInsecureClient משומש כשלא משתמשים באבטחה, ובTokenClient משתמשים כשהלקוח עובר אימות דרך token במנגנון של hadoop. 

4. What are the different options for journal nodes?
יש את dfs.namenode.shared.edits.dir שקובע את הקישור שמזהה את הjournal nodes שהname nodes יקראו ויכתבו בהם. 
יש את dfs.journalnode.edits.dir ששם העריכות נשמרות ועוד קצת מידע שהjournal node צריך. 

5. What types of block reports exist? What is sent in heartbeat?


יש שני סוגי block reports עיקריים, הblock report הראשוני עבור הdatanode, וכל block report לאחר מכן. יש הבדל באיך הnamenode מתייחס אליהן. בפעם הראשונה יש התייחסות רק לבלוקים תקינים. לאחר מכן יש השוואה עם block reports קודמים ויש ניתוח יותר מעמיק וייחוס לבלוקים לא תקינים מסוגים שונים.
בנוגע לheartbeat, נשלח כמה דברים. מידע על הרישום שלו, כמה אחסון פנוי בdatanode, כמה העברות יש מהdatanode לאחרים ברגע זה, כמה כאלו יש ככלל, גודל הcache המקסימלי של הdata node, כמה כרגע מנוצל. 


6. What is ACL in the context of hdfs?


כמו בלינוקס, יש בhdfs תמיכה בACL. ככה ניתן לעשות הרשאות שלא מתאימות רק לאופן ההיררכי הסטנדרטי, אם יש לנו הרבה משתמשים/שרתים שונים שעושים המון פעולות שונות בקבצים ותיקיות שונות ומפת ההרשאות שאנחנו רוצים כבר מסתבכת, כל איבר ברשימת הACL כולל משתמש או קבוצת אנשים ונותן להם הרשאות ספציפיות.

7. What is execute in hdfs?

בhdfs אי אפשר להריץ קובץ אז אין משמעות לexecute על קובץ. כשמדובר בתיקייה, צריך execute על מנת להכנס אל תוך איברי התיקייה (כמובן שבנוסף להרשאות הקריאה של האיברים עצמם)


8. Can files later be edited in hdfs?

כן, אבל רק ניתן לעשות append בסוף הקבצים. ככה אנחנו עדיין תומכים בעקרון שהמידע שנכתב הוא נכתב פעם אחת ודברים לא משתנים, בסך הכל מוסיפים אל זה. 

9. How is the cache in hdfs?

משתמשים יכולים לבקש מסלולים ספציפיים שיהיו cached. הלקוח פונה לnamenode שפונה לdatanode ואומר לו לקחת את הבלוקים האלו מהדיסק ותשמור אותם בcache.







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
