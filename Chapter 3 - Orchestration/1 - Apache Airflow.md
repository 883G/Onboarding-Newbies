# Orchestration Fundamentals:
## Overview
This section will go over the fundamentals of _Apache Airflow_, consisting of the client side, and the backend.

**We will focus on general concepts of airflow, the flow of the tasks and how does client code look like.**

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


1. **Airflow User API & Concepts:** Explain the difference between a DAG and a DagRun? How do tasks share small metadata versus global configuration? What is Jinja Templating, and why would you use {{ ds }} instead of Python's datetime.now()? Contrast the TaskFlow SDK with Classic Operators. How does the TaskFlow SDK handle XComs differently than the old xcom_pull method? What are Assets? What types of Operators exist? Why is it not recommended to run any time consuming code in top level dag code? How does this affect the DAG Processor's performance? What is a Hook? what is the connection between Hooks, Connections and Operators?

הapache airflow הוא כלי אורקסטרציה לפיתוח, תזמון וניטור workflows בדגש על batch oriented workflows. הairflow מתנהל בצורה בה כל הworkflow מתנהל כקוד פייתון מה שמאפשר דינאמיות של הDAG, ויכולת להוסיף אקסטנשנים.
הDAG הוא תזרים של צורת הריצה של כל הtaskים, כלומר באיזה סדר ירוצו ומה התלויות שלהם. הDAG ירוץ בגלל טריגר שנשלח או ידנית או דרך API או לפי תזמון שהוא חלק ממנו.
הDagRun הוא סוג של אינסטנס של DAG שרץ בזמן מסויים, הוא נוצר ברגע שמריצים את הDAG וניתן להריץ הרבה ממנו במקביל (כלומר הרבה DAGRUNים במקביל). לDagRun יש תאריך התחלה וסיום ותאריך לוגי שמתאר מתי הוא עתיד לרוץ.
משימות שולחות פרטי מטא-דאטה ביניהן בעזרת XCOMS (cross communications) , זה מופעל ע"י הלקוח, בדיפולט כל משימה היא מבודדת. לכל XCOM יש מפתח וtask_id $ DAG_id והם יכולים להכיל כל אובייקט שעבר serialization אבל בעיקרון הם נועדו לכמויות קטנות של נתונים. את הXCOM עושים דרך הtask context , אי אפשר לעדכן ישירות דרך הDB של XCOM (בדיפולט הDB של איירפלאו). עושעם לXCOMS פוש או פול והם מזכירים משתנים רק שהם פר-משימה וקיימים רק בתוך הDAGRUN.
ומשימות חולקות קונפיגורציות גלובליות בעזרת משתנים גלובלים שכל המשימות יכולות לגשת אליהם. או דרך הAPI/הדאטה בייס החיצוני.
בairflow יש אופרטורים שהם פשוט טמפלט למשימה שמוגדרת מראש שאפשר להגדיר בDAG לדוגמה bashOperator מבצע פקודת bash או pythonOperator יקרא לפונקציית פייתון. זה שונה ממשימה, זה לוגיקה שכבר נכתבה ורק צריכה ארגומנטים. jinja הוא מנוע template שנועד ליצור קוד דינאמי שאפשר למלא בו place holders בעזרת ארגומנטים בהמשך, יכול לשמש לHTML, XML וכו..
הפעולה של {{ ds }} היא jinja templating ומשתמשים בה ולא בdatetime.now() כי זה ביטוי של תאריך לוגי כלומר מה ה"תחום פעולה" מבחינת זמנים של המשימה, לדוגמה אם המשימה נעשית כל יום הdata interval יתחיל ב00:00 והתאריך הלוגי יתחיל כשהאינטרבל יתחיל.
הtaskFlow הוא API שעוזר לשמור על הDAGS קלים ונקיים במקום שימוש באוםרטורים בעזרת דקורטור @task , הוא משתמש בXCOMS שהזכרנו מקודם וככה כשיש taskFlow בDAG , אנחנו לא נבצע פונקציה אלא נקבל את התוצאה כXCOM ונוכל להזרים את זה כאינפוט לחלק הבא. בניגוד למתודה רגילה עם הפוש ופול של XCOMS, פה הXCOM לא נשמר בDB ולא צריך לדחוף או למשוך, התוצאה פשוט מועברת ישירות למשימה הבאה. 


2. **Airflow Backend & Architecture:** What are the different components in the airflow architecture? Define the roles of each component. Why is the Executor considered a mechanism/logic rather than a standalone service? Explain the Deferrable Operator. Which component makes these possible, and how do they save money/resources in a Big Data stack? What are Airflow Providers?

