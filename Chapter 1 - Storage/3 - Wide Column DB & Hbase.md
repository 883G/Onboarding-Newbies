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

   הwide column database זה ממסד נתונים לא רלציוני (noSQL) שמאחסן מידע בצורה של משפחות עמודות ושורות אבל ניתן ליצור מקבצי עמודות והעמודות בכל שורה יכולים להיות שונים ומפורמט אחר.
   בניגוד לדאטה בייס רלציוני כמו SQL, הנתונים בwide column נשמרים בעזרת key-value-timestamp ולא רק key-value, ניתן לחשוב על זה כטבלה דו מימדית.
   הcolumn family מורכבת מקבוצה של columns.
   האחסון הוא לפי הrow keys (שורות), column family (מקבץ של עמודות) וcolumn qualifiers (עמודות).
   בכל שורה יכול להיות נתונים חלקיים על חלק מהcolumn qualifiers.
   כל column family מורכבת מcolumns.
 השורות בדרך כלל מהוות כמפתח מסויים .
 הסכמות האלה נחשבות מאוד "גמישות" משום שהנתונים בכל תא לא חייבים להיות באותו פורמט, יכולים להיות תאים ריקים ותאים שהפורמט שלהם שונה לחלוטיןף ולכן קל להוסיף/לעדכן נתונים הרבה יותר מאשר בסכמה רלציונית בה יש לכל הנתונים תצורה אחת אחידה וקבועה.
השימוש בtimestamp בניגוד לדאטה בייסים אחרים נותן לשמור כמה גרסאות של אותו נתון ולא רק גרסה אחת שמתעדכנת , כלומר יכול להיות אותו נתון , עם אותו מפתח וערך אבל חותמת זמן שונה שמעידה על הגרסה שלו.

3. **Use Cases & Motivation:**  
   Why do wide-column databases exist? In what scenarios are they most useful (for example: large-scale datasets, time-series data, sparse data, or systems requiring high write throughput)?

   הwide column database קיימים בשביל:
   - להתמודד עם כמות גדולה מאוד של נותנים, הדאטה בייס מהסוג הזה נפרס על גבי כמה שרתים ומאפשר scaling out שנותן להתמודד עם כמויות עצומות של מידע.
   - שמירות של גרסאות ולא גרסה אחת - השימוש בחותמת זמן נותנת לנו לשמור כל עדכון של נתון ולא רק לעדכן אותו בלייב ולשכוח מכל הגרסאות הקודמות
   - נותן לאחסן נתונים גם כשחלק חסרים (מה שהוזכר על כך שלא כל התאים צריכים להיות מלאים) , לא חייב שכל שורה תהיה מלאה בצורה מסויימת
   - רוחב פס גבוה - בגלל שהדאטה בייס מהסוג הזה מפוזר על כמה שרתים, ניתן לקבל הרבה בקשות במקביל ולעבד במקביל ויש ניצול גבוה של רוחב פס
   - גישה מהירה לנתונים - הדאטה בייס מהסוג הזה נותן איזהשהו איזון בין כמות עצומה של נתונים מסוגים שונים שאינם בהכרח רלציונים לעומת העובדה שהם מסודרים במה שמזכיר סכמה, זה הופך אותם להרבה יותר קלים לקריאה וכתיבה.
   - אחסון של נתונים בעמודות מחזק את הscalability, קל מאוד לחלק או להוסיף עמודות והסוג דאטה בייס הזה מאוד "גמיש".
   - ניתן לעשות שאילתות בצורה מהירה מאוד בגלל הגישה המהירה לנתונים.

