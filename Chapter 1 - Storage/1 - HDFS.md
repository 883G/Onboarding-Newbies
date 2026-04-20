# Hadoop Distributed File System (HDFS) :elephant:

## Overview
This session focuses on the core concepts of HDFS, the distributed storage layer of the Hadoop ecosystem. Understanding its architecture will help you appreciate how big data clusters store and manage massive datasets across many machines.

**Study the key components, design decisions, and how they work together to provide fault-tolerant, scalable storage.**

## Goals
- Learn the architecture and roles of HDFS components (NameNode, DataNode, etc.).
- Understand how HDFS handles storage, replication, and availability.
- Practice planning a self-study day and managing your time.

:warning: **Note:**
- This is a self-study day; independence and time management matter.
- Focus on grasping the full picture of each concept; if you can’t explain it, you haven’t learned it.
- When in doubt, consult your mentor about what to study.

### ⏳ Timeline
Estimated Duration: 3 Days
- Day 1-3: Learn the concepts of HDFS; spent time on what is it? on fault tolernce, on failover process and on how reads and writes are being done?
    - Have a Q&A session at the third day and in between sessions each day

## Core Concepts

Consider the following five questions to cover the major HDFS topics:

1. **Architecture & Roles:**  Describe HDFS’s overall architecture, including NameNode(s), DataNodes, blocks, and how the namespace and metadata are managed. Don’t forget the role of ZooKeeper in coordinating HA and keeping track of leases.

הHDFS שומר נתונים על שרתים שונים (בדרך כלל 128MB לכל בלוק) ומשכפל את אותם בלוקים כדי לשמור עותקים שלהם למקרה של קריסה.
מי שמחבר את כל השרתים האלו הוא הNameNode ששומר בתוכו את כל הmetadata של המערכת, הוא שומר את השרתים המעורבים ואת מיקום הבלוקים בהם הFS שמורה 
בדרך כלל יש שני nameNodes, אחד פעיל ואחד בסטנד ביי והם אחראים על התקשורת מול הלקוח
והשיכפולים שלהם. הnameNode נשמר על מה שנקרא הnamespace server והוא מנהל שינויים במידע בתוך מה שנקרא edit logs שם נשמר metadata כמו מיקומי בלוקים או מצב הnode. את הedit logs הוא משתף עם הnameNode שבסטנד ביי כדי שלא יהיה פער בין מה שהם יודעים. 
הnamespace אחראי גם על הfsimage שזה מה שמחזיק בפועל את כל המיפוי של הבלוקים וקבצים, זה נשמר בדיסק של השרת.
הDataNode הוא שרת עליו שמורים מספר בלוקים ששומרים בפועל את המידע.
היחסים בין nameNode לdataNodes הם יחסי master-slave, הnameNode אחראי שהdataNodes יבצעו פעולות כתיבה - יוסיפו\יעדכנו קובץ בהתאם להוראות שהוא מוריד להן.
כשאנחנו רוצים להוסיף dataNode אנחנו בעצם טוענים את הedit log לfsimage ויוצרים בלוקים חדשים לנתונים שהתווספו.
הzookeepr אחראי על כך שתמיד יש NameNode אחד שאחראי על הורדת פקודות לDataNodes ועל כך שהוא תקין ומתפקד כמו שצריך, הוא עושה זאת בכך שהnameNode יוצר ephemeral node שמתקשר עם ZFCK  ושולח לו heartbeats שמסמנים שהכל בסדר, אם הnameNode נופל בהתאמה לא נשלחים heartbeats והznode נמחק וככה הzookeeper יודע שיש בעיה.
הzookeeper יבצע בחירות לבחירת nameNode חדש או יפעיל את הסטנד ביי.
הרבה פעמים יש הרבה סטנד ביי, והבחירות נעשות בכך שכולם מקבלים התראה כשהznode של הactive נפל, והם מנסים ליצור ephemeral znode משלהם, מי שמצליח זוכה בבחירות.
יכול להיות רק קודקוד אחד כזה, זה lock node, כלומר היצירה שלו היא אטומית.


2. **Storage & Fault Tolerance:**  Explain how HDFS divides files into blocks, uses replication (default factor three), and how it detects and recovers from node failures.

