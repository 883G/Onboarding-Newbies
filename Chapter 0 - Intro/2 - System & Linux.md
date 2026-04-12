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

## Answers
1.
 הקרנל הוא בעצם ליבת מערכת ההפעלה, כלומר החלק במערכת ההפעלה שיש לו גישה בלעדית לרכיבים הפיזים במחשב והוא בעצם מהווה ממשק בין כלל מערכת ההפעלה לחומרה הפיזית.
 הפרדה בין הuser space ל kernel space עוזרת באבטחה על ידי הרשאות גישה, למשל שתהליך יוכל לגשת רק לזיכרון שהוקצה לו.
 ובאותו אופן תכנית שנופלת בuser mode לא תפיל את כל מערכת ההפעלה בגלל הבידוד הזה.

 2. 
 כל תהליך נוצר מתהליך אב כלשהו למעט הראשון - איניט שיש לו PID = 1.
 כאשר תהליך נוצר הוא מגיע לready queue ובעצם מחכה שמערכת ההפעלה תתן לו מעבד.
 כאשר הוא מקבל מעבד הוא מגיע לstate running.
 בעת בקשות קלט/פלט הוא יוצא למצב שנקרא waiting ומחכה שוב לזמן מעבד כדי להשלים את התהליך.
 כך עד שהתהליך סיים או שנעצר באמצעות סיגנל.

 ניתן לנטר על משאבים של תהליך באמצעות פקודת Htop או vmstat 
 אפשר להפסיק תהליך באמצעות פקודת Kill

 3. 
 inode - מעין מבנה נתונים שמתאר אובייקט במערכת קבצים. כל קובץ מקבל אינדקס ייחודי. כל inode מכיל את הכתובת של הקובץ על הדיסק 

 חיבור דיסק חדש יראה כך: מחברים את הדיסק למחשב ומשתמשים בפקודה lsblk כדי לראות שהוא אכן חובר.
 לאחר מכן מפרטשים את הדיסק באמצעות fdisk.
 אחר כך יוצרים מערכת קבצים על הדיסק.
 ולבסוף עושים mount לתיקייה לוקאלית
 כדי שזה יישמר לאחר ריבוט, צריך להוסיף ל/etc/fstab
 כמה שורות.

 4. 
 daemon - תוכנה שרצה ברקע ללא תלות בחיבור של יוזר ספציפי ומטרתה לספק איזשהו שירות ה"אב" שלהם הוא הפרוסס איניט אבל ניתן ליצור כאלה ידנית. ההבדל העיקרי הוא ש daemons לא צריכים את המשתמש בכלל לעומת תהליך רגיל שצריך איזשהי אינטרקציה, אפילו הכי בסיסית שיש עם המשתמש.

 כדי לראות לאיזה פורטים התהליך מאזין נשתמש בפקודה 
 sudo lsof -i -a -p "pid"

 ונבדוק האם הוא פתוח או בעזרת ss -ltup על אותה מכונה, או באמצעות nmap "ip" ממכונה אחרת (או nc) 

 5. 
SWAP SPACE - זה מקום על הדיסק שמשתמשים בו כשהראם הפיזי מלא. כשהראם מלא דפים שלא בשימוש מוזזים מהראם ל swap space

המטרה של קונטיינרים היא לגרום לאפליקציה שרצה בו להרגיש כאילו היא היחידה שרצה על מערכת ההפעלה. כדי לבצע את זה קונטיינרים משתמשים ב namespace כדי לבודד תהליכים, למשל כאשר מריצים קונטיינר, נוצר לו ניימספייסים שונים שבהם הוא רץ ורק אליהם יש לו גישה כמו PID, network, filesystem.
ונוצר גם cgroup שמטרתו היא בעצם להגביל את המשאבים של הקבוצה הזו


 

## Wrapping Up :trophy:
Discuss the topics with your mentor and make sure you can describe each one at a basic level.  Don’t worry about memorizing commands—focus on understanding what the topics are and why they matter.
