# Orchestration Fundamentals:
## Overview
This section will go over the fundamentals of _orchestration_, consisting of _scheduling_ and _resource management_.

**We will focus on general concepts such as scheduling algorithms, preemptive vs non-preemptive scheduling and prioritization.**

## Goals
- Develop a foundational understanding of how scheduling is done.
- Learn the common terminology used by most schedulers.
- Practice planning a self-study day and estimating time for learning.

:warning: **Note:**
- This is a self-study day. Independence and time management are essential.
- Many newcomers struggle with self-study; take a moment to plan your day and stick to it.
- Understand the **big picture** of each concept. If you can't explain it, you probably haven't learned it.
- Be prepared to describe how concepts relate to one another and to real-world scenarios.
- When in doubt about what you need to learn, ask your mentor.

### Core Concepts

Think through the following questions; by answering them you’ll touch every major topic listed above:

1. **Scheduling Basics:** Why can’t we just use a simple sleep() command or a basic cron job to manage a modern data workflows? What is the difference between a Time-based trigger and an Event-based trigger? Give a real-world data example for each, In general scheduling, why do we use a DAG to represent a workflow instead of just a simple list of instructions?

הפקודות של sleep() והcron job טובות לתזמון של פקודות פשוטות, אבל ברגע שמדברים על זרימת נתונים מודרנים, בעיקר בביג דאטה, צריך התייחסות לscalability,fault tolerance, מקביליות, שגיאות ועוד דברים שלsleep / cron job אין את היכולת להתמודד עם בעיות מורכבות כאלו.
נסתכל לדוגמה על cron job בסיסי - כל המשימות המתוזמנות תלויות בשרת אחד, אם השרת קורס , כל המשימות עוצרות כלומר אין HA - דבר שחשוב מאוד בתזמון של נתונים בביג דאטה.
כשמדברים על sleep() הפער הוא עוד יותר גדול, בגלל שהדבר היחיד שהוא דואג לו זה השהיית הthread לזמן מסויים - אין התייחסות בפקודה הזאת לשום דבר מעבר.
מעבר לכך, sleep() וcron jobs הם מונעים רק ע"י טריגר זמן , אין להם מודעות לאירועים סביבתיים והם לא יכולים לקרוא לworkflow מסויים בגלל אירוע שקרה.
בשביל תזמון של נתונים בביג דאטה צריך לנהל תזמונים במקביל על גבי שרתים שונים, ולהתייחס לכמות ענקית של נתונים.
תזמון של משימה יכול להיות event-based triggered או time-based triggered:
- בevent based הworkflow יתחיל בגלל אירוע כלשהו שקרה במערכת לדוגמה, התווסף קובץ חדש ועכשיו צריך לקרוא לשרשרת פעולות או נשלחה שאילתה לטרינו ועכשיו יש סט פעולות שצריכות להתקיים.
- בtime based triggers הworkflow יתחיל בגלל שהוא תוזמן לזמן הזה, לדוגמה דחיסת קבצים קטנים פעם בכמה שעות.
אנחנו מייצגים את הworkflow בעזרת DAG כי הוא נותן לנו לייצג גם מקביליות, תלות של הוראה בכמה הוראות אחרות או להפך אי תלות של הוראות אחת בשנייה בעוד שברשימה של הוראות כל הוראה תלויה בכל הקודמות לה - אין מקביליות. כשמייצגים הוראות גם בצורה מקבילית ולא תלותית בכל מי שלפנייה זה עוזר עם fault tolerance, ברגע שהוראה תיכשל לא צריך להריץ את כל הרשימה מחדש. 


2. **Scheduling Algorithms & Types:** Compare First-In-First-Out (FIFO) and Shortest Job First (SJF), how do they handle varying workflows? Define Preemptive vs. Non-preemptive scheduling, If a "Critical" job enters the queue while a "Low" priority job is already running, what happens in both scenarios? What is "Starvation" in priority scheduling, and how does the concept of Aging fix it? what are other common algorithms to fix starvation?