הHDFS מחלק קבצים לבלוקים של 128MB, כל בלוק בהגדרה הדיפולטיבית משוכפל 3 פעמים.
כל node אחראי לשלוח לnameNode הודעת heartbeat שמדגישה שהכל תקין, אם לא קיבלנו הודעה כזאת הnameNode ישים לב שיש תקלה, הוא יבדוק איזה בלוקים משוכפלים פחות מהמינימום בצריך ויעתיק אותם לnodes בריאים.
אם היינו באמצע כתיבה אז קודם נסגור את הפייפליין של הזרמת packets לכתיבה, נשנה את המזהה של הבלוקים הבריאים כדי שהם לא ימחקו והלא תקין כן , נמשיך כתיבה לdatanode בריא ואז נעתיק את הבלוק לdataNode נוסף.

3. **Topology Awareness & Performance:**  What is rack awareness and why does HDFS replicate across racks? Discuss how block placement, snapshots, and checksums contribute to performance and data integrity.

השיטה בה אנחנו מחלקים את העתקי הבלוקים היא נורא חשובה, ההמלצה על כל בלוק היא:
לשים בלוק אחד בnode של הלקוח
לשים בלוק שני בnode שנמצא בrack אחר
לשים בלוק שלישי בnode שנמצא באותו rack (לא אותו node).
הrack זה בעצם cluster של כמה nodes שתלויים באותו סוויץ'.
כל node ממופה לrack והמיפוי נשמר בnameNode, הניהול הזה גורם לכל שאם סוויץ' כשל לא מאבדים את כל העותקים, וגם יש גישה מהירה לנתונים ששמורים בrack של הלקוח.
לזה קוראים rack awarness, לפי המיפוי השרת מחליט איפה לצרף nameNodes כדי להתחשב בגישה מהירה אבל גם לא להעמיס על rack ולהפחית תעבורה.
הfsimage שומר snapshots שזה צילום של המטא דאטה בנקודת זמן (רשימת בלוקים משוייכת לכל קובץ, וכל פרטי הnameSpace, הרשאות וכו).
דבר נוסף ששומר על אמינות נתונים הוא הchecksum, שהוא מספר שמסמל את כמות הספרות הנכונות בבלוק, זה מועבר כל פעם והdataNode מאמת שהוא זהה לבלוק שניתן לו, וגם הלקוח מאמת שהמידע שהועבר לו תואם לchecksum ששמור.


4. **High Availability & Federation:**  Outline HDFS High Availability (Active/Standby NameNode, JournalNodes) and Federation (multiple namespaces). How do these features improve scalability and uptime?

כמו שהוסבר מקודם, הActive/standby nodes מאפשרים זמינות גם במקרה שהפעיל קרס משום שהקודקוד בסטנד ביי זמין לפעולה.
הjournal nodes הוא חבורת קודקודים שאחראים על ניהול הedit logs בnamespace, והם מאפשרים עדכון של הסטנד ביי, הם נכתבים על שרת חיצוני על הדיסק בכתיבה אטומית בדר"כ ככה שבמקרה של נפילת חשמל לדוגמה אפשר לטעון אותם מהדיסק ולא תהיה תקלה באמצע כתיבה. הnameNode חייב לכתוב לרוב הקודקודים.
בHA אם נפל הnameNode הראשי, הסטנד ביי או החדש שנבחר יכול לשחזר את המידע מתוך ה: journal nodes ששמרו את כל העדכונים שקרו, והfsimage שהסטנד ביי קורא כל כמה זמן גם כשהוא בסטנד ביי. בעזרת הjournal אפשר לשחזר את העדכונים האחרונים גם את הfsimage לא הכי מעודכן.
הFederation הוא מצב בו יש כמה namespaces כדי להוריד עומס משרת אחד (scalability), כל הdatanodes מתקשרים עם כל הnamespaces ועונים להוראות של כולם.
לכל namespace יש block pool משלו כלומר הוא אחראי על תפעול בלוקים מסויימים אבל הdataNodes כולם מאחסנים בלוקים מכל הpools.
קיים מצב בו נוצר split-brain , זה מצב בו זיהינו חוסר פעולה בnameNode והעברנו את האחראיות על nameNode אחר אבל המקורי בעצם לא קרס אלא הייתה בעיה (איטיות או משהו דומה) והוא עדיין מנסה לעדכן מטא דאטה למרות שהוא כבר לא הnameNode. במצב כזה נעשה מה שנקרא fencing, או שנעשה  SSH kill שיחתוך את התהליך של אותו nameNode או שנחסום אותו מהפורט.

