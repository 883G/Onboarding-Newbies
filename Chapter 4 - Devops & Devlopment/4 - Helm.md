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
   Explain orchestration, scheduling, scaling, and self-healing.

2. Describe the main Kubernetes components and architecture.  
   Include: cluster, nodes, control plane, kubelet, API server, etcd.

3. What are the core Kubernetes resources?  
   Explain Pods, Deployments, Services, ConfigMaps, and Secrets, and how they interact.

4. How does networking work in Kubernetes?  
   Explain Service types (ClusterIP, NodePort, LoadBalancer) and basic communication between pods.

5. What is Helm, and why is it used?  
   Explain charts, values.yaml, templating, and how Helm simplifies deployments.

---

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
