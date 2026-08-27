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
   Build the Docker image and tag it (e.g., `pizza-api`) **MAKE SURE TO MAKE IT A LIGHTWEGIT IMAGE**

3. **Run the container:**  
   - Run the container locally  
   - Map ports correctly  
   - Verify the API is accessible (`/docs`)  
---

# Module 2 – Development Workflow

### Adding CI

After your mentor approves your tests, add CI stages to the existing `.gitlab-ci.yml`.
The file already includes shared CI jobs for `markdownlint` and `codespell`; these are
maintained separately and are not part of this exercise. Do not modify or remove them.
Only add the project-specific stages described below.

Your CI pipeline must include:

### Creating a Dockerfile

The final step is to containerize the application. Create a `Dockerfile` that builds and
runs the API.

If you are working internally, **ask your mentor for a base image**. Otherwise, use an
official Python base image matching the project's Python version.

Guidelines:

- Install dependencies from `requirements.txt` (or equivalent).
- Expose the port your application listens on.
- Use a non-root user to run the container.
- Keep the image small and avoid including unnecessary files.

Do not start this step before your mentor approves your CI pipeline.

---

### 🎯 Deliverable

- Completed `Dockerfile`
- Working container running the API
- Verified endpoint (`/docs`)
- Clean Git history with PR