5. **Distributed Design:**  
   How do wide-column databases distribute data across clusters? Explain concepts such as partitioning, replication, and horizontal scalability.

   הwide column database מחלק את הנתונים בין regions שונים שיכולים להתפרס על כמה שרתים, כידוע יש column families ויש שורות.
   במערכות כמו HBASE כל טווח שורות יהיו פרוסות על region שונv, מה שעושה scaling out ומוריד עומס משרתים בודדים ומחלק אחראיות בין הregions השונים ככה שהעבודה מתאזנת ביניהם.
    עקרון horizontal scalability - כמו שאמרנו כל פעם שהנתונים גדלים מאוד בקלאסטר תמיד אפשר להרחיב את העבודה לשרתים נוספים (כל עוד יש אופציה) ובכך לחלק את העומס.
   שכפול של המידע לכמה איזורים יגביר את השרידות והגישה המהירה אליו , ימנע מצב של איבוד מידע במקרה של נפילת שרת אחד.
   לHBASE יש פיצ'ר שמאפשר להעתיק מידע מטבלה מסויימת לקלאסטר אחר, כדי שזה יהיה אפשרי צריך להגדיר את הREPLICATION_SCOPE של הטבלה ולוודא יצירה של טבלה זהה בקלאסטר אחר, ואז על כל פעולה על אותה טבלה או הטבלה בקלאסטר אחר יהיה סנכרון בין השתיים. זה פיצ'ר נוסף ולא הגרות הדיפולט של HBASE. הדבר משמש בדרך כלל להעתקה של כל הדאטה בייס למקרה של קריסה מערכתית גדולה (מעתיקים לקלאסטר אחר לחלוטין).
   הregionserver של הקלאסטר השני מתעדכן בכך שהוא עוקב אחריי הכתיבות של הregionserver מהקלאסטר מקור לWAL ומשנה את הנתונים שלו בהתאם.
   נוסף על כך בדרך כלל HBASE בנויה על HDFS שכן דואג להעתקה של נתונים. 

---

### Part 2: Apache HBase (Implementation & Operations)

Answer these five questions to cover HBase’s major areas:

1. **Architecture & Data Model:**  
   Describe the overall architecture of Apache HBase, including tables, rows keyed by row key, column families, regions, and the storage format (HFile). How do these elements differ from a traditional relational database, and why is schema design driven by access patterns?


המערכת של HBASE היא בעצם דאטה בייס מבוסס עמודות ומבוזר, הכוונה במבוסס עמודות הוא שכל הנתונים מקובצים לפי תכונות מסויימת בקבוצות של עמודות.
זאת מערכת שבנויה על HDFS, כלומר משתמשת בHDFS לאחסון הנתונים וHBASE מסדרת אותם בטבלאות לפי עמודות ודואגת לread/write random access.
כל דבר בHBASE נשמר כbyte array, וכל תא הוא ממוספר בversion (אבל זה בעצם timestamp חתום  של מתי הוכנס האובייקט).
לכל שורה יש table row key שהוא primary key של כל שורה גם, זה גם מערך בייטים ממוספר לפי הגודל, דרכו יש גישה לעמודות עצמן.
כל התכנים ממויינים לcolumn families לפי תכונה משותפת, לדוגמה במשפחת info, יהיה לנו info:geo, info:format
איו שמירה של המטא-דאטה של העמודות אז ידיעת שמות העמודות וכו זה באחראיות הלקוח.
הטבלה מחולקת לאיזורים לפי שורות, וכל איזור הוא יחידה שפרוסה על cluster של שרתים. ככל שהנתונים גדלים אפשר ליצור יותר איזורים.
הHfile זה הפורמט כתיבה בו כל התוכן ממויין לפי הprimary key.
יש לנו את הHBASE master שהוא אחראי על כל הregionservers, כל regionservers אחראי על regions אחרים.
הHBase master node מחלק את האיזורים לregionservers ואחראי לטפל בהם במקרה של נפילה.
כל regionserver אחראי לטפל בבקשות קריאה\כתיבה.
הHBASE הוא לא רלציוני ואי אפשר לעשות עליו פעולות SQL רלציוניות בשונה מMYSQL וכו... הוא נותן לנו גישה מהירה לכמויות עצומות של מידע שנפרשות על איזורים שונים.
המבנה שלו עם הrow keys מאפשר random access לנתונים (מה שאין בHDFS נגיד) כדי לאפשר גישה מהירה יותר ועבודה מהירה עם כמויות של נתונים שמתעסקים איתם בHDFS.
כל המטא-דאטה של הregions נשמר בטבלה של hbase:meta שהמיקום שלו נשמר בnode של zookeeper.


2. **Components & Storage Flow:**  Explain the roles of RegionServers, MemStore, HFiles, block cache, and the Write-Ahead Log (WAL). How does data flow from a client write to durable storage, and how are reads served from memory and disk structures?

