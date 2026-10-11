# Zookeeper Foundations

Zookeeper is a distributed coordination service.

Instead of building coordination mechanisms from scratch, systems rely on Zookeeper.

---

### ⏳ Timeline
Estimated Duration: 0.5 Day

Zookeeper Core Concepts:
- Architecture & Ensemble Roles  
- Znode Data Model  
- Consistency & Watches  
- Sessions & Failure Handling  
- Common Distributed Patterns  
- Failover and Leader Elections

---

### 📚 Resources
- [Apache Zookeeper Documentation](https://zookeeper.apache.org/)
- [Zookeeper Recipes and Solutions](https://zookeeper.apache.org/doc/current/recipes.html)

---

# Zookeeper Core Concepts

### ❓ Guide Questions

1. **What is Zookeeper, and how does its architecture organized?**  
תוכנת zookeeper היא תוכנה לסינכרון בין מערכות מבוזרות. היא מאפשרת fault tolerance ומהווה חלק משמעותי מHbase. הארכיטקטורה מסודרת בצורה הבאה:
יש לנו את האפליקציה שלנו וכל לקוח מתחבר ללקוח zookeeper שמאפשר לו לדבר עם שרתי הzookeeper. אם zookeeper בשרת אחת ולא מבוזר אז יש לנו point of failure מאוד גדול לכן לרוב יש ביזור. האוסף ביחד נקרא zookeeper ensemble. כחלק מהביזור יש גם רפלקציה של המידע בשביל fault tolerance, ואם עכשיו לקוח יבקש לכתוב משהו לznode וירצה fault tolerance של עותק נוסף בשרת אחר, אז הוא יקבל קונפירמציה שהכתיבה נעשתה רק אחרי שבאמת נעשו כל הכתיבות, כולל העותקים הנוספים באופן מבוזר.


2. **How does Zookeeper handle consistency and notifications?**  
   Explain:
   - Sequential consistency  
   - Watches  
   - One-time triggers  
   - How clients use watches

התוכנה zookeeper מטפלת בעקביות ובהתרעות בצורה חכמה. בנוגע להתרעות, יכול להרשם להתרעות על znode בעזרת watches. זה חוסך ללקוח את העבודה של כל הזמן לבדוק את הznode ואת המצב שלו. zookeeper מבטיח sequential consistency, שזה אומר שאם לקוח מבקש לעשות פעולות בסדר כלשהו אז הן יקרו בסדר הזה. כשמשתמשים בשעונים בzookeeper בכלליות חשוב לזכור שהם one time triggers, יעני ברגע שהשעון פועל ומתקבלת התרעה, אז זהו, לא יהיו עוד התרעות. אם מעוניינים בלקבל התרעות על עוד שינויים צריך לשים שעון חדש. כן יש חסרונות שבגלל התקורה הזו יכולים לפספס דברים שנרצה לקבל עליהם התרעות בזמן הזה.

3. **What are Znodes and what types of Znodes exists?**

הznodes הם האיברים בעץ הzookeeper. הם מכילים מידע ומנהלים stat שמכיל מידע תאורטי כגון גרסת המידע מבחינת שינויים עם פרטים על הזמנים. יש שני סוגים של znodes. יש persistent znodes שנשארים שמורים עד שמוחקים אותם באופן מפורש ויש ephemeral znodes שנמחקים אם הלקוח שיצר אותם מאבד חיבור עם הzookeeper.
4. **What are sessions, and how does Zookeeper handle failures and node lifecycle?**  
   Explain:
   - Session lifecycle  
   - Heartbeats  
   - Session expiration  
   - Persistent nodes  
   - Ephemeral sequential nodes
   - Failover
   - Leader elections
   - ZXID
כמו שאמרנו, ללקוח יש רשימה של שרתי Zookeeper בensemble. הוא עובר על הרשימה ומנסה להתחבר עם שרת עד שהוא מצליח. כשהוא מצליח אז השרת יוצר session חדש עם הלקוח ונותן לו זמן time out. אם הלקוח לא מתקשר עם השרת למשך הזמן הזה, השרת יכול להחליט לעשות session expiration. כשיש session expiration, הephermal nodes נמחקים. כדי למנוע את הtime out, הלקוח צריך לשלוח לשרת פינגים בשם heartbeats. הולדיות של session לא נפגעת כשעוברים לשרת אחר. יש אופציה של sequential nodes שמוסיפים לסוף הpath אינדקס מונוטוני עולה לznode, וככה אנחנו מבטיחים שיש לנו שמות יחודיים. בגלל שיש padding של אפסים לפני כן לפי הגודל המקסימלי זה באמת יהיה ייחודי. כשיש לנו leader שנופל, אז zookeeper מזהה שהוא נפל כי אין תקשורת איתו, ואז מתחיל תהליך הבחירות. בהתחלה כולם מצביעים לעצמם, אבל בסוף יש רוב והאלגוריתם נגמר ובוחר את המנהיג החדש לפי הרוב.
בשביל תקשורת וסנכרון טוב יש בzookeeper מערכת הודעות שדואגת להודעות ולסנכרון שלהן. יש גם משהו שנקרא proposal שהוא מתאר הצעה שאפשר להסכים אליה, ההצעה מכילה הודעה לרוב (אבל יש מקרי קצה נגיד בבחירת מנהיג חדש). כמו שיש חשיבות לסדר ההודעות בzookeeper יש גם חשיבות לסדר הproposals ולכל proposal יש מספר מזהה בשם ZXID. הZXID מחולק לשני חלקים, החצי הראשון מסמן את המנהיג הנוכחי והחצי השני בעצם את האינדוקס היחסי של הproposals ביחס אליו, ככה שבסך הכל הZXID הכולל באמת יהיה ייחודי לכל proposal.

5. **What are the basic operational concerns in Zookeeper?**  
   Describe at a high level:
   - Ensemble deployment  
   - Scaling considerations  
   - Snapshots and transaction logs
   - Common issues 

בensemble deployments יש שני עקרונות עיקריים. רק מספר קטן מהסרברים בdeployment יפלו/יתנתקו, שרתים בdeployment יתפעלו כשורה ויהיו מסונכרנים. תמיד יחשוב שיהיה לי רוב עובד, אז אם יש לי בensemble 5 שרתים, אני יכול לסבול עד 2 נפילות. אם יש לי N, אפשר עד N/2 - 1 נפילות. כדי למזער נפילות, כדאי שתהיה תלות כמה שיותר קטנה ביניהן מבחינת משאבים ורכיבים כך שדבר אחד לא יגרום לנפילה כוללת. בשביל סקלביליות לפעמים מוסיפים observers, שההבדל היחיד ביניהם לבין שרתים בensemble זה שהם לא מצביעים. היתרון זה שהם מעבירים את הבקשות ונותנים עבודה אבל אם הם נופלים הם לא משפיעים על ההצבעות ופוגעים בתהליך. גם דרך התקשורת שלהם יכולה להיות פחות מאובטחת מה שמאפשר לנו לאפטם את מהירות התקשורת. משתמשים יכולים לקחת snapshot מהשרת עם הzxid הכי גבוה ולשמור את המידע איפשהו. כל פעם לפני שמתבצעת בקשה zookeeper מוודא שהבקשה הזאת מתועדת בזיכרון לא נדיף. כמו שאמרנו יש בzookeeper כמה בעיות, בין אם זה העניין שדיברנו עליו קודם עם הwatches שלאור העובדה שצריך לשים אותם מחדש עלול להתפספס בזמן הזה מידע, ובנוסף zookeper מוסיף סיבוך נוסף למערכת בתור רכיב לא טריוויאלי ולפעמים עדיף לא לבחור בו כמו בKafka שיש מעבר כבר לKRaft כי יש יותר סקלביליות וזה יותר מודרני.

6. **Which architectural patterns is ZooKeeper commonly used to implement?**
ארכיטקטוקה של client-server, שלקוחות מדברים עם כמה שרתי zookeeper.
---

### Skila questions


1. Is the data stored by zookeeper stored in a disk or in memory?

A: נשמר בזיכרון

2. What is zookeeper mainly used for?

A: דברים קלים שתוכנות משתמשות בהן כל הזמן וצריך לשמור על סינכרון מדויק, כגון קבצי קונפיגורציה
אפשר להשתמש בו בשביל עוד דברים כגון מימוש מנעולים. 
3. How does zookeeper promise that if at most half the servers crash then nothing is lost?
A:
מריצים בreplicated mode. ככה שרת ששומר מידע משוכפל, אוסף של שרתים כאלו נקרא quorum. בגלל שצריך רוב כדי להכריע החלטה, אפשר שעד חצי מהquorum יקרוס כי כל עוד לפחות חצי רץ ותקין אז ניתן להגיע לרוב בהצבעה. 
A: 
### 🔄 Alternatives
Assignment: Compare two coordination approaches:

- Zookeeper vs Alternatives

Deliverable:
- 1–2 sentences comparison  
- Include a simple use case for each  


---

### 🎯 User Story & Scenario

Assignment: Describe a simple real-world coordination scenario.

Deliverable (2 paragraphs)
