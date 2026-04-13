# System, Linux & Security Fundamentals :computer:

## **Topics Covered**
- Linux directory hierarchy (`/`, `/etc`, `/var`, `/proc`, etc.)
- Process model and scheduling
- Kernel I/O path and page cache
- Authentication vs. authorization; Kerberos, LDAP, SSSD
- Basic shell usage and GNU utilities
- User/group management and service control (`systemd`)
  - *Other init systems*: initd, OpenRC, runit, etc. (historical/alternative)

> ⚠️ **Note:**
> This chapter is a roadmap, not a lesson.  You’ll enter the mock course we’ve prepared with your mentor’s help and work through it together.  Ask your mentor for guidance before diving into any of the material.

### ⏳ Timeline
Estimated Duration: 1 Day
- Day 1: Spent this day as your mentor instructs you;
    - Have a Q&A session right after

## Overview
These are the high‑level areas you should be familiar with when starting on our platform.  The actual content will be explored during the mock training session with your mentor; use the list above as a checklist.

> Note: while some environment uses `systemd` for service management, other init systems like **initd**, **OpenRC**, and **runit** exist and may be encountered in alternative distributions. Understanding the basic concept of an init system is more important than knowing the specific implementation.

## Wrapping Up :trophy:
Discuss the topics with your mentor and make sure you can describe each one at a basic level.  Don’t worry about memorizing commands—focus on understanding what the topics are and why they matter.



1.תפקיד הקרנל הוא לקשר בין החומרה לתוכנה, לנהל את התהליכים ביעילות ולתקשר עם האפליקציות המקושרות אליו.
הקרנל פועל בדרגת ההרשאשה הגבוהה ביותר ובעל השפעה רבה על ביצועי המערכת, כל שגיאה הכי קטנה שמתבצעת בקרנל עלולה לגרום להשלכות רבות במערכת ואפילו עשויה לגרום לה לקרוס לגמרי.
בשל כך יש את היוזר ספייס, שהוא פועל בדרגת הרשאה נמוכה יותר מהקרנל (יש בו גישה מוגבלת ומבוקרת על ידי הקרנל) ואין ביכולתו לגשת ישירות לחומרה.

2.-1לאחר שרץ תהליך הוא יכול להגיע למצב "שינה", זה יכול לקרות עקב כך ש-התהליך מחכה למצב מסוים שיקרה על מנת שיוכל להמשיך את הרצתו, או שהתהליך לא מגיב.
תהליך שרץ יכול להיכנס גם למצב "סטופ", זה קורה כאשר הפרוסס עוצר את הרצתו או כאשר מדבגים אותו.
בנוסף תהליך יכול גם להיכנס למצב "זומבי", במצב זה התהליך עושה שימוש במשאבים אך אין דרך לתקשר איתו.

2-באמצעות הרצת הפקודה top בטרמינל נראה את כל התהליכים שעכשיו רצים במערכת.
כחלק מפלט הפקודה נראה עבור כל תהליך רץ כמה הוא מנצל את המעבד ואת הראמ.
 כאשר מבחינים בתהליך שצורך כמות חריגה של משאבים ניתן להפסיק את הרצתו באמצעות הרצת הפקודה kill עבור התהליך.

3. 1-איינוד הוא מבנה נתונים המשמש לניהול מידע על הקבצים השונים במערכת הקבצים.
לכל קובץ במערכת קבצים לינוקס יש אינוד יחודי לו שהוא מכיל את המטא דאטה של הקובץ (מאפייני הקובץ) ואת כתובות הזיכרון של הבלוקים בדיסק שבהם מאוחסן התוכן של אותו הקובץ.

  2-לאחר חיבור הדיסק מערכת ההפעלה תזהה איזה מחיצות (פרטישנים) יש על הדיסק.
לאחר מכן, בשביל שהמחיצות יימופו עם עליית מערכת ההפעלה אוטומטית נשתמש בקובץ etc/fstab/ שמחזיק את הפקודות למיפויים הנדרשים. כל פקודה בקובץ תכיל את מזהה הדיסק, השם של המיפוי (mount point), ואת סוג מערכת הקבצים באותה מחיצה.

4. תהליך מסוג דימון הוא תהליך רקע אשר רץ באופן עצמאי ללא שום אינטראקציה עם המשתמש בשונה מתהליך רגיל (שאותו המשתמש מריץ).
כדי לבדוק אם שירות רשת מסויים רץ קודם כל נבדוק האם שירות הרשת אליו רוצים לגשת קיים באמצעות הרצת הפקודה systemctl status. אם הוא אכן קיים נבדוק האם הוא מאזין בפורט הנכון באמצעות הרצת הפקודה netstat. לבסוף נבדוק האם שירות הרשת נגיש ממחשב מרוחק באמצעות השימוש בפקודת netcat או telnet.

5. 1-סוואפ זהו קובץ אשר מחקה את זיכרון הראם ומאפשר למחשב להמשיך לעבוד כאשר מגיעים למצב שבו נגמר למחשב זיכרון הראם.
שהמחשב מגיע למצב בו זיכרון הראם מנוצל כולו, הוא יכתוב את המידע לקובץ הסוואפ וימנע מהמחשב להיות תקוע באופן מוחלט.

2-הנאימספיסס מאפשרים את קיום הסביבות המבודדות במערכת ההפעלה, ובזכות כך כל קונטינר יכול לרוץ בסביבה מבודדת לו ולעשות שימוש רק במשאבים המוקצים לו.
הסיגרופס תומך בניהול הקצאת המשאבים במערכת ההפעלה , ובזכות כך כל קונטינר יכול לראות את כמות המשאבים המוקצאת רק לו.
בעת הקמת הקונטינר נוצרים הנאימספיסס והסיגרופס אשר ישמשו את הקונטינר בפנייה למשאבים שהוקצו לו .