תפקיד הregionServers הוא לנהל את הregions שיש, הוא רץ על dataNode ואחראי על:
אחראי לעשות flush לmemstore , אחראיים על פעולות כתיבה וקריאה לregions שלהם, ניהול הWAL והblock cache שמשותפים לכל האיזורים שלהם.
הregions שהregion server מנהל מורכבים מmemStore, שכל אחד אחראי על column family אחד, ומהstoreFiles, הstoreFiles אחראיים לכל הנתונים שעל הדיסק, והם שומרים אותם בפורמט HFILE, הmemStore אחראי לכל השינויים שנעשים שנשמרים עליו, ואז הregion server עושה לו flush לדיסק ויוצר HFILE חדשים.
לפניי שהכתיבה נעשית בmemStore היא גם נעשית לWAL , שנמצא על הHDFS שמאפשר לשחזר את כל המידע במקרה והשרת נפל.
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
נשמר על הtrailer block ביחד עם הרפרנס למטא-דאטה, עוזר בלמנוע קריאות מHFILES שהנתונים לא נמצאים אצלם.
הbloom filter הוא מערך ביטים מאותחל ל0 עם כמות קבועה של פונקציות hash.
על כל נתון שיש בHFILE, נקודד אותו בK פונקציות HASH ואת הK ביטים בbloom filter array נהפוך ל1.
על כל נתון שמחפשים נעשה את כל הK פונקציות ואם באחת מהK ערכים שיצאו הערך בbloom filter הוא 0 אז אפשר לומר שהנתון לא נמצא בHFILE הזה ואין צורך לעשות scan.
על כל row key נעשת פונקציית hash שיוצרת מערך ביטים, ועושים זאת גם בחיפוש מסמך. אם התוצאה אינה זהה השורה לא בקובץ שמחפשים.
הcaching כולל את הblock cache והmemStore שהגדרנו לפניי, וגם scan caching שזה בעצם כשהלקוח מבקשה לעשות בקשת scan ליותר משורה אחת בטבלה, אז הscan caching קובע מספר מסויים עמודות שיוחזרו כל פעם בצ'אנקים כדי לא להעמיס על הרוחב פס.
כל הדברים האלה עושים את הפעולות קריאה וכתיבה מהירות יותר כי :
- יש לנו גישה מהירה יותר (אפשר לקחת מהcache ולא לטעון מהדיסק כל פעם)
- אפשר לגשת לחלק מהנתונים ולא לסרוק קובץ שלם כל פעם
- האחסון בHFILE מסודר ומפולטר ויש אינדקסים שמורים והrow key ממויין, חיפוש הוא נורא קל
- אנחנו לא מעמיסים על הcache כי עושים לו fkush ולא מעמיסים עם קבצים בינוניים שלוקחים מקום אבל מבזבזים בלוקים וצריך לעשות עליהם הרבה פעולות - כי אנחנו  מאחסנים אותם ישר בHDFS.



4. **Fault Tolerance & Coordination:**  How does HBase use WAL replay, region reassignment, and coordination via Apache ZooKeeper to handle failures and maintain availability? What happens when a RegionServer crashes?

לכל region servers יש WAL שנמצא בHDFS, הWAL משמש כגיבוי למקרה שנפל הregion servver ואיתו הmemStore.
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


