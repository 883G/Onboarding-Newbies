# Hands-On Practice: Kubernetes & Helm (Pizza API Deployment)

This module continues the previous Pizza API exercise by moving from a local service  
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

- Working Pizza API
- Dockerfile from previous exercise  
- Built image 

Tasks:

1. Create a Helm chart using: helm create pizza-api  
2. Clean unnecessary default templates  
3. Define deployment:
   - container image  
   - port (e.g. 8000)  
   - replicas  
4. Define service:
   - expose ingress 
5. Move configuration into values.yaml:
   - image repository and tag  
   - replica count  
   - service port  

---

# Module 2 – Deployment & Networking

Tasks:

1. Install chart:
   helm install pizza-release ./pizza-api  

2. Verify deployment:
   - kubectl get pods  
   - kubectl get svc  
   - kubectl describe pod  

3. Expose application:
   Option A: port-forward service to local port 8000  
   Option B: NodePort
4. Test API

---

# Module 3 – Scaling & Rolling Updates

Tasks:

1. Scale application:
   - update replicaCount in values.yaml  
   - run helm upgrade pizza-release ./pizza-api  
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
- Add resource limits (CPU/memory)  
- Switch Service to NodePort and access externally  
- Add Ingress

---

# 🎯 Deliverable

By the end of this exercise you must have:

- Working Helm chart for Pizza API  
- Application deployed on Kubernetes  
- Service exposing the API  
- Demonstrated scaling  
- Demonstrated rolling update via Helm  