אלגוריתמים לתזמון משימות:
- הFIFO - האלגוריתם הכי פשוט, המשימה הכי ראשונה בתור רצה עד שהסתיימה (כלומר היא מקבלת את המשאבים). זה מבטיח שיגיעו לכל המשימות אבל בעייתי כי יכול להיות שיש משימה גדולה יחסית בתחילת התור ש"תתקע" משימות קצרות שאפשר לבצע מהר.
- הSJF - מריץ את המשימה עם הזמן הכי קצר קודם, מצד אחד יגיע אל משימות אחרות בזמן מהיר יותר, מצד שני יכול לגרום להרעבה (כלומר אם ניכנסות הרבה משימות בזמן קצר יחסית או יותר קצר ממשימה ספציפית, יכול להיות שלא נגיע למשימה הזאת). מתחלק לשני סוגים : הפרימיטיבי (נקרא גם STRF) שאומר שברגע שהגיע משימה קצרה יותר נחדול את המשימה הקיימת ונחליף אותה (עלול לגרום לoverhead מרובה) ולא פרימיטיבי שאומר שאם הגיעה משימה קצרה יותר היא תהיה בראש התור אבל תחכה לסוף הריצה.
  בpriority scheduling שבו לכל משימה יש ערך עדיפות, יש גם את עיקרון הפרימיטיבי\לא פרימיטיבי (עובד אותו דבר), וגם שם יכולה לקרות הרעבה לתהליך עם ערך עדיפות נמוך, במקרה הזה משתמשים בaging שבו אחריי כמות זמן מסויימת שתהליך מחכה לרוץ מעלים את העדיפות שלו.
  אלגוריתמים אחרים להתמודד עם הרעבה:
  - הRR (round robin) : רצים על תהליך אינטרבל מסויים של זמן ואז עוברים לתהליך הבא בתור, אם התהליך הראשון לא הסתיים נחזיר אותו לסוף התור (או לתור משני). 

3. **Scheduling & Priorities:** Explain the difference between Pessimistic Scheduling (Priority Blocking) and Optimistic Scheduling (Resource Maximization), If a "High Priority" job needs 100 CPUs but only 80 are available, how does a Pessimistic scheduler treat the remaining 20 "Low Priority" jobs in the queue compared to an Optimistic one? How do Resource Pools (or Slots/Concurrency limits) help a scheduler "sandbox" different types of work?

בpriority blocking משימות עם עדיפות גבוהה יותר הן הראשונות לרוץ, זה אלגוריתם פרימיטיבי, לעומת זאת בresource maximization משימות שמתאימות למשאבים הקיימים ירוצו קודם. לדוגמה עבור משימה בעדיפות גבוהה שמבקשת יותר משאבים מהנדרש ואחרייה יש 20 משימות בעדיפות נמוכה יותר, הpessimistic scheduler יעשה block לשאר המשימות ויחכה לעוד משאבים כדי לא להרוס את העדיפות. לעומת זאת האופטימיסטי יתן למשימות בעדיפות קטנה יותר לרוץ על המשאבים כדי לנצל אותם.
במקרה שיש כמה workloads , הresource pools מגדירים להם קבוצות משאבים נפרדות , הוא מחלק את כל המשאבים הנגישים לסוג של פרטישנים. ככה מוודאים שלכל תהליך יש את המשאבים שלו ואין אחד ש"אוכל" את כל המשאבים לדוגמה. בשביל לא לנסות לנצל יותר משאבים ממה שיש הresource pool  מגבילה את התהליכים במקביל שניתן לעשות.
הslots בhadoop לדוגמה הם יחידות שעליהם ירוץ job והן מבטיחות שלא יפריע לו job אחר ושהמשאבים מספיקים לו.
אפשר לנטב סוגי עבודות שונים לסוגים אחרים של משאבים. לדוגמה למערכות שיותר מסובכות חישובית (נגיד עיבוד סרטונים) נצטרך יותר CPU ולמערכות שיותר מסובכות מבחינת זיכרון נצטרך יותר MEMORY.
הairflow לדוגמה משבץ את הslots עם tasks.
הresource pools יכולות להיות VM pools, storage pools ועוד.
יש לו הזמנות , הגבלות , ושיתופים.
הזמנות - מה אנחנו מבטיחים לPOOL, המינימום.
הגבול - מה המקסימום של הPOOL.
שיתופים - הPOOLS יקבלו עוד משאבים בהתאם לעדיפות שלהם.

4. **Resource Allocation & Scheduling:**Explain Dominant Resource Fairness (DRF). Why is it more "fair" to look at CPU and RAM usage rather than just task count? What is Capacity Scheduling, and how does it provide "guaranteed lanes" for different departments? Compare Static Allocation to Dynamic Allocation. Which one is safer for the system, and which one is more efficient for the cluster?

