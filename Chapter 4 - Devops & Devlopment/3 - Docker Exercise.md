# Hands-On Practice: Dockerizing the Pizza API

After implementing and testing the Pizza Delivery API, the next step is to
run the service inside a Docker container.

This exercise continues the previous assignment.  
A `Dockerfile` already exists in the project and needs to be completed.

The goal is to make the API runnable via Docker with minimal setup.

---

### ⏳ Timeline
Estimated Duration: 0.5 Day

---

### 📚 Resources
- [Docker Documentation](https://docs.docker.com/)

---

# Module 1 – Complete, Build & Run

### 📁 Getting Started
Continue working on the same repository from the previous exercise.

A partial `Dockerfile` already exists in the project.

---

### ❓ Your Tasks

1. **Complete the Dockerfile:**  
   Fill in the missing instructions so the API can run inside a container.

2. **Build the image:**  
   Build the Docker image and tag it (e.g., `pizza-api`)

3. **Run the container:**  
   - Run the container locally  
   - Map ports correctly  
   - Verify the API is accessible (`/docs`)  
---

# Module 2 – Development Workflow

### 🌿 Git & Collaboration Rules

1. Create a branch:
   - `feature/dockerize-api`

2. Use commit conventions:
   - `FEAT: complete Dockerfile for API`
   - `FIX: resolve container runtime issue`

3. Open a Pull Request and request Code Review

---

### 🎯 Deliverable

- Completed `Dockerfile`
- Working container running the API
- Verified endpoint (`/docs`)
- Clean Git history with PR