5. **Protocol & Operations:**  Describe how clients read and write data to HDFS via RPC, how they locate NameNodes and DataNodes, how DataNodes send block reports, and why these mechanisms matter for everyday operations. Cover the runtime behaviour of leases and pipeline formation.

בקשות קריאה:
בשימוש בAPI, בקריאה לopen() אנחנו קוראים לnameNode בעזרת בקשת RPC ומבקשים לפתוח את הקובץ לקריאה.
הnameNode נותן לנו אינדקסים לdataNodes של הכמה הבלוקים הראשונים והוא מחזיר את העותקים בסדר של מי הכי קרוב ללקוח.
הלקוח קורא read() והDFSinputStream מנהל תקשורת I/O בין הdataNodes לnameNode מאחסן בתוכו את כתובות הdataNodes והולך למי שהכי קרוב.
כל פעם הDFSinputStream יבקש מהnameNode עוד אינדקסים לdataNodes של הבלוקים הבאים.
כל פעם שהDFSI מסיים קריאה הוא יסגור את החיבור לאותו dataNode וימצא את האחד שהכי קרוב בשביל הבלוק הבא.
אם DataNode לא עבד באמצע קריאה הDFSI יזכור את זה ובפעמים באות ידלג עליו ויתעדף רחוקים יותר.


עבור כתיבה הלקוח עושה create() ושולח בקשת RPC לnameNode בבקשה ליצור קובץ.
הnameNode בודק שללקוח יש הרשאות ושאין כבר קובץ כזה ושולח FSDataOutputStream ללקוח שיתחיל לכתוב.
הקובץ מתחלק לpackets שנכנסים לdataQueue בDdataStreamer.
הdataStreamer שואל את הnameNode איפה לשים בלוק חדש והוא נותן לו 3 אינדקסים לשים העתקים.
הdataStreamer יעביר את הpacket לdataNode הראשון והוא יעתיק אותו ויעביר לשני, שיעתיק אותו ויעביר לשלישי.
בסיום של השלישי הוא יעביר אחורה הודעת ACK שמודיעה על סיום, ואז גם השני ואז גם הראשון.
לdataStreamer יש גם תור פנימי של פקטים שמחקים לACK חזור שלהם (פקט שהתחלנו להעתיק ועדיין לא קיבלנו את כל הACKים חזרה).

אם רוצים לשנות קובץ - אי אפשר, אפשר לעשות append לסוף הקובץ.

גם הblock reports נשלחים עם RPC, ביחד עם רשימה של כל העתקי הבלוקים שיש בdataNode הזה כדי לשמור על שלמות הנתונים. שולחים את זה כשהקודקוד נוצר, כשהתווסף או נמחק ממנו קובץ.

הlease מבטיח לנו שרק לקוח אחד יכול לפתוח קובץ כל פעם, בעצם כל פעם שהלקוח יוצר קובץ או עושה אפנד אנחנו "מסמנים" את הקובץ ושמים עליו lease ונבקש לחדש אותו כל פעם. כל עוד הקליינט כותב ימשיכו לחדש את הlease , אחרת אם הלקוח לא מגיב אחריי תקופת זמן מסויימת קצרה יחסית לקוח יכול לקחת גישה לקובץ ואם הוא לא מגיב אחריי משך זמן גדול יותר ולקוח אחר לא לקח את הקובץ אז המערכת תסגור אותו בכוח.


*********** הערה**************************
- הHDFS זה מערכת קבצים מבוזרת של hadoop שפרוסה על שרתים שונים באיזורים שונים ונועדה לאחסן קבצים גדולים מאוד.
  


4. **High Availability :**  Outline HDFS High Availability (Active/Standby NameNode, JournalNodes). How do these features improve scalability and uptime?
5. **Protocol & Operations:**  Describe how clients read and write data to HDFS via RPC, how they locate NameNodes and DataNodes, how DataNodes send block reports, and why these mechanisms matter for everyday operations. Cover the runtime behaviour of leases and pipeline formation.

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