******************************* שאלות סקילה *******************************************
1. האם אפשר להעלות HBASE לא על HDFS? כן, HBASE הוא תוצר של hadoop אבל hadoop לא חייב את הHDFS , הוא יכול לרוץ גם על FS אחר או S3 אם מקנפגים אותו בשביל זה.
2. איזה קבצים נמצאים בblock cache (לא תדירות גבוהה)? data blocks שהייתה אליהם גישה לאחרונה.
3. מה הפקודות הנפוצות ואיך נראה query ? פקודות: put, get, delete, scan . הquery יראה כך נגיד: scan 'table_name' בכתיבה לshell, והתשובה תיראה כמו רשימה של column=cfs1:cf, timestamp=0000000, value=x כשמספר השורה גם מופיע.
4. מה הuse cases לשימוש בHBASE?  כמויות גדולות מאוד של מידע שמצריכות פעולות בזמן אמת או random access לנתונים ומצטבר כמויות גדולות של מידע באופן רציף או חוזר, לדוגמה מערכות ניטור או אחסון של איטרקציות של משתמשים. 
5. האם אפשר וכדאי לעשות join בHBASE ? אין פקודה לעשות Join , קשה עם המבנה של הטבלאות( בין column families לארגן מחדש את כל המידע בהם.) אפשר לעשות את הJoin בעזרת spark.
6. הבדלים בין מונגו לHBASE? מונגו הוא דאטה בייס חצי מובנה שנועל בעיקר לסקריפטים וכו, HBASE הוא דאטה בייס לא רלציוני שנועד לכל סוגי המידע, מונגו שומר מידע בקבצי JSON, הHBASE שומר בטבלאות, מונגו בדרך כלל יושב על שרת אחד ואינו מפוזר בעוד שHBASE מפוזר על כמה שרתים.
7. חייב להתחבר לzookeeper? כן, HBASE מסתמך על zookeeper בשביל ניטור מצב הregion servers והHMASTER.
8. אפשר לחלק את טבלת הmeta לכמה שרתים? כן, טבלת המטא היא טבלת hbase בעצמה ומתנהגת כך, היא יכולה להיות מחולקת לאיזורים שונים ואז בחיבור של שהלקוח לzookeeper הוא יקבל את הרפרנסים לכל חלקי הטבלה.
9. מה מכיל את הטבלאות? מה מעליהן? הnamespace - איזהשהי הפרדה לוגית שמאגדת קבוצה מסויימת של טבלאות. בnamespaces שונים נגיד לטבלאות יכולות להיות אותן שמות.
10. האם הblock cache תמיד עדכני? בכללי לא כי אנחנו כותבים בזמן שהנתונים יכולים להישמר שם, מה שhbase עושה כדי לנסות להתמודד עם זה זה שבכל flush שעושים לmemStore אם הנתונים שעוברים לHFILE נמצאים בblock cache אז הם יסומנו כinvalidated וימחקו.
11.  דחיסה גדולה וקטנה:
     דחיסה קטנה - דחיסה שמתייחסת רק לקבצים יחסית חדשים, הוא לא לוקח את כל הקבצים רק חלק מהם (הכי קטנים), קורה דיי הרבה (יכול להיות על בסיס שעתי).
     דחיסה גדולה - לוקחת את כל הקבצים HFILES והופכת אותם לקובץ אחד פר column family, הדחיסה מוחקת כל נתון שמסומן כexpired אבל גם במחיקה אחרת של נתון בעצם שמים עליו סימן "מצבה" שמונע מהנתון לחזור             בשאילתות, בדחיסה גדולה בעצם מוחקים לגמרי את הנתון ומוציאים את ה"מצבה" הזאת. בדחיסה גדולה אנחנו גם מעבירים כל מה שהיה לא לוקלי לשרת הלוקלי. הדחיסה הזאת בדרך כלל נעשית פעם בשבוע בסופשים או בערב כדי להימנע         מwrite amplifications אחריי הכל אנחנו משכתבים את כל הנתונים מחדש לHDFS.
 12. למה צריך גם memStore אם יש כבר WAL?  הmemStore הוא לכל column family לעומת הWAL שכל הregion servers חולקים, אם עבור כל קריאה היינו צריכים לסרוק את הWAL זה היה איטי מאוד, לעומת זאת זה שזה משוייך ספציפית לאחד מקל על השרתים, הWAL הוא יותר לשרידות והmemStore ליעילות. 
     

******************************************************הערות********************************************************************
מבנה:
HMASTER -> אחראי על הרבה REGION SERVER ->  common block cache  -> כל אחד אחראי על הרבה REGIONS -> בכל אחד יש כמה COLUMN FAMILIES -> כל אחת מורכבת מ FILESTORE, MEMSTORE  -> FILESTORE= HFILES

לכל הREGION SERVERS יש WAL משלהם אבל כל הregion חולקים את אותו WAL של הREGION SERVER.
לוקליות:
חשוב שמידע יהיה לוקלי כדי שיהיה פשוט לבצע קריאה וכתיבה (שזה אחת ממטרות הHBASE) והשימוש בHDFS באמת מאפשר לשמור את הנתונים לוקלית בregion אבל אם הregion זז (קורה פיצול או משהו דומה) אז הנתונים לא יהיו לוקלים עד שנעשה דחיסה, כי בדחיסה אנחנו כותבים הכל מחדש ומכניסים לHDFS מחדש, הפעם לdataNode הלוקלי.

