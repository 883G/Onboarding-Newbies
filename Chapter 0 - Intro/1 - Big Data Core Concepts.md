# Introduction to Core Data Concepts :baby:

## **Goals**
- Understand the data landscape and its core concepts.
- Explore the importance of data operations and the role of data in guiding business decisions.
- Gain a comprehensive overview of the data lifecycle and its implications for the organization.

## **Overview**
Today’s session lays the foundation for your journey into data operations. You will examine the core concepts that underpin the modern data landscape and gain insight into data management, processing, and analysis. The emphasis is on appreciating how data drives business decisions and shapes the strategic direction of an organization.

> ⚠️ **Note:**  
> This is your first day in the world of data operations. Don’t worry about diving deeply into every topic; focus on understanding the big picture and the major concepts.

### ⏳ Timeline
Estimated Duration: 1 Day
- Day 1: Spend this day getting acquainted with the world of big data.
    - Hold a Q&A session immediately afterward

## 1. Understanding the Data Landscape

Research the following topics and look for real‑world examples. Discuss your findings with your mentor to deepen your understanding and clarify any questions. Keep a high‑level perspective, and consider the drawbacks of each concept as well as alternatives.

1. **The five V’s of Big Data**

אלו בעצם חמישה עקרונות שמדגישים את הבעיות והאתגרים של 'big data' ובעצם נותנים מסגרת להגדרה הזאת שהיא קצת אבסטרקטית.

