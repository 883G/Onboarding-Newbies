# Hands-On Practice: Kubernetes & Helm

This module continues the previous fast ORM API exercise by moving from a local service  
to a fully containerized deployment running on Kubernetes using Helm.

The goal is to practice packaging applications, deploying them to a cluster,  
and understanding how configuration, networking, and scaling work in a real system.

---

### ⏳ Timeline  
Estimated Duration: 2 Days  

Day 1 – Helm Chart & Deployment Setup  
- Complete Docker image usage  
- Create Helm chart structure  
- Define Kubernetes resources  

Day 2 – Deployment, Networking & Validation  
- Deploy to cluster (Kind / External)  
- Configure service exposure  
- Test scaling and rolling updates  

---

### 📚 Resources  

- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Helm Documentation](https://helm.sh/docs/)
- [Kind Documentation](https://kind.sigs.k8s.io/) 

---

# ⚠️ Environment Selection

There are two versions of this exercise:

- Internal environment (team cluster)  
- External/local environment (Kind / public labs)  

You must ask your mentor which environment to use before starting.

---

# Module 1 – Helm Chart Creation

Starting point:

- Working ORM API
- Dockerfile from previous exercise  
- Built image 

Tasks:

1. Create a Helm chart using: helm create ORM-api  
2. Clean unnecessary default templates  
3. Define deployment:
   - container image  
   - port (e.g. 8000)  
   - replicas  
4. Define service:
   - expose ingress 
5. Move configuration into values.yaml 

---

# Module 2 – Deployment & Networking

Tasks:

### Deploying on OpenShift

After your Dockerfile is ready and approved, deploy the application on OpenShift using a
minimal Helm chart.

If working locally:

Setup cluster:

- kind create cluster
- kubectl cluster-info

The deployment must:

- Run **3 replicas** of the application.
- Make the application **accessible from outside the cluster**.

Before deploying, **ask your mentor**:

- Which OpenShift cluster and project to deploy to.
- How to authenticate and access the cluster.
- Whether any organizational conventions or existing Helm charts should be used.

Your mentor will help you with the deployment process.

---

# Module 3 – Scaling & Rolling Updates

Tasks:

1. Scale application:
Hints
   - replicaCount
   - helm upgrade
   - verify multiple pods  

2. Rolling update:
   - change image tag/version  
   - run helm upgrade again  
   - observe rollout status via kubectl rollout status deployment  

---

# Module 4 – Optional: Local Cluster

If working locally:

Setup cluster:
- kind create cluster  
- kubectl cluster-info  

---

# Module 5 – Deep Dive

Explore:

- Difference between Pod IP and Service IP  
- Why pods are not accessed directly  
- How Services load balance traffic  
- What happens when a pod fails  
- Add readiness/liveness probes  
- Add resource limits (CPU/memory)  (Why did it work without this?)
- Switch Service to NodePort and access externally  
- Add Ingress

---

# 🎯 Deliverable

By the end of this exercise you must have:

- Working Helm chart for ORM API  
- Application deployed on Kubernetes  
- Service exposing the API  
- Demonstrated scaling  
- Demonstrated rolling update via Helm  
