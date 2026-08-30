# Hands-On Practice:

After implementing and testing the development part, the next step is to
run the service inside a Docker container.

This exercise continues the previous assignment.  
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

---

# Module 2 – Development Workflow

### Adding CI

After your mentor approves your tests, add CI stages to the existing `.gitlab-ci.yml`.
The file already includes shared CI jobs for `markdownlint` and `codespell`; these are
maintained separately and are not part of this exercise. Do not modify or remove them.
Only add the project-specific stages described below.

Your CI pipeline must include:
1. Installing all project requirements from `requirements.txt`.
2. Running `ruff format`.
3. Running `ruff check`.
4. Running tests with `pytest`.

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