מטא דאטה:
טבלת המטא דאטה שומרת - (table, row key range) -> regionserver ופרטים כמו מזהה של הregion, מיקום הregionserver, ומצב הregion
הכוונה במצה היא האם הוא בפיצול כרגע, האם הוא פועל, נפל וכו..
הטבלה מאוחסנת כHFILE ושומרים העתקים שלה ברחבי הקלאסטר (חשוב למקרה של קריסה של השרת)
השרת עליו הטבלת מטא יושבת שולח heartbeats לHMASTER שבמקרה שהשרת יקרוס ימנה שרת אחר שיש עליו העתק.
בדרך כלל הלקוחות יזכרו את האיזורים וישמרו אותם אצלם במחשב כדי לא לתשאל את טבלת המטא כל פעם.
בHBASE 2 יש חיבור ללא zookeeper, כי אפשר לתשאל את הHMASTER איפה טבלת המטא עם בקשת RPC.
באופן דומה הassignment manager היה משתמש בzookeeper ועכשיו הוא מנהל התאמת איזור למנהל בעזרת הPV2.


פיצול איזורים:
עד שהפיצול הסתיים, נוצרים reference files שמצביעים להתחלה של הטבלה המקורית לגישה מהירה לקריאה (אי אפשר לעשות כתיבה).
במהלך הפיצול נוצר קודקוד בzookeeper ותיקייה בHDFS לפיצול.
עושים flushing לאיזור הזה, ומעדכנים את הHMASTER. אחריי הפיצול עושים דחיסה גדולה והקבצי reference נמחקים.
אפשר לעשות פיצול נוסף רק אחריי שהקבצי reference הקודמים נמחקו והדחיסה הסתיימה.
אפשר לעשות פיצול בכוח גם לאיזור קטן יותר בעזרת פקודה ידנית.
אחריי הדחיסה גם הטבלה המקורית נמחקת מהמטא.
במהלך הassignment של איזור לregionserver הוא יהיה בסטטוס opened/closed ובסטטוס הזה אי אפשר לעשות כתיבה או קריאה מהאיזור. זה RIT
הפעולות האלו כמו פיצול ויצירת טבלה  וכו נעשות בפריימוורק בשם PV2 שמאפשר לעשות procedures.
לכל region יש procedure store ששם שומרים את התהליכים בזמן שהם initialized/waiting, זה נשמר על הHMASTER.
את תקינות הregions מוודאים עם כלי בשם hbck שבודק את שלמות הטבלאות ומתקן תקלות, יש לו מוד של קריאה בלבד ומוד של קריאה וכתיבה.
הHBCK 1 היה משנה ישירות את הHDFS אבל HBCK 2 מורה לHMASTER לעשות שינויים דרך הPV2.
יש בנוסף את הbalancer שדואג שאיזורים יהיו מאוזנים, גם אם לא הגענו לגודל המקסימלי (למנוע bottleneck).
הcoprocessor מאפשר לבצע קוד לקוח בצד שרת בשביל בטיחות וכאלה.

הbulk load:
שיטה לעיבוד כמות גדולה של נתונים ,בעזרת spark או mapreduce ולהפוך אותם לHFILES.
### 🔄 Alternatives
Assignment: You are required to research and write a comparative analysis between Hbase and an industry alternative.
- Deliverable: A written summary (minimum 1 or 2 sentences).
- Focus: Compare performance, architecture, and specific "pain points" this tool solves compared to legacy systems or competitors.
- Goal: You must be able to justify why the department uses this tool for our specific environment.

  השוואה - HBASE VS CASSANDRA
  גם HBASE וגם CASSANDRA שתיהן פלטפורמות לאחסון ועיבוד כמויות גדולות של מידע בעזרת דאטה בייס לא רלציוני על בסיס קוד פתוח.
  שתיהן מאפשרות scalability, data recovery.
  הHBASE משתמש בwide column database והקסנדרה משתמש ב column store ששומרת כל עמודה בנפרד בדיסק.
  אבל יש כמה דברים שונים בהתנהגות שלהם:
  - בHBASE שעובדת על HDFS הdatanodes נמצאים במערכת של master-slave ובcassandra הם מתקשרים במערכת של P2P. בגלל שלקסנדרה יש P2P כלומר כל הקודקודים יכולים לעשות קריאה או כתיבה הHA של קסנדרה טובה יותר, אבל העקביות של HBASE טובה יותר כי קודקוד אחד אחראי על ביצוע רפליקות
  - האחסון טיפה שונה, בקסנדרה מאחסנים עמודות קשורות תחת Keyspaces ששונה ממה שהסברנו על HBASE
  - קסנדרה לא דורשת מערכת חיצונית כמו HDFS או zookeeper
  - לHBASE יש latency נמוך יותר מקסנדרה, והקריאה בו יותר מהירה.
  - בקסנדרה הכתיבה מהירה יותר כי אפשר לכתוב מקבילית ללוג ולcache
  הHBASE רגיש למקרי קריסה של הHMASTER (אם אין יותר מHMASTER 1), משום שכל הפעילות תלויה בו, לעומת זאת בקסנדרה יש את הP2P וכל קודקוד יכול לענות לכל בקשה, אז הpain point הזה לא קיים.
