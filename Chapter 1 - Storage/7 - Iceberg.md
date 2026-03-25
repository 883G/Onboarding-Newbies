# Apache Iceberg

Now that you are familiar with the concepts of catalogs and the metastore,
and understand the critical separation between how data is stored versus how it is logically organized,
it is time to move from theory to the practice of the modern data world.

Meet Apache Iceberg – the table format we use as the storage layer in our lakehouse.
designed to solve the consistency and performance "pains" of legacy directory-based systems.

###⏳ Timeline
Estimated Duration: 2 Days
- Day 1: Independent research and deep dive into the foundations of Iceberg.
- Day 2:
  - (Morning): First Q&A.
  - (End of Day): Question Answering & Final Q&A.

### 📚 Resources
Use the resources listed below and practice searching the internet for questions not answered by the provided documentation.
- [Apache Iceberg Official Docs](https://iceberg.apache.org/docs/latest/#documentation)
- [Apache Iceberg Definitive Guide](http://103.203.175.90:81/fdScript/RootOfEBooks/E%20Book%20collection%20-%202024%20-%20F/CSE%20%20IT%20AIDS%20ML/Apache%20Iceberg%20(2024).pdf)
- [Meap Book - Apache Iceberg](./asstes/Architecting_an_Apache_Iceberg_Lakehouse_v3_MEAP.pdf)

### Guide Questions❓
Please use these questions as a guide for your research, dive in, and deepen your understanding of all concepts.
1. What is Apache Iceberg? 
   Explain the problems it solves compared to Hive tables (schema evolution, partitioning, consistency, performance).

הapache iceberg הוא table format שנוצר ב2017 כמענה לבעיות ביצועים ועקביות בhive שנוצרו בגלל דימוי הטבלאות כdirectories.
הiceberg בא להציע table format חדש עם שיפורים:
- עקביות : אם מעדכנים נתון על גבי כמה partitions שונים, או שיראו את כל הpartitions כפי שהיו לפני השינוי או לגמרי אחריי, לא יהיה באמצע. זאת בעיה שנוצרה בhive כשלא יכלו להבטיח עקביות בנתונים ששונו על גבי כמה סכמות, וביצירה של קובץ חדש לא הייתה דרך להבטיח אטומיות, לקוח היה יכול לראות את הנתונים כשהם עוד "בתהליך".
- ביצועים : בגלל המבנה של הטבלאות בhive כdirectory , כל שאילתה לוקחת זמן לבצע עוד לפני שהיא בוצעה בכלל בגלל הצורך לסרוק את כל הlist באותו directory והכרחיות לסרוק גם קבצים שלא בהכרח רלוונטים. iceberg בא לפתור את זה בעזרת מטא-דאטה שהטבלה עצמה מספקת שמונע את זה ומשפר משמעותית את הביצועים.
- פרטישנינג : הפרטישנינג בiceberg הרבה יותר פשוט מאשר בhive כי הלקוח לא צריך להיות מודע לחלוקה הפיזית של הטבלה. לדוגמה - בhive אם הפרטישן הוא לפי חודשים, והלקוח יבקש לעשות פילטר לפי timestamp אז עדיין כל הטבלה תיסרק למרות שהtimestemp והחודש הוא אותו קריטריון בפועל, הhive לא יזהה את זה כי אין column עם הקריטריון הזה, זה מכריח את הלקוח לדעת את מבנה הטבלה ואת הפרטישנים. בiceberg פותרים את הבעיה הזאת בעזרת טרנספורמציות truncate, buckets...
- הschema evolution : העדכון של הסכמה בhive יכול לגרום לטרנזקציות לא בטוחות, ועדכון פרטישן יכול להצריך שכתוב של כל הטבלה. iceberg פותר את זה ומאפשר עדכון של פרטישן ללא צורך בשינוי כל הטבלה.

הapache icenerg נוצר כדי לספק שכבת metadata שמאפשרת שאילתות בצורת SQL על הנתונים באופן מהיר ופשוט על כמויות גדולות מאוד של נתונים, באופן בו המפתח או הלקוח לא צריך כמעט להתעסק בשכבת האחסון או בפורמט הטבלאות אלא לעסוק בשאילתות בלבד. 

2. Describe the Apache Iceberg table architecture. 
   Explain metadata files, manifest files, data files, and snapshots and how they relate to each other.

ארכיטקטורת apache iceberg: 
במקום להשתמש במודל של תיקיות, icenerg משתמש במודל של עץ שבו שכבת המטא-דאטה מורכבת מכמה מרכיבים:
- מרכיב הmanifest file : רשימה של datafiles שמכילים את הנתונים עצמם ומאוחסנים בשכבת הDATA ביחד עם הdelete files, הנתיב שלהם ועודנפרטי מטא-דאטה הכרחיים.
- מרכיב הdelete files מכיל את המחיקות שנעשו לקבצים בשיטת MOR כלומר, ברגע שמשתמש יבקש לקרוא קובץ נמזג את הקובץ עם השינוי שנעשה (בניגוד לCOW שעושה קובץ חדש לכל שינוי).
- מרכיב הmanifest list : אוסף של manifest files ופרטים עליהם שמהווים סוג של סנאפשוט של הטבלה, שומר גם איזה manifest file שייך לאיזה partition ואת המספר מקסימלי ומינימלי של עמודות שיכולים להיות בdatafile . יש בmanifest list את הarray של structs שבכל אחד יש מעקב אחריי manifest file אחד (כמה קבצים בו נמחקו, מזהה של הסנאפשוט אליו הוא שייך וכו).
- מרכיב הmetadata file : קבצים שמגדירים את מבנה הטבלה, הסכמה שלו, פרטישנים ורשימת המניפסטים. כל פעם שנעשה שינוי לטבלה בiceberg, נוצר קובץ metadata חדש. נשמר בו הגרסה, מזהה ומיקום של הטבלה, סנאפשוטים ועוד.
- הקטלוג : אחראי על מיקום הטבלה, כל המידע בו נשמר בתור שם טבלה -> מיקום של הקובץ מטא-דאטה שלה בניגוד לhive בו יש שם טבלה -> רשימה של directories.
- מרכיב הpuffin files : קבצים שאוגרים סטטיסטיקות ואינדקסים על הטבלה

כלומר iceberg מוסיפה פה שכבה נוספת של קבצי המטא-דאטה ששומרים סנאפשוטים, הם מה שמאפשרים פה את העקביות ושמירה על אטומיות, למה? כי במקרה בו לקוח רוצה לקרוא טבלה בזמן שנעשים שינויים כמו שינוי פרטישן, אז בניגוד לhive בו יכול להיות שהוא היה רואה נתונים במהלך השינויים (כלומר לא עקביים) , בiceberg הוא יפנה ישירות לסנאפשוט שיכיל את כל הmanifest list והוא מהווה תמונת מצב של הטבלה לפני השינויים (או אחריי אם השינויים כבר בוצעו) אבל אין מצב שזה יהיה סנאפשוט באמצע השינויים.

3. What is an Iceberg catalog, and what is its role? 
   Explain what a catalog manages (table namespace, metadata pointers, commits), why it’s required, and how it differs from a metastore. 
   Mention common catalog implementations.

הקטלוג של iceberg הוא הצעד הראשון לכל אינטרקציה עם הטבלאות. הדרישה המרכזית מקטלוג הוא שהוא יתמוך בפעולות אטומיות.
הקטלוג ממפה בין כל טבלה לפוינטר לקובץ מטא-דאטה שלה ושומר קבוצות של טבלאות בתוך namespace.
בגלל שאלה הדרישות היחידות מהקטלוג, הרבה שירותי backend יכולים להוות קטלוג, וכולם יכולים לאחסן את הפוינטרים בצורה אחרת.
הhive metastore לדוגמה יכול להוות את הקטלוג ולאחסן את המיקום של קבצי המטא-דאטה.
קטלוג נוסף שנפוץ הוא AWS glue, hadoop catalog  וJDBC.
קטלוג hadoop - מחפש לפי גרסה אחרונה בעזרת timestamps , קל לשימוש (צריך רק FS) , אבל מגביל מבחינת כלים לאחסון.
מטאסטור - אינטגרציה טובה עם כלים אחרים, אטומיות ומקביליות מוגבלת.
קטלוג AWS - אינטגרציה טובה עם כלים של AWS, לא תומך בטרנזקציות בין טבלאות. סוג של iceberg שמנוהל ע"י amazon.
אלה קטלוגים קלאסים, אבל יש איתם עדיין בעיות כמו קונפיגורציות מסובכות בצד לקוח ותלות בשפה מסויימת, בשביל זה ceberg עובד גם עם קטלוג מסוג REST.
קטלוגים מסוג REST משתמשים בREST API בו בקשות נשלחות בHTTP ויכולות להיות בשפות שונות, פייתון , JSON ועוד..
סוגים של קטלוגי REST הם tabular, polaris ועוד.

4. How does Iceberg handle concurrent reads and writes? 
  Explain snapshot isolation, atomic commits, optimistic concurrency control, and conflict detection.

נסביר את ההתמודדות של iceberg עם מקביליות בכך שנסתכל על הlifecycle של תהליך קריאה/כתיבה:
נגיד והלקוח רוצה לשנות טבלה מסויימת, הוא יגיע לקטלוג קודם משם יקבל הפנייה לmetadata file עם הגרסה הכי עדכנית שאחראי על הטבלה.
הmetadata file יפנה אותו לsnapshot של הטבלה ברגע נתון. בגלל שהסנאפשוטס נוצרים אחריי סיום התהליך, גם אם מישהו שינה או משנה נתונים במהלך שהלקוח רוצה לגשת לטבלה, הלקוח יראה את הטבלה או לפני השינויים (סנאפשוט לפני) או אחריי (סנאפשוט חדש) , לא באמצע השינויים - זה האטומיות.
בנוסף לזה, iceberg משתמש במתודת optimistic concurrency control, כלומר הוא מניח שהטרנזקציות של לקוחות שונים לא מתנגשות - או שהן עובדות או שהן נכשלות, למה? כי מתמודדים עם המקביליות בסוף בצורה אטומית. נגיד ושני משתמשים עשו שנאפשוטים שונים מקבילים ורוצים לעשות commit, ההחלפה של הגרסה האחרונה היא אטומית ולכן אחד מהמשתמשים יכשל ויצטרך לעשות זאת מחדש על הנתונים המעודכנים.

5. What maintenance operations does Iceberg require, and why? 
   Discuss compaction, snapshot expiration, orphan file cleanup, and metadata cleanup.

כמה מהפעולות תחזוק שiceberg דורשת :
- דחיסה : הפעולה של לפתוח לסרוק קובץ ולסגור אותו גם לוקחת זמן, וכשיש הרבה מאוד קבצים קטנים היא יכולה סתם להאט את התהליך על סריקה וסגירה של כולם. כפתרון לזה, בiceberg דוחסים הרבה קבצים קטנים לכמה קבצים גדולים, זה יכול לקרות אוטומאטית או ידנית והדחיסה יכולה להיות בשיטת binpack שהיא פשוט לחבר קבצים או עם sort שלוקח יותר זמן אבל מקצר זמני קריאה.
- תוקף של סנאפשוטס : iceberg מגדיר תוקף לסנאפשוטס ומוחק אותם ברגע שהם פגי תוקף, מחיקת הסנאפשוט תמחוק איתה את כל הdatafiles שיחודיים לה כלומר אם עוד סנאפשוט משתמש בdatafile הוא לא ימחק.
- מחיקת קבצים או קבצי מטא דאטה שכבר לא בשימוש (נקרא גם orphan file cleanup ) : iceberg מוחק קבצים שכבר אין להם רפרנס בסנאפשוט (כלומר, אין להם שימוש יותר בטבלאות), נעשה גם אוטומאטית או ידנית.
- מחיקת קבצי מטא דאטה : ניתן להגדיר ביצירה של קובץ מטא דאטה חדש מחיקה של ישן.


### 🔄 Alternatives
Assignment: You are required to research and write a comparative analysis between Iceberg and an industry alternative.
- Deliverable: A written summary (minimum 1 or 2 sentences).
- Add real life usecase 
- Focus: Compare performance, architecture, and specific "pain points" this tool solves compared to legacy systems or competitors.
- Goal: You must be able to justify why the department uses this tool for our specific environment.

האלטרנטיבה הכי ידועה לapache iceberg היא delta lake, בדומה לiceberg היא גם שומרת על עקרון ACID, עובדת עם ספארק ומאפשרת time travel, אבל הגישה שלה לזה שונה לחלוטין.
אם iceberg נוהגת בשיטת MOR ובעיקרון בו מטפלים בבעיה רק כשמנסים לעשות לה execute (כמו הדוגמה על הcommits) אז delta lake נוטה בגישה שונה לגמרי, בגישת MOR, ברגע שיכתב שינוי לא תקין היא תעצור אותו והיא משתמשת בtransaction log בשביל זה שפעם בכמה זמן היא "מרוקנת" לקבצי פרקט, ובהתאם לכך היא מתמקדת רק בקבצי פרקט ולא גמישה כמו iceberg.
הiceberg שם דגש על ארגון וסידור המידע, ואחסון יעיל (דחיסות, פרטישנים מתקדמים) בעוד שdelta lake שם דגש על ביצועים מהירים.
נשתמש בiceberg במקום בו יש מודל נתונים מסובך שצריך לו סכמה גמישה שאפשר לשנות , ושצריך אינטגרציה עם כלים כמו ספארק וטרינו.
נשתמש בdelta lake כשהדגש הוא על ACID ושלמות הנתונים או כשמדובר בסטרימינג (עבודה עם ספארק).
** בCOW על כל שינוי קטן יוצרים קובץ וסנאפשוט חדש - זה יעיל לread heavy כי לא צריך לעבור על קבצים מחוקים וכו השינוי מתבצע מיד. אבל המחיקות וכתיבות יהיו איטיים יותר. בMOR בעת מחיקת נתון הנתון יצור delete file ובעת עדכון נתון הנתון הישן יצור delete file וניצור קובץ חדש רק עם השורה המעודכנת וכשלקוח יעשה קריאה הוא יתעלם מהשורה הישנה כי היא בdelete file ויגש לחדשה. זה עדיף לwrite heavy אבל מכביד על תהליכי הקריאה

### 🎯 User Story & Scenario
Assignment: Based on your research and understanding of the department's pipeline, define a concrete Use Case for this technology.
- Deliverable: A written summary example/story (two paragraphs approx.).
- Requirement: Describe a real-world scenario (e.g., a specific client requirement) where this technology is the optimal solution.
- Data Flow: Map out the data flow and explain how this tool integrates with other components in the Data Pipeline.

***************** שאלות סקילה ***********************************
1. איפה נשמר איזה type יכול להיות בעמודה? בmetadata files 
2. הבדלים map vs struct vs list? בסכמה של טבלה הסוג מידע יכול להיות פרימיטיבי או - struct טיופל של ערכים מוגדרים. - list רשימת ערכים מאותו סוג - map ערכי key-value.
3. איך נוצרים orphan files והאם זה יקר מבחינת עלות? קבצי דאטה שנמחקים דרך iceberg, פעולות כתיבה שנכשלו והותירו קבצים. זה יכול להיות יקר כי אנחנו צריכים ללכת למקום הפיזי שהטבלה מאוחסנת בו ולעשות ליסט לכל הקבצים, ולהשוות ביניהם לכל הקבצים במניפסט ליסט.
4. איפה מגדירים סנאפשוט?
5. האם אפשר לעדכן מידע ישירות באחסון? אפשר לא מומלץ, הפעולה MSCK REPAIR עובדת רק על טבלאות hive ולמרות שיש פעולות בספארק נגיד שיכולות לעזור בעדכון כמו add_files לא מומלץ לעשות את זה.
6. איך עושים מחיקה ? אם דרך iceberg - פשוט מוחקים את הרפרנס לdata file בmanifest file, אם עושים מחיקה של רשומה נגיד והטבלה היא מסוג MOR אנחנו כותבים אותו לDELETE FILES ובעת בקשה של הרשומה נסרוק אם הוא שם, בCOW אנחנו נכתוב קובץ חדש לגמרי, הישן יהפוך לחלק מsnapshot ישן עד שהוא יהיה פג תוקף ואז יהפוך לorphan.
7. מהן סטטיסטיקות במטא-דאטה? סטטיסטיקות הן מטא-דאטה שנשמר בmanifest file אודות הdata fildes שמאוחסנים בו, הם מכילים את המזהים של הפרטישנים, כמה קבצים נמחקו\קיימים, מה המינימום ומקסימום עמודות שיכולות להיות, כמה שורות נמחקו\קיימות ועוד...
8. איפה המטא דאטה נשמר בAVRO? בheader של הקובץ .
9. האם הDB צריך לקרוא ולכתוב בREST? אם יש שימוש בREST קטלוג אז כן.
10. מה ההבדל בין REST ללפנות ישירות לJDBC? הREST מספק לנו שירות עם פחות dependencies כי משתמשים בHTTP סטנדרטי, כל כלי שתומך בREST ידע לתקשר איתו לא משנה באיזה שפה והוא תומך בmultitable transactions. נוסף על כך בניגוד לגישה ישירה יש שירות נפרד לAPI והcommits נעשים על צד שרת ולא לקוח מה שעוזר עם התמודדות עם מקביליות ועקביות של לקוחות. JDBC פונה ישירות
11. מתי שינוי בmanifest list ישפיע על metadata file? תמיד , כל שינוי ישפיע כי כל אחד מצריך snapshot חדש.
12.  באקטינג בiceberg ? חלוקה לפי פונקציית hash למספר N באקטסת עוזר עם joins.
13.  איך עובד repartition? אפשר לעדכן קריטריון פרטישן חדש, הישן ישמר ויש מה שנקרא split plan בו מי שיש לו ID של הישן ימשיך להיות בפרטישן הזה וכל מי שחדש יחולק לפרטישן החדש, כדי להתפטר ממנו צריך לעשות rewrite.
14.  איך עושים partition pruning בmetadata file? בעזרת הbuckets וסטטיסטיקות התעלמות מקבצים לא רלוונטים.
15.  האייסברג המשעמם : אימפלמנטציה של קטלוג אייסברג בתוך קובץ JSON 1 שמכיל את הניימספייסס וטבלאות בלי שרת שצריך להקים, בלי API ובלי ענן שיכול להיות בדרכ על S3 או כל אחסון שעובד עם fsspec, בא עם CLI בשם ice


************************* שאלות סקילה 2 ************************************
1. האם סטטיסטיקות זה משהו שאוטומאטית קיים? כן, זה נאסף אוטומאטית בכל פעולת כתיבה, בhive אפשר להפעיל סטטיסטיקות בעזרת פעולת ANALYZE.
2. חסרונות ויתרונות של REST catalog : חסרונות - עלות כספית, אבטחה של השרת, overhead , הקמה וקונפיגורציה מסובכת יותר. יתרונות - מתקשר עם כל כלי שתומך בREST לא משנה באיזה שפה, commits נעשים בצד שרת ולא לקוח וזה עוזר למקביליות ועקביות, תומך בmultitable transactions, פחות dependencied כי יש תקשורת HTTP סטנדרטית, לא מוצמד לאחסון אחד ספציפי.
3. באיזה פורמט נשמר manifest files? פורמט avro.
4. איך עובד access control בiceberg? הקטלוג אחראי על הרשאות, ההרשאות הם לרמת קובץ בהתבסס על שכבת האחסון (הרשאות HDFS/S3/...) ומעל שכבת האחסון יש semantic layer שדואגת להרשאות מבלי שהלקוח יצטרך לדעת איך האחסון עובד (יש שכבות כאלה המסופקות ע"י dremio, trino...) כל קטלוג משתמש בשיטה שונה לטפל בהרשאות, tabular נגיד משתמש בRBAC שהרשאות מחולקות לתפקידים ותפקידים מחולקים לאינדיבידואלים.
5. הבדלים בין גרסאות v2 וv3? גרסה v3 הציגה גישה אפקטיבית יותר למחיקה, בv2 היו יוצרים delete file חדש לכל מחיקה בעוד בv3 מסמנים שורות למחיקה בוקטור מחיקה מה שגורם לקריאות בv3 להיות מהירות יותר, v3 גם מציעה סוגי דאטה טייפ חדשים כמו geography למיקומים גיאוגרפים. בנוסף v3 מאפשר באקטינג לפי מספר עמודות וlineage לעמודות, שני הדברים האלו לא קיימים בv2.
 


