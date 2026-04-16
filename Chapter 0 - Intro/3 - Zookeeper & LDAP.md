# Zookeeper, Kerberos & LDAP :lock:

## Overview
This session focuses on the components that provide coordination and authentication in distributed systems.  Zookeeper acts as the lightweight coordination service, while Kerberos and LDAP handle secure identities and directory information.  These technologies are commonly paired in Hadoop and other big‑data ecosystems.

**Study the key components, design decisions, and how they work together to enable secure, reliable clusters.**

## Goals
- Learn Zookeeper’s architecture and core features.
- Understand the Kerberos authentication flow and the purpose of LDAP directories.
- See how these systems integrate with each other and with Hadoop.
- Practice organizing a self‑study day and managing your time.
- Prepare to discuss your findings with your mentor.

:warning: **Note:**
- This is a self‑study session; independence and time management are critical.
- Focus on grasping the full picture of each concept – if you can’t explain it, you haven’t learned it.
- When in doubt, ask your mentor which topics deserve deeper attention.

### ⏳ Timeline
Estimated Duration: 1 Day
- Day 1: Spent no more than third a day on each of the following: LDAP, ZOOKEEPER,Kerberos, Hint read a bit about Active Directory As well;
    - Have a Q&A session right after

## Core Concepts

### Zookeeper – five guiding questions
1. **Architecture & Data Model:**  Describe a Zookeeper ensemble, the role of the leader and followers, the znode hierarchy, and how znodes store data and metadata.
2. **Consistency & Watches:**  How does Zookeeper guarantee sequential consistency?  Explain watches, one‑time triggers, and how clients use them for cache invalidation.
3. **Sessions & Failure Handling:**  What is a Zookeeper session, how are heartbeats maintained, and what happens when the session expires?  Discuss how ephemeral and sequential nodes relate to this.
4. **Common Patterns:**  Explain how leader election, distributed locks, and configuration storage are implemented on top of Zookeeper primitives.
5. **Operational Concerns:**  Outline how to deploy an ensemble, handle scaling, manage snapshots and transaction logs, and troubleshoot typical issues (e.g., split‑brain, latency).

### Kerberos – five guiding questions
1. **Protocol Flow:**  Walk through the Kerberos authentication flow from initial login (kinit) to obtaining service tickets.  Include AS, TGS, and ticket caches.
2. **Key Concepts:**  Define principals, realms, KDC components, tickets (TGT vs service ticket), and how encryption keys are derived and used.
3. **Security Properties:**  Why is Kerberos considered secure?  Discuss mutual authentication, replay protection, time sensitivity, and the role of the ticket lifetime.
4. **Administration & Tools:**  What are common Kerberos administration tasks?  Describe commands like `kadmin`, `kinit`, `klist`, `kdestroy`, and how to add principals or change passwords.
5. **Integration & Troubleshooting:**  How do services (Hadoop, HTTP, SSH) integrate with Kerberos?  What are typical issues (clock skew, wrong realm, keytab problems) and how do you diagnose them?

### LDAP – five guiding questions
1. **Directory Structure:**  Explain how LDAP organizes information in a hierarchical tree (DN, RDN), common object classes, and attributes for users and services.
2. **Protocols & Operations:**  Describe basic LDAP operations – bind, search, modify, add, delete – and the difference between simple and SASL binds.
3. **Schema & Extensibility:**  What is an LDAP schema?  How do object classes, attribute types, and syntax rules define what data can be stored?  Mention extending schemas.
4. **Authentication & Authorization:**  How is LDAP used for authentication and authorization?  Cover binding with credentials, password policies, and group lookups.
5. **Deployment & Security:**  Outline how to install/configure an LDAP server (e.g., OpenLDAP), secure it with TLS, replicate data, and troubleshoot common errors (referral loops, access controls).

### 🔄 Alternatives
Assignment: You are required to research and write a comparative analysis between Zookeeper, Kerberos & LDAP and an industry alternative.
- Deliverable: A written summary (minimum 1 or 2 sentences).
- Focus: Compare performance, architecture, and specific "pain points" this tool solves compared to legacy systems or competitors.
- Goal: You must be able to justify why the department uses this tool for our specific environment.

### 🎯 User Story & Scenario
Assignment: Based on your research and understanding of the department's pipeline, define a concrete Use Case for this technology.
- Deliverable: A written summary example/story (two paragraphs approx.).
- Requirement: Describe a real-world scenario (e.g., a specific client requirement) where this technology is the optimal solution.
- Data Flow: Map out the data flow and explain how this tool integrates with other components in the Data Pipeline.