בקסנדרה יש בעיית עקביות , בגלל שצריך לעדכן את כל הקודקודים לפעמים המידע לא יהיה מסונכרון.
הבנייה של HBASE יותר מסובכת כי היא בנויה על zookeeper וכו..
אחד מהחסרונות שלו הוא המסובכות של HBASE (תלות בhadoop וzookeeper, ותלות בכלים נוספים - נגיד בלי apache pheonix או כלי דומה השאילתות מאוד מוגבלות).  

### 🎯 User Story & Scenario
Assignment: Based on your research and understanding of the department's pipeline, define a concrete Use Case for this technology.
- Deliverable: A written summary example/story (two paragraphs approx.).
- Requirement: Describe a real-world scenario (e.g., a specific client requirement) where this technology is the optimal solution.
- Data Flow: Map out the data flow and explain how this tool integrates with other components in the Data Pipeline

נראה use case לHBASE:
מערכת של log analytics בה יש לנטר ולעקוב אחריי נתונים פיננסים כלשהם.
זאת פעילות שמתעדכת בבאופן רציף וכוללת כמויות ענקיות של נתונים.
רשימת הלוגים היא בעיקר לקריאה ולא לכתיבה ויש צורך בעקביות תמיד, (נתונים פיננסים חייבים תמיד להיות מדוייקים).
השימוש בHBASE יאפשר ניטור של הנתונים וגם יתן random access לחלקים מסויימים.
הוא גם ישמור על המערכת אמינה כי בנתונים רגישים אפילו אי עקביות אחד יכול להיות עניין גדול.

נראה use case לקסנדרה:
רשתות חברתיות, שבהן יש עדכונים מהירים והרבה כתיבות.
במיוחד העובדה שצריך שעומס הפעולות יתחלק בין הרבה מקומות השימוש בP2P בקסנדרה עוזר.
בנוסף חייב שתמיד יהיה HA מכל הבחינות.
זה בסדר ברשת חברתית שיהיה עקביות בסוף התהליך ולא ישר ברגע השינוי.
הקסנדרה תתאים פה יותר בין אם זה כמויות גדולות של כתיבה (הודעות ברשת, פוסטים, תגובות וכו) או בין אם זה בפעילות מקבילית.


********************************* שאלות מסקילה 2 **************************************************************
1. איך נראה row key של טבלת המטא? שילוב של שם הטבלה, הrow key של השורה הראשונה בregion והregionID.
2. מה זה WAL splits? כשregionserver קורס כל הWAL FILES שקשורים אליו נהיים reassigned לregions specific files עד שהregions יועברו לregion server אחר.
3. מה זה הbalancer והבדל מהnormilizer? הbalancer מעביר regions בין regionservers כדי לודא שיש איזון בכמות הregions בכל השרתים, לעומת זאת הnormalizer משנה regions בעזרת פיצול או איחוד כדי שבכל region server הregions יהיו יחסית זהים בגודל.
   

## Wrapping Up :trophy:
Go over your answers with your mentor and clarify any uncertainties. Relate HBase concepts back to the broader data platform.

## Action Items
- Identify HBase topics you want to delve into further.
- Collect a list of real‑world HBase deployments or related technologies.
- Prepare questions for the next mentor Q&A session.

## Recommended Resources
- [Official HBase Reference Guide](https://hbase.apache.org/book.html) – the definitive documentation.
- *Hadoop: The Definitive Guide* (O'Reilly) – chapters on HBase.