הDRF הוא כלל שמטרתו ליצור חלוקת משאביפ פיירית בין תהליכים שמבקשים כמות משאבים שונה. הוא פועל לפי עיקרון min-max שאומר למקסם את המספר המינימלי של משאבים שאפשר לתת ליוזר.
לכל יוזר יש טאסקים עם דרישות לכל טאסק, כמות המשימות שהוא יכול לבצע בהינתן משאבים מסויימים זה הutility שלו.
בDRF מסתכלים על המשאבים יותר מעל מספר המשימות בגלל שבצורה הזאת מתחשבים בצורך של כל היוזרים, ואם יוזר 1 הוא כבד מאוד מבחינת CPU ויוזר 2 כבד מבחינת זיכרון , הDRF ידע לחלק להם יחס של זיכרון וCPU שצריך.
הcapacity scheduling זה שיטה להקצאת משאבים בהתאם למה באמת פנוי , מבלי לתת יותר ממה שקיים. אם אין למשאב יכולת - יעשו תזמון למאוחר יותר. הוא שומר guaranteed lanes בגלל שהוא שומר slots שמורים מראש למשימות שמספקים את הדרישות שלהם.
הקצאה סטטית - מקצה בזמן קומפילציה לסטאק, קל ופשוט
הקצאה דינאמית - להיפ בזמן ריצה, מאפשר לשנות הקצאה.
סטטית בטוחה יותר כי אין בה חשש לleaks, אבל דינאמית יותר יעילה לקלאסטר כי היא נמנעת מבזבוז משאבים.


5. **Users Perspective:** Why is Idempotency the most important concept for a developer to understand when writing scheduled jobs? what is an Exponential Backoff when jobs fail? What is Backfilling, and how does it relate to the "Optimistic" approach of keeping resources busy?

הIdempotency הוא עיקרון שבודק שמשימה שרצה כמה פעמים מפיקה את אותו תוצאה כמו בפעם אחת שרצה. זה חשוב כי זה עלול לגרום לאי יציבות במערכת לדוגמה, משימה שהופרעה באמצע אבל עדיין בוצע חיוב ללקוח- אם היא תרוץ שוב ואין Idempotency היא עלולה לבצע חיוב כפול. Idempotency משתמש במפתחות לזיהוי תהליכים שעובדו לקאש ובודק שאין להם תלות במצבם הקודם, דואג לפעולות אטומיות ובודק לפני שהוא מבצע.
הExponential Backoff הוא אסטרטגיה לניהול retry בעקבות כשל בjob מסויים בו מחקים זמן מסויים במקום לנסות שוב ישר. בדרך כלל אחריי כל כשל מכפילים את זמן ההמתנה. זה כדי למנוע עומס על שרת שיכול להיות "בהלם" ובגלל זה הג'וב לא עבד, כשיש זמן מקסימלי להמתנה ומספר מקסימלי של נסיונות חוזרים.
הBackfilling זה אסטרטגיה לניצול משאבים (אופטימיסטי) בו מאפשרים לג'ובים עם דרישות קטנות יותר לרוץ גם אם העדיפות שלהם לא עליונה. בBackfilling יש "הזמנות" והמשימות הקטנות צריכות לסיים את ההרצה שלהן לפני שהמשימות עם הזמנה מוכנות לרוץ (כשיש משאבים). בeasy Backfilling רק למשימה הראשונה יש הזמנה, ובconservative יש לכולם.

### Real-World Context
Rather than focusing on one technology, think about how these ideas show up in schedulers, such as the linux scheduler or the trino task scheduler.

בטרינו יש בcoordinator רכיב של מתזמן שהוא אחראי על התכנון הפיזי, הוא עושה hased scheduling, מנסה לפרוס splits כמה שיותר אבל לשמור על לוקליות ולהתחשב במרחקים ביניהם.
המתזמן של לינוקס הוא רכיב בקרנל, הוא מנהל schedualing classes שזה היררכיה לפי פריוריטי.
ספארק בדיפולט עובד בפיפו אבל יש fair scheduler שעובד בסגנון RR

## Wrapping Up :trophy:
Discuss your answers and any areas of confusion with your mentor. Reflect on how these general concepts will help when you later when using scheduled jobs.
***************** שאלת סקילה ********************************
1. איזה עוד סוגים של משאבים הresource pools מקצות? מלבד CPU,RAM וחיבורים במקביל, הם יכולות להקצות הגבלה לI/O בזמן מסויים, ועדיפויות לתהליכים.
## Additional Topics from Review
- A deep dive into sheduling algorithms.
- What are the different obsolescence algorithms widely used? where could they also be implemented? what are some scheduling algorithms without preemption and aging that solve starvation?

## Action Items
- Review your notes and identify topics you want to explore deeper.
- Collect a list of real-world schedulers and their algorithms.
- Prepare questions for the upcoming mentor Q&A session.

## Recommemded Resources
- [Priority Scheduling Slurm](https://slurm.schedmd.com/priority_multifactor.html)
- [Operating Systems Scheduling Stanford University](https://web.stanford.edu/~ouster/cgi-bin/cs140-spring14/lecture.php?topic=scheduling)