## Wrapping Up :trophy:
Review your answers with your mentor and discuss any unclear points.  Relate each concept back to actual deployments you might encounter.

## Action Items
- Note topics you want to investigate further.
- Prepare questions for the mentor Q&A session.
- Document any commands or configuration steps you used during research.

Zookeeper, Kerberos & LDAP 

Zookeeper – five guiding questions
Architecture & Data Model: Describe a Zookeeper ensemble, the role of the leader and followers, the znode hierarchy, and how znodes store data and metadata.
1-ארכיטקטורת הזוקיפר מורכבת מהירכיה של צמתים הנקראים "znodes" והיא מאורגנת בצורת עץ.
כל znode מאחסן בתוכו נתונים ורשימת Access Control List (רשימה שמגבילה את הגישה לביצוע פעולות מסוימות).
קיימים 2 סוגי znodes, סוג אחד הוא ephemeral שהוא נעלם כאשר הסשן שיצר אותו הסתיים והשני הוא persistent, שהוא נשאר עד שמוחקים אותו.
בראש הירכיית ה-ensemble ממוקם הleader znode שהוא znode הבסיס.
 כל שאר הצמתים האחרים הם למעשה צאצאיו והם קרויים followers ועוקבים אחר הוראות הleader znode .
תפקיד הleader הוא לשמור על עקביות הנתונים בנודים שבקלסטר וגם לבצע בו את פעולות הכתיבה המתקבלות באופן תקין (שהנודים יהיו מסונכרנים, מדויקים, ועקביים כמה שיותר).
כל פעולות הכתיבה שמתבצעות לznodes השונים עוברות דרך הleader znode, והוא דואג לעדכן בכך את הfollowers, ולאחר שמרבית הצמתים אישרו את פעולות הכתיבה, הוא מבצע אותן.
תפקיד הfollowers הוא להיות משוכפלים בהתאם לleader ולבצע בקשות קריאה.
הznode מסוגל לאחסן מידע במערך בתים .
לכל znode  יש מבנה נתונים ששמו stat ובו מאוכסן metadata (רשימת ACL, צמתי הצאצאים של אותו הznode וכו…) של אותו הznode.
יש 4 סוגים שונים של znodes.
Persistent nodes- נוד שקיים תמיד, עד לרגע בו הוא ימחק רשמית (הוא לא נמחק לאחר שהסשן נגמר)
Persistent Sequential Node- נוד שהוא פרסיסטנט שזוקיפר מצוות לו מספר שעולה כל פעם שנוצרים עוד נודים מסוג זה בסיומת השם שלו לאחר יצירתו
Temporary Node- נוד שקיים עד לרגע שבו הסשן מסתיים
Temporary Temporary Node -שזוקיפר מצוות לו מספר שעולה כל פעם שנוצרים עוד נודים מסוג זה בסיומת השם שלו לאחר יצירתו Temporary נוד מסוג  


Consistency & Watches: How does Zookeeper guarantee sequential consistency? Explain watches, one‑time triggers, and how clients use them for cache invalidation.
הzookeeper מבטיח עקביות בשל כך שכל פעולות הכתיבה שמתבצעות עוברות דרך הleader znode והוא מעדכן בכך את שאר הfollowers ורק לאחר שרב הfoloowers אישרו את ביצוע פעולות הכתיבה הן מתבצעות.
בzookeeper יש פיטר שנקרא Watches שהוא שהוא מנגנון שמתריאה על שינויים שהתרחשו בznode.  המשתמש יכול להגיד מעקב אחר znode  וכל פעם שיוחל בו שינוי הוא יקבל עדכון על כך ישר, דבר המאפשר לצרכן להגיב באופן מיידי לשינויים שבוצעו . 




Sessions & Failure Handling: What is a Zookeeper session, how are heartbeats maintained, and what happens when the session expires? Discuss how ephemeral and sequential nodes relate to this.
סשן זה מהלך התקשורת בין הלקוח ל-ensemble.
הסשן מתחיל מהרגע בו הלקוח מתחבר לשרת מסוים בensemble ומסתיים לאחר שהלקוח מתנתק ממנו או לאחר שהלקוח לא תקשר עם השרת פרק זמן מסוים שמוגדר אשר נקרא session timeout.
כאשר הסשן מסתיים ה-ephemeral nodes נמחקים וה-sequential nodes נמחקים אם הם זמניים וישארו אם הם קבועים.  


