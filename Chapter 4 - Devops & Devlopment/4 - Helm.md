# Container Orchestration Foundations: Kubernetes & Helm

Before deploying production-grade services, it is important to understand how container orchestration works.

This module introduces Kubernetes and Helm as the standard tools for managing containerized applications at scale.

The goal is to understand *how systems are deployed, configured, and managed*, and to gain hands-on experience using real-world labs.

---

### ⏳ Timeline  
Estimated Duration: 2 Days  

**Day 1 – Theory & Concepts**  
- Kubernetes core architecture  
- Workloads and networking  
- Helm fundamentals and packaging  

**Day 2 – Hands-On Labs**  
- Kubernetes practical labs  
- Helm chart deployment  
- Debugging and inspection  

---

### 📚 Resources  
Use the resources below as your primary reference:

- [Kubernetes Documentation](https://kubernetes.io/docs/)  
- [Helm Documentation](https://helm.sh/docs/)  
- [OpenShift Documentation](https://docs.openshift.com/)  

---

# Day 1 – Kubernetes & Helm Concepts

### ❓ Guide Questions

1. What is Kubernetes, and what problems does it solve compared to running containers manually on vm?  

2. Describe the main Kubernetes components and architecture.  
   Include: cluster, nodes, control plane, kubelet, API server, etcd.

3. What are the core Kubernetes resources?  
   Explain Pods, Stateful sets, daemon sets , limit ranges, pv and PVC, namespaces, cronjobs, jobs, roles, rolebindings  Deployments, Services, ConfigMaps, and Secrets, and how they interact.

4. How does networking work in Kubernetes?  
   Explain Service types (ClusterIP, NodePort,Ingress,Internal or external network) and basic communication between pods.

5. What is Helm, and why is it used?  
   Explain charts, values.yaml, templating, and how Helm simplifies deployments.

---

## Q&A

1. מתי צריך תלות בין containers

למשל אם הם צריכים משאבים משותפים או פועלים בצורה מאוד צמודה אחד לשני,
למשל כאשר container אחד דוחף קונפיגורציות לcontainer אחר או למשל לנהל איזשהו backup של מידע, בלי לפגוע בcontainer הראשי, או להוציא לוגים מהcontainer הראשי.

2. מה זה init container

הם containers שחייבים לרוץ ולהסתיים בהצלחה לפני שהapp הראשי יתחיל לרוץ.
למשל לחכות לservice שיעלה.

3. לחפש דוגמה לjob עם כמה pods

למשל עיבוד של מידע באופן מקבילי כאשר מחלקים לכמות batches.
או למשל איזשהו queue של works שכל pod לוקח משם עבודה, ואז ניתן להריץ במקביל (בהנחה שהם בלתי-תלויים)

4. למה צריך deployment

נותן לנהל את הpods שהוא פורס בצורה הרבה יותר נוחה.
למשל מאפשר scacling בקלות וupdates למיניהם בלי להתחיל לחפש pod pod.

5. מתי נשתמש בnodeport

היתרון היחיד (שמצאתי) הוא הפשטות שלו, בסך הכל פותחים עוד port על הnode,
ואין צורך להרים עוד רכיב ביניים שיחשוף את הservice.
ולכן מאוד מקל על סביבות פיתוח פשוטות.

6. מה זה ingress controller

הרכיב שמנתב בפועל לפי החוקים של הingress כלומר הresource.

7. מה זה kubernetes gateway api

זה מין סטנדרט שמגדיר ניתוב של בקשות בcluster kubernetes.
הוא מורכב מ3 רכיבים 
הgateway class הוא תבנית ליצירת gateways ומגדיר קבוצה של gateways שחולקים קונפיגורציה ומנוהל על ידי controller מתאים.
הGateway, ששם הניהול קורה בפועל והוא בעצם הentry point לcluster.
הhttp route, מנהל ניתוב של בקשות http.

8. פתרון להצפנה של secret

ניתן להשתמש באפשרויות מחוץ לkubernetes למשל ב HashiCorp Vault.
שמאפשרים ניהול secrets ברמה יותר גרנוילרית.

9. מה זה GC ?

אוסף של רכיבים בkubernetes לביצוע GC
למשל מחיקה של תמונות ללא שימוש, מחיקה של containers לא פעילים בpod (על ידי הkubelet).
https://kubernetes.io/docs/concepts/architecture/garbage-collection/

10. האם פוד בsuccess/failed עדיין קיים ?

כן, kubernetes לא מוחק pods באופן אוטומטי.

11. מה הphase של pod שמורידים אותו תשתיתית בכוח

אני מניח שהכוונה היא לterminating למרות שזה לא phase אלא state.

12. מה זה probe

הגדרה של בדיקות כדי לקבוע תקינות של containers 
למשל כדי לקבוע עם container עדיין רץ או להגדיר מתי הוא נחשב ready.
קצת מזכיר health check וdepends on מdocker compose.

13. איך מחלקים משאבים לnamespace - מה השם של האובייקט ?

ResourceQuota.

14. איזה משאבים ניתן להגביל לnamespace

הרבה, בין היתר, cpu, memory, כמות storage, כמות pvc,
כמות kubernetes' resources למיניהם כמו כמות פודים, קונפיג מאפס ועוד. 

15. האם חייב להגדיר limit

נראה שלא

16. access mode in pvc

ReadWriteOnce, ReadOnlyMany, ReadOnlyMany, ReadWriteOncePod
די מסביר את עצמו, רק שאם לא מצויין Pod אז הכוונה היא לnode.

17. מאיפה מוקצים המשאבים לdaemon set

למיטב הבנתי, הם תחת הnamespace.
כלומר לא שונים באופן הזה מפודים רגילים.

18. האם כל pod ב statefull set מקבל pvc משלו

כן

19. למה צריך שמות קבועים לpod בstatefull set

בשביל סדר הרצה מסודר וכך לשמור למשל בdatabases על זה שprimary תרוץ לפני רפליקות.

20. מה מופיע בChart

מכיל את השם והגרסה של הchart, לפחות אלו החובה.
למשל מאפשר לעשות rollback לכל הפריסה, לא בהכרח רק לפוד אחד או resource אחד.

21. איך helm תורם להפחתת redundencies בValues

ניתן לארגן את הValues בצורת overlays כך שלמשל יש איזשהו base.yaml וניתן לעשות לערכים override,
מקבצים כמו dev.yaml או prod.yaml.

# Day 2 – Hands-On Labs (Kubernetes & Helm)

### ⚠️ Important

There are **two versions of this exercise**:

- Internal lab (provided by the team)  
- External lab (public platforms)  

👉 **You must ask your mentor which version you are required to complete before starting.**

---

## 🧪 Lab Tasks (External Option)

### Kubernetes Core Practice

👉 Start here:  
- [KillerCoda Kubernetes Labs](https://killercoda.com/kubernetes)

**You must complete the following scenarios:**

- Kubernetes Basics  
- Kubernetes Pods  
- Kubernetes Deployments  

---

### 🎯 Required Skills (Must Demonstrate)

During the labs, you must perform:

- Deploy an application (nginx or similar)  
- Expose it using a Service  
- **Scale the deployment (replicas up/down)**  
- **Perform a Rolling Update (change image/version)**  
- Inspect logs and running pods  

---

### Helm Hands-On Lab

👉 Helm practice:  
- [KillerCoda Helm Labs](https://killercoda.com/helm)

Tasks:

- Install a Helm chart  
- Modify values.yaml  
- Perform upgrade  
- Uninstall release  

---

## 🔄 Alternatives

Assignment: Compare two Kubernetes deployment approaches:

- Helm Charts vs Raw Kubernetes YAML manifests

Deliverable:
- 1–2 sentences comparison  
- Include a real-world use case for each  

Goal:
Understand the trade-offs between templated/package-based deployments and manual resource definitions.

---

## 🎯 User Story & Scenario

Assignment: Describe a real-world Kubernetes deployment using Helm.

Deliverable (2 paragraphs):

- Describe a service (e.g., API) deployed to Kubernetes  
- Explain how deployment is managed using Helm (chart, values.yaml, releases)  
- Describe how Helm helps manage environments (dev/staging/prod) and simplifies updates (e.g., rolling upgrades)  

---

## 🎯 Deliverable

By the end of this module, you should have:

- Completed the assigned labs (internal or external, per mentor decision)  
- Successfully deployed and exposed an application in Kubernetes  
- Demonstrated scaling and rolling updates  
- Used Helm to install and manage an application  
- Demonstrated ability to inspect and debug workloads 