VOLUME - כמות המידע שקיימת בפועל. אם כמות המידע גדולה מספיק, זה יכול להיחשב כביג דאטא (מה זה מספיק ? באופן כללי זה לא מוגדר מספיק וזה תלוי בכמות המשאבים, מילים כמו "מספיק", "גדול", "מהיר" כולן יחסיות ולכן תלויות במשאבים, אופי הבעיה וכו') 

VELOCITY - המהירות בה "נוצר" מידע והמהירות שלוקח לו לעבור עד לנקודה הסופית במסלול. בעולמות הביג דאטא יהיה זרם מהיר ורציף של מידע שנרצה לעבד בזמן אמת או כמעט בזמן אמת.

VALUE - הרווח, כלומר מה אנחנו מרוויחים מהמידע בפועל. אם אין לנו דרך להסיק מהמידע מסקנות עסקיות, הוא לא רלוונטי, ולכן "רווח" היא דרישה הכרחית בעולמות הביג דאטא.

VARIETY - המגוון של המידע שנאסף. צריך דרך לשמור את המידע בלי להתחייב לפורמט ספציפי או להנחות קודמות על המידע שמגיע. זה דורש מודלי מידע ואחסון גמישים ומאפשר תובנות חדשות על ידי התבוננות של כמה סוגים שונים של מידע (data types) 
וזה מאתגר את הדרכים הקלאסיות לעיבוד מידע.

VERACITY - מידת הניקיון של המידע, לא כל מה שנכנס מגיע כרצוננו, מתוקנן ובסכימה מתאימה. כאשר מגיע מידע לא טוב נתקלים בבעית 'garbage in, garbage out'  כלומר לר משנה כמה נעבד את המידע, המסקנות לא רלוונטיות במידה ונכנס מידע זבל.
(קצת מזכיר "שקר גורר אמת" מלוגיקה)

2. **Structured, unstructured, and semi‑structured data**

Structured - דאטא שמגיע בפורמט קבוע ולכן הרבה יותר קל לעיבוד למשל טבלאות בדאטא בייסים רלציונים, לכל שורה יש סכמה קבועה שהמידע חייב לעמוד בה.

Semi‑Structured - מידע חצי מובנה כלומר יש תנאים שהוא חייב לעמוד בהם למשל פורמטים כמו JSON וXML

Unstructured - אין התחייבות בכלל על המידע, יכול תיאורטית להגיע כל ייצוג של מידע באמצעות ביטים שצריך לדעת להתמודד איתו

3. **ETL vs. ELT**

שתי מתודולוגיות עיבוד מידע שהשוני ביניהן הוא סדר הפעולות.

E - extract, T - transform, L - load.

בשני המקרים דבר ראשון מחלצים את המידע - מקבלים אותו.
ETL - קודם מבצעים עיבוד מקדים על המידע ואז שומרים את המידע המעובד

ELT - דבר ראשון שומרים את המידע הגולמי, ורק אחר כך, בשליפה, נעבד אותו.

4. **NoSQL vs. SQL databases**

בגדול בגדול, ההבדל בין מידע מובנה למידע חצי מובנה.

SQL - המידע מובנה ואוכף סכימה קשיחה וכפועל יוצא הרבה פחות גמיש ומתבסס על רלציוניות, כלומר joins. מצד שני רלציוניות חוסכת מקום ויש לנו טרנזקציות והסכימה מאפשרת לנו נוחות מקסימלית בתשאול ועיבוד.
כמובן שגם מרוויחים את האפשרות לשימוש בשפה SQL

NoSQL - אין הגדרה לסכימה אחידה וגם אם יש סכימה כלשהי אז היא מאוד גמישה. העובדה שזה לא רלציוני מאפשר לנו סקיילביליות (לרוחב) ביותר קלות. לעומת זאת מפסידים טרנזקציות ושאילתות צריכות להיות יותר ספציפיות כי אקספלורציה הרבה יותר קשה.
וכמובן שאין שימוש בSQL (לפחות לא באותה יעילות כמו על DB רלציוני)
 
5. **OLAP vs. OLTP**

אלו שני דפוסי גישה שונים לדאטא שצריך לקחת בחשבון כשמחליטים על DB.

oltp - online transaction processing - מתמקד בהמון טרנזקציות קצרות ומהירות 

olap - online analytic processing - מתמקד בעיקר בשאילתות כבדות יותר למשל אגרגציות וjoins ומאפטם על שאילתות כאלה.

6. **Batch processing vs. stream processing**

Stream processing - עיבוד של כל הודעה שמגיעה בפני עצמה בזמן אמת. המידע מעובד באופן רציף, הודעה אחר הודעה.

Batch processing - עיבוד של כמות הודעות מסויימת במקביל כיחידה אחת. יכול להיות עיכוב בעיבוד ביחס להודעה בודדת, מצד שני מאפשר עיבוד של יותר הודעות במקביל ועיבודים יותר מורכבים, למשל אגרגציות על כל ההודעות כרגע


7. **Data warehouse vs. data lake**

Data warehouse - מושג כללי (ולא מוגדר כל כך היטב) שמייצג בעצם "מקום" בו שומרים את המון מידע כמה שיותר מהר, כמו שהוא, עם כמה שפחות מניפולציות.

data lake - מאוד דומה, רק שמרשים מניפולציות בסיסיות למשל הבאת המידע לסכימה אחידה או הוספת תגיות וכו'.

שניהם משמשים לstore first והגבול ביניהם לא תמיד ברור

8. **Distributed file systems**

בגדול מערכת קבצים מבוזרת בסקייל גבוהה - הקבצים נשמרים על כמה שרתים באופן שקוף למשתמש, שמבחינתו הכל נמצא באותו מקום.

9. **Data governance**

משילות על המידע - כלומר אחריות של הארגון כלפי המידע שלו. התחייבות על האיכות, אבטחה, פוליסות וכל מה שקשור למידע.

10. **Data visualization**

כמו שזה נשמע - הצגה של המידע בגרפים ותרשימים. מאפשר הסתכלות על המידע ועל איך הוא מתנהג בדרך נוחה נגישה ופשוטה 

11. **Data analytics**



12. **Data ownership**
13. **Data quality**
14. **CDC (Change Data Capture)**
15. **Data catalog**
16. **Data lifecycle management**
17. **Data lineage**
18. **Store‑first approach**
19. **Data serialization**
20. **Data compression**
21. **Scale‑out vs. scale‑up**
22. **High availability**
23. **Master‑slave vs. masterless architectures**
24. **Apache data stack**

These topics are meant to guide your research. Don’t hesitate to look up other relevant concepts.
</br>
> Note✅: Reinforce your understanding by relating the concepts to real‑world scenarios.

## Wrapping Up


### Reflection
Take a few minutes to reflect on what you have learned:
- Write down key takeaways and examples
- Note any questions or uncertainties
- Discuss real-world use cases with your mentor

### Mentor Discussion
Talk through the following with your mentor:
- Clarify concepts that remain unclear
- Share your findings and insights
- Discuss real‑world use cases and implications for your work

## Q&A Session :raising_hand:
Participate in an open Q&A session with your mentor to address any questions about specific tools, technologies, or practices.

## Action Items
- Identify areas you want to explore more deeply.
- Ask for recommended resources for further learning.