Common Patterns: Explain how leader election, distributed locks, and configuration storage are implemented on top of Zookeeper primitives.
תהליך בחירת הleader נעשה על ידי אלגוריתם ששמו ZAB, האלגוריתם בוחר בznode העדכני ביותר כleader.
ה- distributed locks מיושמים בצורה כזאת שהם מבטיחים שרק לקוח אחד יכול לפעול במשאב מסוים בכל פעם ובכך מונעים מצב שבו כמה לקוחות יעדכנו או יקראו את אותם הנתונים במקביל ויהיה סכנה לפגיעת שלמות, דיוק ועקביות הנתונים.
דיסטרביוטד לוק מבוסס על Temporary Sequential Node. 
כאשר כמה לקוחות נעילה באותו הזמן, נוצרים כמה emporary Sequential Nodes ברצף תחת הlocks node.
הנוד עם הsequence number הכי קטן הוא זה שיכול לבצע את הנעילה, והנודים האחרים יעקבו אחר השינויים המתבצעים על ידי הנוד שמבצע את הנעילה.
לאחר שהנוד שביצע את הנעילה שחרר אותה הנוד ימחק והנוד הבא עם הסיקוונס נאמבר הקטן ביותר הוא זה שיבצע את הנעילה.

אפשר בזוקיפר להוסיף נפח לאחסון הנתונים באמצעות הוספת Persistent Volumes לקלסטר.

Operational Concerns: Outline how to deploy an ensemble, handle scaling, manage snapshots and transaction logs, and troubleshoot typical issues (e.g., split‑brain, latency).

כדי לפרוס אסמבל יש לבצע את השלבים הבאים:
-להתקין JDK (ערכה לפיתוח תוכנה של java)
-להגדיר את גודל הheap המוקצה לjava
-להתקין את חבילת השרת של זוקיפר.
-ליצור קובץ קונפיגורציה שבאמצעותו מקשרים לאסמבל את הznodes.
כדי לפרוס אסמבל הוא חייב לכלול 3 znodes לפחות.

על מנת לשפר ביצועי המערכת או להגדיל את הקצאת האחסון שלה ניתן או להוסיף עוד שרתים לאסמבל או להגדיל את גודל המשאבים הקיימים בו.

זוקיפר שומר תיעודים של הטרנזקציות שהתבצעו בsnapshots ו בtransaction log 
ב-transaction log נרשם מספר הטרנזקציות שהתבצעו לפני שהיה אפשר לבצע snapshots 
הזוקיפר לא מוחק snapshots וlog files כברירת מחדל, על הלקוח לעשות זאת.

split brain-
באמצעות השימוש ב-quorum ניתן להגדיר את כמות השרתים המינימלית באסמבל שצריכה לשלוח ack על מנת שיהיה אפשר לבצע פעולת כתיבה או בחירת leader znode חדש (לאחר שהוא נופל).

latency-
בזוקיפר הנתונים מאוחסנים בmemory, מה שהופך אותם לזמינים במהירות .






1. **Protocol Flow:**  Walk through the Kerberos authentication flow from initial login (kinit) to obtaining service tickets.  Include AS, TGS, and ticket caches.
1-הkerberos מקצה כרטיס לשרת או לקוח מסוים (הכרטיס למעשה נותן את האפשרות לקיים תקשורת מאובטחת על ידי הkeberos),
שרת ה-Authentication  מאשר את הלקוח או השרת שברצונם לתקשר, מעניק לו את כרטיס ה-ticket caches ומחבר אותו לשרת Ticket-granting .
שרת הTicket-granting server הוא מספק את הכרטיסים בסופו של דבר.
ה-Kerberos  עושה שימוש בשרת Key distribution center שתפקידו לספק את הכרטיס הראשוני ללקוח ולטפל בבקשות לקבלת הכרטיסים.

2. **Key Concepts:**  Define principals, realms, KDC components, tickets (TGT vs service ticket), and how encryption keys are derived and used.

principal-   ישות מסוימת (שרת או לקוח) שאליה ניתן להקצות כרטיסים
realm-Key Distribution Center אשר תחת שרת ה principals  גבול רשת לוגית שמקבץ בתוכו
KDC-
שרת שמאמת את ה-principels ודואג לכך שיסופקו להם כרטיסים.
לכל reakm יש שרת KDC משלו.
הוא מורכב מ- השרתים: AS, TGS
ומ-DB המכיל את כל הprincipals שב-realm שלו.

הTGT זהו הכרטיס שהעניק הKDC ללקוח ובו נעשה שימוש כדי לקבל כרטיס מהשרת TGS .



