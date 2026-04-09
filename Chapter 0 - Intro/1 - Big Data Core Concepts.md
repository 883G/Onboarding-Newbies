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
 נפח- סך הנתונים שמתקבלים.
 מהירות -קצב המהירות שבו נוצרים, מוזרמים ומעובדים הנתונים.
  מגוון - מתייחס למגוון סוגי הנתונים השונים שעלולים להתקבל
  מהימנות - מידת העיקביות והאמינות של הנתונים שהתקבלו
  ערך- הסקת מסקנות על סמך ניתוח הנתונים
2. **Structured, unstructured, and semi‑structured data**
נתונים מובנים- נתונים בעלי סכמה קבועה ופורמט זהה אשר מוגדרים מראש
נתונים לא מובנים- נתונים שבהם אין סכמה קבועה או פורמט המוגדרים מראש
נתונים חצי מובנים- נתונים בעלי פורמט מוגדר מראש (הסכמה לא קבועה) 
3. **ETL vs. ELT**
ההבדל בין 2 הגישות הללו לניהול וניתוח הנתונים הוא סדר העיבוד בפעולות.
בETL-  קודם כל מחלצים את המידע הגולמי, משנים אותו בהתאם לצורך ולאחר מכן מאחסנים אותו
בELT- קודם כל מחלצים את המידע הגולמי, מאחסנים אותו ורק לאחר מכן מבצעים טרנספורמציה על המידע בהתאם לצורך
בגישה זו ניתן לגשת בכל רגע למידע הגולמי בשונה מETL

4. **NoSQL vs. SQL databases**
SQL DB - מכיל נתונים מובנים בעלי סכמה קבועה ופורמט מוגדרים בתוך טבלאות המכילות שורוות ועמודות
NoSQL- 
יכול להכיל נתונים חצי מובנים בעלי סכמה גמישה הניתנת לשינוי אשר בעלי פורמט מוגדר או נתונים לא מובנים, הנתונים מאוחסנים בשיטת אחסון שאינה טבלאית בהתאם לסוג הנתונים הנקלטים.
5. **OLAP vs. OLTP**
מערכות OLAP - רלוונטיות עבור הסקת מסקנות וניתוח מעמיק על נתונים היסטוריים מצטברים
מערכות OLTP - רלוונטיות עבור מקרים בהם יש צורך לעבד עסקאות בזמן אמת בשביל לשמור על העיקביות והאמינות של המידע
6. **Batch processing vs. stream processing**
Batch processing- עיבוד של כמות גדולה של ההודעות שבבאץ בבת אחת לאחר פרק זמן מסוים
stream processing-(ישר אחרי שההודעה התקבלה) עיבוד של הודעה בזמן אמת 
7. **Data warehouse vs. data lake**
בדאטה וור  האוס מאוחסן מלא מידע מובנה המתקבל ממקורות שונים
מטרת השימוש בשיטת אחסון הזו הינה לאפשר ניתוח מעמיק על המידע והסקת מסקנות יותר בקלות.
 בדאטה לאק מאחסנים כמויות גדולות של מידע גולמי המתקבל ממקורות שונים בפורמט המקורי והגולמי שלו, הדאטה לייק מסוגל לאחסן מגוון נתונים בפורמטים שונים בשונה מדאטה וור האוס. 

8. **Distributed file systems**
מערכת קבצים מבוזרת היא מערכת קבצים המאפשרת לאחסן נתונים על פני שרתים ומיקומים רבים על פני הרשת באופן מבוזר .
בכל מערכת קבצים מבוזרת כלל הקבצים נגישים לצרכן כאילו הם מאוחסנים אצלו באופן מקומי.

9. **Data governance**
שיטה לניהול הנתונים שבה הם מאובטחים , איכותיים וזמינים לאורך מחזור חייהם.

10. **Data visualization**
הצגת הנתונים בצורה ויזואלית אשר ברורה וקלה להבנה.
ניתן להציג ויזואליזציה של נתונים באמצעות מפות , תרשימים, גרפים וכו.

11. **Data analytics**
ניתוח נתונים זהו תהליך אשר מתבצע על מנת להבחין בדפוסים מסויימים, מגמות ובארועים חריגים על מנת שיהיה אפשר להסיק מהנתונים מסקנות ולקבל בזכות כך החלטות שכולות וטובות יותר.
12. **Data ownership**
בעלות על הנתונים מאפשרת לארגונים לקחת אחריות הקשורה לניהול , בקרה ,  והבטחת אבטחת הנתונים בתוך הארגון.

13. **Data quality**
 מדד הבודק כמה מידע של ארגון מסוים עומד בספנדרטים
 על מנת שהוא יחשב למידע איכותי.
 המדד נקבע על סמך : אמינות, דיוק, שלמות, ועקביות המידע.

14. **CDC (Change Data Capture)**
זוהי טכניקה לזיהוי ורישום שינויים בדאטה בס.

15. **Data catalog**
דאטה קטלוג זהו מאגר מרכזי של נתונים המקשר בין המטה דאטה למידע

16. **Data lifecycle management**
זוהי גישה לניהול הנתונים לאורך כל מחזור החיים שלהם- החל מתכנונם ויצירתם עד לעיבודם, אחסונם, ומחיקתם.
ישנם 8 שלבים עיקריים במחזור החיים של הנתונים והם:
1-יצירה : יצירת הנתונים
2- איסוף:איסוף נתונים שרלוונטים
3-אחסון: אחסון הנתונים שנאספו
4-עיבוד: ניקוי, ארגון  והפיכת הנתונים לפורמט שמיש בהתאם לצורך
5-ניהול: שמירה על דיוק הנתונים , אבטחתם ונגישותם.
6-ניתוח: ניתוח הנתונים המעובדים על מנת שנוכל להבחין בדפוסים, חריגויות ותובנות .
7-הצגת הנתונים בצורה ויזואלית (כמו גרפים תרשימים וכו)
8- השמדת הנתונים

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