ארכיטקטורת airflow בנויה מכמה רכיבים, הworkflow עצמו מיוצג בעזרת DAG.
הDAG של הworkflow מיוצג בעזרת :
- הtasks
- הtask dependencies
- הscheduler שאחראי לתזמן את כל הworkflow ואת הtaskים הוא משבץ לexecutors ברגע שכל הdependencies שלהם הושלמו, הexecutor הוא configuration property של הscheduler ולא רכיב נפרד. הscheduler עוקב אחריי כל קבצי הDAG ופעם בדקה בודק את כל הparsing כדי לראות אם יש משימה שאפשר להתחיל.
- הcallback שזה פעולות לביצוע כשהworkflow הושלם. הDAG מראה את המשימות ותלותן אחת בשנייה.
- הDAG processor עושה parsing & serialization לקבצי DAG והופך אטתם לדאטה בייס של מטא-דאטה.
- הwebserver.
- פולדר של קבצי DAG שהscheduler קורא כדי להבין איזה משימות להריץ ומתי.
- הדאטה בייס של הקבצי DAG (מטא דאטה) , שומר מצבי טאסקים, DAGים ומשתנים.

  הdefferable operator הוא אופרטור שיכול להשהות את עצמו ולפנות את הworker שהוא עליו למשימה אחרת. הטריגר עושה את ההמתנה שצריך בשביל האופרטור וברגע שהיא הסתיימה הוא שולח לו לחזור לעבוד. בגלל שהעבודה "הועברה" לטריגר אז האופרטור לא תופס את הworker יותר.הטריגרים האלו, הם פיסת קוד קטנה ומתקיימים כולם בפרוסס אחד כחלק מקומפוננט הtriggerer שהזכרנו כחלק מהDAG, לכן הם לא תופסים מקום גדול. זה מונע את הצורך בעוד משאבים שעולים כסף , כח אנחנו מפנים slots במקום לעשות scaling או להישאר בidleness.
  איירפלאו הוא אגנוסטי לחלוטין לגבי מה מריצים במשימות, ניתן להריץ הכל ובעזרת הproviders שהם פשוט חבילות פייתון שמאפשרים לעשות אינטגרציה עם כלים אחרים, כמו דוקר , קוברניטיס, וכו...


3. **Airflow Workflow Synchronization:** How were DAGs typically synchronized to the Scheduler and Workers in Airflow 2? What where the risks with the approach? How was this solved in Airfloe 3? How did it solve the main issue with the Airflow 2 approach? What are the other advantages DagBundles give us?

4. **Airflow Task Lifecycle:** What is the full flow of a dag from being written to being run? What happens when the DAG Processor encounters your file? How is Jinja parsing different in dag processing than execution time? At which state does the Scheduler stop managing the task and hand it over to the Executor? What is the flow when a task gets to a worker? when does it become running?

5. **Airflow Critical Sections:** What is the "Critical Section" of the Scheduler? Describe the three primary "loops" or critical sections (DagRun Creation, Task Instance Creation, Task Scheduling).

### Real-World Context
Rather than focusing on one technology, think about how data workflows are shceduled, and think about when running and ocrhestrating data workflows.

## 🔄 Alternatives

Assignment: You are required to research and write a comparative analysis between Airflow and an industry alternative.

    Deliverable: A written summary (minimum 1 or 2 sentences).
    Focus: Compare performance, architecture, and specific "pain points" this tool solves compared to legacy systems or competitors.
    Goal: You must be able to justify why the department uses this tool for our specific environment.

## 🎯 User Story & Scenario

Assignment: Based on your research and understanding of the department's pipeline, define a concrete Use Case for this technology.

    Deliverable: A written summary example/story (two sentences approx.).
    Requirement: Describe a real-world scenario (e.g., a specific client requirement) where this technology is the optimal solution.
    Data Flow: Map out the data flow and explain how this tool integrates with other components in the Data Pipeline.


## Wrapping Up :trophy:
Discuss your answers and any areas of confusion with your mentor. Reflect on how these general concepts will help when you later when using scheduled jobs.

## Additional Topics from Review
- A deep dive into the Airlfow database and the inner workings of Airflow.
- A deep dive into bugs solved and unsolved inside Airflow.

## Action Items
- Review your notes and identify topics you want to explore deeper.
- Collect a list of real-world schedulers and their algorithms.
- Prepare questions for the upcoming mentor Q&A session.

## Recommemded Resources
- [Airflow Docs](https://airflow.apache.org/docs/)