כאשר הKDC מנפיק ללקוח כרטיס ועונה על בקשתם הוא משתמש בשלושה מפתחות שונים שהם:
1-המפתח long-term: שבו משתמש שרת הKDC בשביל להצפין את הכרטיס שהתקבל מהשרת TGS.
2-המפתח session: הKDC בוחר את המפתח באופן רנדומלי וממקם העתק שלו בתוך כרטיס ובתוך חלק מוצפן של התשובה לבקשה.
3-המפתח reply-encrypting-הKDC משתמש בו כדי להצפין את התשובות שהוא שולח ללקוחות.

3. **Security Properties:**  Why is Kerberos considered secure?  Discuss mutual authentication, replay protection, time sensitivity, and the role of the ticket lifetime.
   הקרבורס נחשב למאובטח בשל כמה סיבות.
   1- יש בו פיטר הדורש מכל לקוח לאמת את זהותו לשרת, והשרת צריך לאמת את זהותו ללקוח לפני שמתקיימץ
4. **Administration & Tools:**  What are common Kerberos administration tasks?  Describe commands like `kadmin`, `kinit`, `klist`, `kdestroy`, and how to add principals or change passwords.
5. **Integration & Troubleshooting:**  How do services (Hadoop, HTTP, SSH) integrate with Kerberos?  What are typical issues (clock skew, wrong realm, keytab problems) and how do you diagnose them?


1. **Directory Structure:**  Explain how LDAP organizes information in a hierarchical tree (DN, RDN), common object classes, and attributes for users and services.

הפרוטוקול בנוי מספריות במבנה עץ הירכי שנקרא דירקטורי אינפורמאשיון טרי.
כל צומת בעץ מיוצגת כערך או כרשומה במסד נתונים של LDAP.
כל ערך של LDAP בעל מזהה יחודי שנקרא DN ומורכב מצמדים של תכונות וערכים.
לכל צומת בעץ יש גם שם יחודי שנקרא RDN והוא מורכב מצמד אחד לפחות של תכונה וערך.
מחלקות של אובייקטים הם מגדירות את המבנה והתכונות של הספריות.


התיקיות משתמשות בסכמות כדי להגדיר מחלקות ליצירת אובייקטים ותכונות

   
2. **Protocols & Operations:**  Describe basic LDAP operations – bind, search, modify, add, delete – and the difference between simple and SASL binds.
   בינד-אימות המשתמש ושינוי פרטי ההתחברות שלו.
   חיפוש- אחזור ערכים שמתאימים לקבוצת ערכים מוגדרת.
   שינוי- שינוי התוכן של ערך מסוים בספריה
   הוספה- הוספת ערך חדש לספריה.
   מחיקה- הורדת עך מהספריה.
   בהתחברות SASL ניתן להזדהות באמצעות מגוון דרכים שונים בשונה מהתחברות רגילה שבה תהליך ההזדהות מתבצעת רק על ידי הכנסת סיסמה ושם החשבון.
   
3. **Schema & Extensibility:**  What is an LDAP schema?  How do object classes, attribute types, and syntax rules define what data can be stored?  Mention extending schemas.
4. **Authentication & Authorization:**  How is LDAP used for authentication and authorization?  Cover binding with credentials, password policies, and group lookups.
5. **Deployment & Security:**  Outline how to install/configure an LDAP server (e.g., OpenLDAP), secure it with TLS, replicate data, and troubleshoot common errors (referral loops, access controls).



-איך קרברוס מתקשר למונחים directory active וLDAP?
כדי שלקוח יקבל גישה להתחבר לactive directory עליו לפנות לKDC על מנת להתחיל את תהליך ההתחברות.
לאחר שהמשתמש אומת הוא מקבל icket-granting ticket אשר מאשר את אימותו.
אחר כך הלקוח שולח בקשה לקבל tgs ticket מהשירות בו הוא רוצה להשתמש (active directory למשל) באמצעות השימוש בפרוטוקול ldap, במידה ויש למשתמש את הסמכות לעשות שימוש מסוים בשירות, הוא מקבל ממנו את הכרטיס.


## Recommended Resources

- [Apache Zookeeper Documentation](l)
- [Kerberos: The Network Authentication Protocol](https://web.mit.edu/kerberos/)
- [LDAP: RFC 4511 Overview](https://datatracker.ietf.org/doc/html/rfc4511)
- *Hadoop Security* chapter in any modern Hadoop book for integration examples.
