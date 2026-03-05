# Introduction to HBase :elephant:

> **Note:** this document was renamed earlier to `Wide Column DB & Hbase` to reflect the broader category; the title remains centered on HBase for now.

## Overview
Today’s session dives deeper into column‑oriented databases with a focus on Apache HBase, the Hadoop ecosystem’s wide‑column store. (The filename has been updated to “Wide Column DB & Hbase” per reviewer suggestion.) Understanding HBase will help you see how low‑latency random access is provided over massive data sets.

**The emphasis is on HBase’s architecture, core components, and operational model.**

## Goals
- Grasp the columnar database model and why HBase exists.
- Learn the responsibilities of key HBase components (RegionServer, ZooKeeper, HFile, etc.).
- Improve your ability to plan and self‑direct learning.

:warning: **Note:**
- This is a self‑study day; independence and time management are crucial.
- If you can’t explain a concept clearly, you probably need to revaisit it.
- Read the [Exercise](#exercise) before starting so you know what to emphasize.
- Ask your mentor if you’re unsure what to research.

### ⏳ Timeline
Estimated Duration: 3 Days
- Day 1: Learn the concepts of wide column DB and HBASE spesficly; spend the day.
- Day 2-3: Get deep into HBASE spesficly
    - Have a Q&A session at the third day and in between sessions each day

## Core Concepts

## Part 1: Wide Column Databases (General Concepts)

Answer these questions to understand the fundamentals of wide-column databases before focusing on HBase:

1. **Data Model & Structure:**  
   What is a wide-column database, and how does its data model work? Explain the concepts of rows, column families, and flexible schemas. How does this model differ from traditional relational databases and key-value stores?

2. **Use Cases & Motivation:**  
   Why do wide-column databases exist? In what scenarios are they most useful (for example: large-scale datasets, time-series data, sparse data, or systems requiring high write throughput)?

3. **Distributed Design:**  
   How do wide-column databases distribute data across clusters? Explain concepts such as partitioning, replication, and horizontal scalability.

---

### Part 2: Apache HBase (Implementation & Operations)

Answer these five questions to cover HBase’s major areas:

1. **Architecture & Data Model:**  
   Describe the overall architecture of Apache HBase, including tables, rows keyed by row key, column families, regions, and the storage format (HFile). How do these elements differ from a traditional relational database, and why is schema design driven by access patterns?

2. **Components & Storage Flow:**  
   Explain the roles of RegionServers, MemStore, HFiles, block cache, and the Write-Ahead Log (WAL). How does data flow from a client write to durable storage, and how are reads served from memory and disk structures?


המערכת של HBASE היא בעצם דאטה בייס מבוסס עמודות ומבוזר, הכוונה במבוסס עמודות הוא שכל הנתונים מקובצים לפי תכונות מסויימת בקבוצות של עמודות.
זאת מערכת שבנויה על HDFS, כלומר משתמשת בHDFS לאחסון הנתונים וHBASE מסדרת אותם בטבלאות לפי עמודות ודואגת לread/write random access.
כל דבר בHBASE נשמר כbyte array, וכל תא הוא ממוספר בversion (אבל זה בעצם timestamp חתום  של מתי הוכנס האובייקט).
לכל שורה יש table row key שהוא primary key של כל שורה גם, זה גם מערך בייטים ממוספר לפי הגודל, דרכו יש גישה לעמודות עצמן.
כל התכנים ממויינים לcolumn families לפי תכונה משותפת, לדוגמה במשפחת info, יהיה לנו info:geo, info:format
איו שמירה של המטא-דאטה של העמודות אז ידיעת שמות העמודות וכו זה באחראיות הלקוח.
הטבלה מחולקת לאיזורים לפי שורות, וכל איזור הוא יחידה שפרוסה על cluster של שרתים. ככל שהנתונים גדלים אפשר ליצור יותר איזורים.
כל הנתונים בcolumn family שבאותו איזור מאוחסנים ביחד על קובץ Hfile משותף, Hfile זה הפורמט כתיבה בו כל התוכן ממויין לפי הprimary key.
יש לנו את הHBASE master שהוא אחראי על כל הregionservers, כל regionservers אחראי על regions אחרים.
הHBase master node מחלק את האיזורים לregionservers ואחראי לטפל בהם במקרה של נפילה.
כל regionserver אחראי לטפל בבקשות קריאה\כתיבה.
הHBASE הוא לא רלציוני ואי אפשר לעשות עליו פעולות SQL רלציוניות בשונה מMYSQL וכו... הוא נותן לנו גישה מהירה לכמויות עצומות של מידע שנפרשות על איזורים שונים.
המבנה שלו עם הrow keys מאפשר random access לנתונים (מה שאין בHDFS נגיד) כדי לאפשר גישה מהירה יותר ועבודה מהירה עם כמויות של נתונים שמתעסקים איתם בHDFS.
כל המטא-דאטה של הregions נשמר בטבלה של hbase:meta (מוצפן בMD5) שנשמר בקלאסטר של zookeeper.


2. **Components & Storage Flow:**  Explain the roles of RegionServers, MemStore, HFiles, block cache, and the Write-Ahead Log (WAL). How does data flow from a client write to durable storage, and how are reads served from memory and disk structures?

תפקיד הregionServers הוא לנהל את הregions שיש, הוא רץ על dataNode ואחראי על:
אחראי לעשות flush לmemstore , אחראיים על פעולות כתיבה וקריאה לregions שלהם, ניהול הWAL והblock cache שמשותפים לכל האיזורים שלהם.
הregions שהregion server מנהל מורכבים מmemStore, שכל אחד אחראי על column family אחד, ומהstoreFiles, הstoreFiles אחראיים לכל הנתונים שעל הדיסק, והם שומרים אותם בפורמט HFILE, הmemStore אחראי לכל השינויים שנעשים שנשמרים עליו, ואז הregion server עושה לו flush לדיסק ויוצר HFILE חדשים.
במקביל לכל שהכתיבה נעשית בmemStore היא גם נעשית לWAL , שנמצא על הHDFS שמאפשר לשחזר את כל המידע במקרה והשרת נפל.
הם מנהלים את כל התקשורת מול הHDFS, צריכים גישה אליו ולאחסן בו מידע.
הWAL שומר עדכונים כsequenceFile כלומר שומר הכל כkey-value כשהם הrow, column timestamp ועל כל שינוי מעלה את המספר הסידורי.
הregionserver מנהל את הblock cache - שבו מאחסנים נתונים שעושים להם קריאה דיי הרבה נמצא בheap ביחד עם הmemStore.

הHFILE מכיל נתונים שמחולקים לבלוקים (בדיפולט 64KB), כל בלוק דאטה מורכב מheader וערכי key-value, בנוסף יש Index blocks שמאפשרים לקרוא דאטה בלי לקרוא את כל הHFILE, שממפים את הkey לבלוק שבו הנתונים נמצאים. יש trailer block שמכיל bloom filters. 

איך נראה כתיבה של לקוח?
הלקוח מבקש מהzookeeper cluster את הhbase:meta ששם הוא מחפש את הregionserver הרלוונטי , תוך כדי הם עושים cache כדי ללמוד בעצמם מיקומים.
הלקוח כותב לregionserver ששם את זה בWAL, בmemStore ובcommit log שנמצא בHDFS
כשהmemStore מתמלא עושים flush לקובץ HBASE לHDFS.
הHDFS מחלק אותו לבלוקים, שם אחד בשרת הלוקלי ומפזר את השאר.

איך נראה קריאה של לקוח?
הלקוח מבקש מהzookeeper cluster את הhbase:meta ששם הוא מחפש את הregionserver הרלוונטי , תוך כדי הם עושים cache כדי ללמוד בעצמם מיקומים.
הregionserver יבדוק קודם את הblock cache ואם הנתונים לא שם ילך לHDFS.
הregionserver יתשאל את הnameNode ויקבל ממנו את כל הבלוקים הרלוונטים ויעביר ללקוח.

3. **Performance & Maintenance:**  What are minor and major compactions, MOB storage, Bloom filters, and caching? How do they affect read/write latency, storage efficiency, and amplification? Discuss the importance of row-key design and hotspot avoidance.

דחיסות מינוריות:
הHBASE יקח כמה קבצים קטנים וידחוס אותם לHFILE אחד גדול
דחיסות גדולות:
הHBASE יקח את כל הנתונים בregion מסויים וישכתב את כולם לקובץ HFILE אחד לכל column family.
בדרך כלל עושים את זה בסופשים או בערב כדי להימנע מwrite amplification, שזה תעבורה שקוראת באמצע השכתוב.
הדחיסה הזאת גם מוותרת על תאים שהHBASE מגדיר כexpired ואם יש קבצים על שרתים רחוקים (בגלל שרת שנפל נגיד) היא תעביר אותם להיות לוקלים.
הMOB storage הוא בעצם ניהול אחסון קבצים בינוניים.
קבצים מעל 100KB ועד 10MB (שמוגדרים גם קבצים בינוניים) מקטינים את היעילות קריאה וכתיבה של HBASE כי זה דורש הרבה דחיסות וגורם לwrite amplications.
מה שעושים זה בדרך כלל לאחסן את הקבצים האלו רק בHDFS ולשמור בHBASE פוינטר למיקום שלהם בHBASE.
הbloom filters :
נשמר על הtrailer block ביחד עם הרפרנס למטא-דאטה, עוזר בלהתעלם משורות שאינן רלוונטיות לקובץ שמחפשים כי הrow key לא תואם או שהtimestamp לא בטווח שמחפשים.
על כל row key נעשת פונקציית hash שיוצרת מערך ביטים, ועושים זאת גם בחיפוש מסמך. אם התוצאה אינה זהה השורה לא בקובץ שמחפשים.
הcaching כולל את הblock cache והmemStore שהגדרנו לפניי, וגם scan caching שזה בעצם כשהלקוח מבקשה לעשות בקשת scan ליותר משורה אחת בטבלה, אז הscan caching קובע מספר מסויים עמודות שיוחזרו כל פעם בצ'אנקים כדי לא להעמיס על הרוחב פס.
כל הדברים האלה עושים את הפעולות קריאה וכתיבה מהירות יותר כי :
- יש לנו גישה מהירה יותר (אפשר לקחת מהcache ולא לטעון מהדיסק כל פעם)
- אפשר לגשת לחלק מהנתונים ולא לסרוק קובץ שלם כל פעם
- האחסון בHFILE מסודר ומפולטר ויש אינדקסים שמורים והrow key ממויין, חיפוש הוא נורא קל
- אנחנו לא מעמיסים על הcache כי עושים לו fkush ולא מעמיסים עם קבצים בינוניים שלוקחים מקום אבל מבזבזים בלוקים וצריך לעשות עליהם הרבה פעולות - כי אנחנו  מאחסנים אותם ישר בHDFS.



4. **Fault Tolerance & Coordination:**  How does HBase use WAL replay, region reassignment, and coordination via Apache ZooKeeper to handle failures and maintain availability? What happens when a RegionServer crashes?

כל הregion servers חולקים את אותו WAL שנמצא בHDFS, הWAL משמש כגיבוי למקרה שנפל הregion servver ואיתו הmemStore.
במקרה כזה אנחנו צריכים לשחזר את כל המידע שהיה שם, ונעשה מה שנקרא WAL replay.
הzookeeper אחראי לשים לב כשregion server קרס, והוא מודיע לHMaster שמחלק את הregions לregion servers אחרים , ובהתאם כל הנתונים בWAL מתחלקים לregion servers אחרים שבאחריותם לשחזר את הנתונים הרלוונטים אליהם מהWAL.
זה יקרה גם אם אחד מהregion servers עמוס מדיי, או region עמוס מדיי - יקרה פיצול ואז הregion serer צריך לבקש מהHMaster לעשות פיצול בregion, הוא יחלק את הregion לשני שרתים לפי כמות השורות.
איך יודעים אם הregionServer קרס? 
הzookeeper אחראי לנטר את הפעילות של הregion serversת לכל אחד מהם נוצר ephemeral nodes שברגע של קריסה נמחקים וככה מזהים שיש תקלה.
ככה אנחנו מוודאים שתמיד יש לנו גישה לנתונים ושהם לא נאבדים, וגם שאנחנו תמיד יכולים להתמודד עם קריסה של regionserver אחד.


5. **Scalability & Operations:**  Discuss how HBase scales horizontally through region splitting and balancing, how it relies on HDFS for durability, and what administrative actions (snapshots, backups, schema changes, recovery) operators perform in production environments.


הHBASE עושה scale-out בכך שברגע שיש עומס מדיי על region מסויים היא מפצלת אותו ל2.
הregionserver יבקש מהHMASTER לעשות זאת והוא יחלק את הrow keys בין 2 regions כדי להפחית בעומס.
או שאפשר פשוט להזיז region שלם לregion server אחר.
השמירה של קבצים HFILES בHDFS היא מה ששומרת על שרידות, כי בHDFS הכל נשמר בדיסק והHBASE עצמו הוא יותר לגישה מהירה.
הsnapshots זה סוג של צילום של הHFILE שנשמר בHDFS כדי שיהיה אפשר לשחזר אותו במצב של קריסה, הוא מכיל מטא דאטה של הHFILE ורפרנס אליו.
זה אחד מהדברים שנחשב backup ומאפשר שחזור של הטבלה , ביחד עם כך שאפשר לשמור את כל המטא דאטה על שרת חיצוני.
מבחינת schema changes, אפשר "לשנות" נתונים (חוץ מrow key) רק שזה לא באמת שינוי, יוצר cell חדש כי החותמת זמן שונה.

### 🔄 Alternatives
Assignment: You are required to research and write a comparative analysis between Hbase and an industry alternative.
- Deliverable: A written summary (minimum 1 or 2 sentences).
- Focus: Compare performance, architecture, and specific "pain points" this tool solves compared to legacy systems or competitors.
- Goal: You must be able to justify why the department uses this tool for our specific environment.

### 🎯 User Story & Scenario
Assignment: Based on your research and understanding of the department's pipeline, define a concrete Use Case for this technology.
- Deliverable: A written summary example/story (two paragraphs approx.).
- Requirement: Describe a real-world scenario (e.g., a specific client requirement) where this technology is the optimal solution.
- Data Flow: Map out the data flow and explain how this tool integrates with other components in the Data Pipeline

## Wrapping Up :trophy:
Go over your answers with your mentor and clarify any uncertainties. Relate HBase concepts back to the broader data platform.

## Action Items
- Identify HBase topics you want to delve into further.
- Collect a list of real‑world HBase deployments or related technologies.
- Prepare questions for the next mentor Q&A session.

## Recommended Resources
- [Official HBase Reference Guide](https://hbase.apache.org/book.html) – the definitive documentation.
- *Hadoop: The Definitive Guide* (O'Reilly) – chapters on HBase.
