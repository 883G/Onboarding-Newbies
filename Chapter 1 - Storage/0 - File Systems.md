# File Systems Fundamentals :
## Overview
This session introduces the basic ideas that apply to most file systems, whether they run on a single machine or across a cluster. The goal is to understand how data is organized, managed, and accessed so you can speak intelligently about storage technologies.

**We will focus on general concepts such as hierarchy, metadata, block allocation, and performance trade-offs.**

## Goals
- Develop a foundational understanding of how file systems work.
- Learn the common components and terminology used by most file systems.
- Practice planning a self-study day and estimating time for learning.

:warning: **Note:**
- This is a self-study day. Independence and time management are essential.
- Many newcomers struggle with self-study; take a moment to plan your day and stick to it.
- Understand the **big picture** of each concept. If you can't explain it, you probably haven't learned it.
- Be prepared to describe how concepts relate to one another and to real-world scenarios.
- Review the [Exercise](#exercise) before diving in so you know what to focus on.
- When in doubt about what you need to learn, ask your mentor.

### ⏳ Timeline
Estimated Duration: 0.5 Day
- Day 1: Spent no more than hlaf a day on file systems;
    - Have a Q&A session right after


### Core Concepts

Think through the following questions; by answering them you’ll touch every major topic listed above:

1. **Hierarchy, Metadata & Lookup:**  Describe how a file system organizes files in a namespace, how it separates metadata from content (e.g. using inodes), and explain the steps taken to resolve a path like `/home/user/docs/report.txt` to the underlying data.

הFS מארגן את כל המידע שיש לנו במחשב בתור קבצים שמאורגנים לפי היררכיה מסוימת.
בין כל directory , כלומר כשנכנסים פנימה, אנחנו מוסיפים / לpath של הקובץ. לדוגמה אם בdownloads יש לי תיקייה בשם tests ובתוכה test1, הpath יקרא כDownloads/tests/test1.
הpath הוא ייחודי לכל קובץ, כלומר בכל ספרייה לא יכול להיות 2 קבצים עם אותו השם, בתוך tests יהיה רק קובץ אחד בשם test1.
בלינוקס הFS שומר מידע במבנה נתונים בשם inode , שעובד כמו עץ היררכיה. לכל קובץ יש inode משלו.
הinode מורכב מכמה חלקים.
החלק הראשון שייך לmetadata (גודל קובץ, מתי עודכן לאחרונה, מספר מזהה ועוד..)
החלק השני הוא 12 פויינטרים ישירים למיקומים של ה12 חלקים הראשונים של הקובץ, זה מייעל תהליכים לקבצים קטנים.
החלק השלישי הוא פוינטר לטבלה נוספת שבה יש כתובות נוספות למקרה שצריך עוד בלוקים לקובץ.
החלק הרביעי מכיל פוינטר לטבלה, שמכילה פוינטרים לשתי טבלאות אחרות שמכילות את הכתובות הנוספות אם צריך.
ובחלק החמישי אנחנו מוסיפים עוד שכבה, יש פוינטר לטבלה שממנה יש פוינטרים לשתי טבלאות שמכל אחת יש פוינטר לשתי טבלאות שבהן יש כתובות נוספות.
נסתכל על הדוגמה של tests/test1, יש לנו inode לtests, בחלק השני שלו נראה פוינטר שמוביל ל/test1 ממנו נגיע לinode שלו ששם בחלק השני יש את הפוינטרים לבלוקים של test1.
דוגמה מורכבת יותר:/home/user/docs/report.txt
מתחילים מהinode של home , שם בחלק השני יש פוינטר ל /user, נגיד לinode שלו ושם בחלק השני יש פוינטר לinode של /docs ומשם יש פוינטר לinode של /report.txt ושם יש פוינטרים לכל הבלוקים של הקובץ.


2. **Storage & Allocation:**  Explain block allocation strategies (contiguous, linked, indexed, extent‑based), discuss what internal and external fragmentation are, and outline how performance is impacted by file size and access patterns (small vs. large files, sequential vs. random).

הfile allocation strategies מגדיר באיזה צורה הבלוקים נשמרים על הדיסק, יש כמה שיטות נפוצות:
- שיטת contegous file allocation - הקצאה רציפה, כלומר כל הבלוקים ישמרו אחד אחריי השני. בהינתן גודל הקובץ צריך למצוא כתובת התחלה שיש מספיק בלוקים אחד אחריי השני שיכולים להכיל את כל הקובץ, זה מהווה גם יתרון וגם חיסרון. יתרון כי אין צורך בכמה פוינטרים, כל עוד יודעים את כתובת ההתחלה וגודל הקובץ יודעים איפה כל הקובץ נמצא, הגישה אליו מהירה וקלה, וחיסרון כי נוצר גם פרגמנטציה פנימית וגם חיצונית (יוסבר בהמשך), וגם הגדלת הקובץ זה מסובך כי צריך שבהכרח הבלוק הבא אחריי האחרון יהיה פנוי (ואי אפשר לבחור כל בלוק רנדומלי). במקרה של קבצים גדולים קשה מאוד למצוא מקום רציף שיכול להכיל את הקובץ.
- הlinked file allocation - הבלוקים לא צריכים להיות רציפים, הם מתנהגים כמו רשימה מקושרת. בinode שלנו נשמור פוינטר לבלוק הראשון והאחרון וכל בלוק יחזיר פוינטר לבלוק הבא אחריו, הבלוק האחרון לא יצביע על אף אחד אלא יהיה null pointer. יתרונות: קל להגדיל את הקובץ, אין פרגמנטציה חיצונית. חסרונות: הרבה פוינטרים לבלוקים שיכולים להיות בכל מקום בדיסק וזה הופך את התהליך לאיטי יותר וגם כדי לגשת לבלוק N צריך לעבור את כל תהליך הפוינטרים מהבלוק הראשון. במקרה של קבצים גדולים זה מכביד מאוד ומאט את התהליך.
- הindexed file allocation - מה שהוסבר בשאלה הקודמת, יש טבלה של פוינטרים המצביעים לכל הבלוקים (יכול להתחלק גם לכמה שכבות), זה מונע פרגמנטציה חיצונית וגם נותן גישה לבלוק הN בלי לעבור את כל התהליך שעוברים בlinked. אבל מקצים הרבה מקום לטבלאות פוינטרים ולפעמים המקום הזה יכול להתבזבז אם הקובץ קטן. במקרה של קבצים גדולים נלקח הרבה מקום על שמירת פוינטרים, אבל זה יותר קל לשימוש מlinked.
- הextent-based file allocation - גרסה משודרגת יותר לindexed,  אפשר לשמור לפי צ'אנקים של בלוקים, נגיד ויש לנו קובץ שצריך 8 בלוקים ויש בזיכרון 5 בלוקים פנויים במקום אחד ו3 במקום אחר, אז אפשר לשמור בלוק התחלתי וכמה בלוקים ברצף ואז עוד בלוק התחלתי וכמה בלוקים ברצף במקום לשמור פוינטר לכל בלוק. בשיטה הזאת, מונעים פרגמנטציה חיצונית וממש מקטינים סיכויים לפרגמנטציה פנימית.

  מה זה פרגמנטציה חיצונית? פרגמנטציה חיצונית נוצרת כשיש בלוקים פנויים אבל לא באופן רציף, ואי אפשר לשמור קובץ באופן רציף עליהם, לדוגמה בcontegous.
  מה זה פרגמנטציה םנימית? כשגודל הקובץ לא מתחלק לגמרי לפי גודל הבלוקים וחלק מהבלוק יכול להיות מבוזבז למרות שאין בו צורך. כשנותנים יותר זיכרון ממה שצריך. יכול לקרות גם בlinked, indexed , extent based אבל בextent בדרך כלל רק בבלוק האחרון.
   

3. **Directories, Indexing & Permissions:**  Compare different directory indexing methods (linear lists, hash tables, B‑trees) and why efficient lookup matters. Then describe common permission models such as UNIX mode bits and ACLs, and how access control integrates with directory lookup.

כשאנחנו מסתכלים על השיטות לסידור הdirectory יש לנו כמה שיטות לעשות את זה:
- שיטת linear lists : הצורה הכי פשוטה לסידור הdirectories, מסודרות ברשימה אחת אחריי השנייה. כלומר בתוך התיקיית test לדוגמה כל הפוינטרים לinodes של הקבצים בתוכה יהיו רשומים ברשימה ליניארית. חיפוש, הכנסה/מחיקה נגיד יעלה לנו (n)O. קל להבנה אבל לא יעיל לספריות גדולות שמכילות הרבה קבצים בתוכן.
- שיטת הhash table : בעזרת פונקציית hash ממפים את הקבצים לרשימה, אם מדובר בשיטת chaining בכל תא יש רשימה מקושרת דינאמית של אובייקטים ואם מדובר בשיטת open addressing אז מוצאים מקום אחר בטבלה פנוי לפי פונקציית גישוש (בעייתי יותר כשבא למחיקה), חיפוש עולה (1)O וככה גם הכנסה ומחיקה, אבל הגודל של הטבלה קבוע מראש ואם יש כמות ענקית של קבצים זה יכול ליצור בעיה. פונקציית hash נפוצה: לחבר את סכום הASCII של השם קובץ ולעשות מודלו הגודל טבלה.
- שיטת הB-tree : הdiectories מסודרות בעצים מדרגה m (כלומר לכל תיקייה יכול להיות עד m ילדים) ערך הm נקבע לפי גודל הבלוקים בדיסק. לכל קודקוד בעץ יש ערך, כל ילד מצד ימין יהיה עם ערך גבוה וכל ילד מצד שמאל יהיה עם ערך נמוך. כלומר, הבנייה תהיה לפי לקסיקוגרפיה של השמות קבצים, ובחיפוש בגלל שהעץץ בינארי החיפוש יהיה בינארי בסיבוכיות (logn)O. זה גם הסיבוכיות של המחיקה והכנסה. 

מודלים נפוצים לשליטה בהרשאות לקובץ:
- הUNIX mode bits : 12 ספרות בינאריות שמייצגות את ההרשאות. ה3 הראשונות מייצגות גישה מיוחדת setuid מריצה את הקובץ עם הרשאות של הבעלים, setgid מורישה לקובץ את הקבוצה של הdirectory שהוא נמצא בו, וsticky bit מונעת מחיקה של הקובץ, רק הבעלים יכול. ה9 ספרות הבאות מייצגות : 3 הרשאות לבעלים, 3 הרשאות לקבוצה ו3 הרשאות לשאר כל ביט מיצג קריאה, כתיבה והרצה אם יש הרשאה יהיה 1 ואם אין יהיה 0. לאחר מכן הופכים את ההרשאות למספר לפי הספרה הבינארית שיצאה, דוגמה:  100 110 111 000: ספרה ראשונה 0 ספרה שנייה 7 ספרה שלישית 6 וספרה רביעית 4 אז ההרשאות יהיו 0764.
- הACL : בלינוקס זה מאפשר לתת הרשאות ליוזר או קבוצה ספציפי מעבר למה שאפשר בmode bits בעזרת setfacl משנים הגדרות. נגיד בעזרת setfacl -m "u:user:permissions" /path/to/file עושים שינויים להרשאות של יוזר ספציפי.
-  
מה שמאחד את הניהול הרשאות ופעולות חיפוש בשיטות שונות בdirectory זה LDAP, שבעזרתו עושים גם את החיפוש בDirectory וגם את הניהול הרשאות.
4. **Consistency, Journaling & Caching:**  Why do file systems employ journaling or copy‑on‑write logs? What problems do these techniques address, and how do caching and write buffering interact with crash recovery and power‑failure scenarios?

הjournaling הוא בעצם תהליך בו הFS שומרת שינויים לקובץ שעדיין לא נשמרו לקובץ סופית (metadata בדרך כלל), בעצם מתעדים את כל הגישות שנעשו לדיסק בצורה אטומית. זה בא למנוע בעיות שחיתות או שגיאות בהן אם נפל החשמל או קרתה תקלה והmetadata לא נרשם עד הסוף, אז הוא לא תואם את מה שיש בפועל. עם הjournaling משלימים את מה שחסר בעזרת הגישות שנרשמו לדיסק.
עיקרון דומה קיים עם copy‑on‑write logs , שומרים לוגים של השינויים שנעשו. כלומר במקום לשנות את המידע שקיים אנחנו יוצרים עותק חדש ושם מבצעים שינויים וככה אם נפל החשמל או קרתה תקלה באמצע העדכון לא איבדנו את כל הקובץ אלא את הגרסה החדשה במקרה הרע. זה קצת שונה מjournaling כי שם אנחנו לא משנים מידע אלא רושמים מה צריך לשנות ואז מעדכנים ופה יוצרים קובץ חדש ומשנים את המידע
אחד מהדברים הנוספים שמערכת ההפעלה עושה זה read&write caching שומרת נתונים בRAM בשביל ניהול מהיר יותר. אם המ"ה מצפה שיהיה שימוש קרוב בקובץ היא טוענת העתק שלו מראש למה שנקרא הpage cache כדי שהקריאה ממנו תהיה מהירה או בשביל כתיבה (lazy writing).
בצורה דומה בwrite buffering שומרת שינויים שנכתבים לקובץ זמנים בבאפר לפני שזה נכתב לדיסק ישירות.
שני הדברים האלה בעצם מסכנים את המידע שלנו באיזה שהו מקום כי המידע הזמני הזה ששמרו לא ישמר אם נפל החשמל או קרתה תקלה, לכן חייב לסנכרן את הנתונים בdisk ביחד איתם בשנייה שהשלמנו כתיבה. משתמשים במתודות כמו checksum.


5. **Performance Trade‑offs & Distributed Extensions:**  Discuss the key trade‑offs between throughput, latency, and reliability in file systems. Finally, briefly explain how additional concepts like replication, failover, and namespace servers extend these ideas in distributed systems (HDFS, Ceph) without re‑inventing the core principles.

תפוקה והשהייה הם שני קריטריונים שבודקים את התנהלות מערכת הקבצים. תפוקה מייצגת כמה נתונים אנחנו יכולים לעבד במערכת הקבצים בזמן מסויים לדוגמה כמה קבצים ניתן להעביר בבת אחת בזמן מסויים והשהייה מייצגת כמה זמן לוקח ממתי שנעשתה הבקשה עד שההוצאה לפועל שלה מתחילה לדוגמה כמה זמן לוקח להעתיק ולהדביק קובץ. התנהלות טובה באחת מהם לא בהכרח אומרת שהשני גם עובד טוב, לדוגמה יכול להיות שזמן התגובה לבקשות לוקח המון זמן, אבל כן שאפשר להעביר הרבה מידע בזמן קצר.
קריטריון נוסף שמודד התנהלות של הFS הוא אמינות, האם הצלחתי להעביר את כל הנתונים בשלמותם, בסדר שהם צריכים להיות. הרבה פעמים תפוקה גבוהה או זמן השהייה קצר יכולים לבוא על חשבון האמינות, נגיד בהעברה של קובץ גדול מאוד יכול להיות שלא כל הקובץ עבר כמו שצריך.
עקרונות נוספים:
- שכפול\replication - שמירה של כמה עותקים בכמה שרתים ובכמה איזורים כדי למנוע איבוד של כל המידע לגמרי. לדוגמה אם יש תקלה איזורית והשרת נופל אנחנו לא רוצים לאבד את כל המערכת שלנו. נוסף על כך חייב לשמוא עותקים של דברים כמו מפתחות הצפנה כדי לא לחסום גישה למידע מעצמנו. כמו בHDFS שלכמות שונה של שרתים יש גישה לFS ויכולים לקרוא ולכתוב אליה.
- בעיית failover - בהמשך לשכפול, הfailover הוא העברה אוטומאטית לשרת אחר לשכפול של המערכת אם היה כשל ושרת קרס. צריך לעשות זאת בצורה מיידית ולהעביר את כל הלקוחות המחוברים לשרת אחר. במערכות מבוזרות כמו HDFS הFS מחולקת ושמורה בעותקים על פני כמה שרתים, אז גם אם שרת אחד נפל המערכת לא קרסה.
- עקרון הnamespace server - בHDFS יש לנו namespace server שהוא הnameNode הוא בעצם מקבץ קבצים שתחת אותה תיקייה אבל בשרתים שונים ומראה את זה למשתמש כתיקייה אחת עם הקבצים בתוכה ללא קשר למיקום השרתים אבל מפנה אותם לשרת בו הם נמצאים. הוא שומר את השמות שרתים וכתובות שלהם ומיקומי הבלוקים אבל לא בהכרח את המידע עצמו.

  שלושת הדברים האלו עוזרים להוריד את זמן ההשהייה ולהגדיל את התפוקה בכך שהם לא מעמיסים מדיי על שרת אחד (המערכת מבוזרת) אז העברת קבצים גדולים לא מכבידה, וגם הם נותנים גישה מהירה מאיזורים שונים ומפחיתים בקשות על שרת אחד מה שמוריד את הזמן השהייה. בנוסף העזרה שלהם לכשלים מגבירה אמינות.

   ******************* הערות ************************
  - למה צריך random access ? כשרוצים לקרוא חלק מהקובץ, לדוגמה בלוגים אם רוצים רק את הזמן האחרון, או קבצי parquet שהם קבצים בדר"כ מוצפנים ודחוסים שמסודרים בעמודות נועד להתמודד עם כמויות גדולות של מידע ולסדר אותו עבור OLAP. המידע נשמר בצ'אנקים של מידע בעמודות ואפשר לגשת לעמודה מהגדרות המטא דאטה שבסוף הקובץ.
  - merge-on-read, מעדכנת את המצב רק כשיש בקשה באמת לקרוא את הקובץ.
  - הרשאות למחיקת קובץ תלויות בכתיבה והרצה לתיקייה שהוא נמצא בה.
  - ההרשאות של הקובץ נשמרות בinode במטה דאטה שלו בלינוקס ובHDFS זה נשמר בnameNode.
  - הNFS וSMB שתיהן מערכות קבצים ברשת , NFS בלינוקס וSMB מקבילה אליה בווינדוס
  - אנומליות של rwx: הרשאות קריאה אבל לא הרצה - לא אפשרי להריץ סקריפט שאין לו הרשאת ריצה כי הקרנל מעביר את הקובץ לאינטרפרטר שצריך לפתוח אותו כדי להריץ אותו, על קובץ בינארי של הוראות מחשב אפשר להריץ בלי לקרוא. הרשאות כתיבה אבל לא קריאה - אפשר לעשות < או << אבל לא cat נגיד, על תיקיות אפשר לעשות קובץ חדש או למחוק אבל לא לעשות ls.
  - file attributes: a(append-only) - אי אפשר לשנות תוכן קיים רק להוסיף לסוף (טוב נגיד לקבצי לוגים), s - כל שינוי לקובץ ירשם לדיסק במיידי, 
  - אפשר לראות בעזרת lsattr
     

### Real-World Context
Rather than focusing on one technology, think about how these ideas show up in common operating systems (ext4, NTFS, APFS), networked storage (NFS, SMB), and cloud offerings (S3, Azure Blob). Your task is to recognize the underlying principles across implementations.

## Wrapping Up :trophy:
Discuss your answers and any areas of confusion with your mentor. Reflect on how these general concepts will help when you later study specific systems such as HDFS.

## Additional Topics from Review
- The I/O path: what happens when an application calls `read()` or `write()`? Understand the kernel I/O path, page cache, and block layer.
- Mounting & abstraction layers: what “mounting a filesystem” means, and the separation between filesystem, block device, partition, volume manager. These ideas are essential later for containers, cloud disks, distributed storage, RAID/LVM.

## Action Items
- Review your notes and identify topics you want to explore deeper.
- Collect a list of real-world file systems you’d like to examine in future chapters.
- Prepare questions for the upcoming mentor Q&A session.
- Continue the Day 01 challenge by mapping these ideas to future chapters.

