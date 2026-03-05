# Hands-On Practice: FastAPI & Testing (Pizza Delivery API)

Diving into complex services development, practice the fundamentals of API design, automated testing, and proper Git workflows.

This module provides a hands-on exercise to solidify your understanding of FastAPI, mocking in tests, and collaborative development standards. 

The goal is to practice writing clean code, implementing missing logic, and ensuring your code is fully tested and properly committed.

---

### ⏳ Timeline
Estimated Duration: 3 Days

---

### 📚 Resources
- FastAPI Official Docs – https://fastapi.tiangolo.com/
- Pytest Mocking Guide – https://pytest-mock.readthedocs.io/en/latest/
- Git Branching Strategy – https://nvie.com/posts/a-successful-git-branching-model/

---

# Module 1 – The Pizza API Exercise

### 📁 Getting Started
The base project for this exercise is located in the `assets/pizza_api_project` directory of this current chapter. 
To start, you must **clone the entire repository** to your local machine. Do not copy-paste files; work directly within the Git repository.

### ❓ Your Tasks

1. **Complete the API:** The application currently has a working `GET` endpoint for fetching the menu, but the `POST /orders` endpoint is missing its implementation. Your task is to implement the logic to create a new order.
   
2. **Write Tests with Mocks:**
   Some basic tests are already written in `tests/test_main.py`. However, most are missing. You need to write comprehensive tests for your new `POST` endpoint. 
   *Important:* You must use **Mocks** to simulate the database/payment saving process so that the tests run in isolation without needing a real database.

---

# Module 2 – Development Workflow & Git Standards

To complete this assignment, you must adhere strictly to our team's development workflow.

### 🌿 Git & Collaboration Rules

1. **Clean Commits:** Work with clean, descriptive commits. 
2. **Branching:** Work systematically with Git branches. Create a new branch for your feature (e.g., `feature/post-order-endpoint`).
3. **Pull Requests:** Open a PR per feature. Do not push directly to `main`.
4. **Code Review:** You must request a Code Review (CR) on your PR before merging. Address all comments before completing the merge.

### 📝 Commit Message Standard
Your commit messages must follow this exact convention:

- `DOCS: <files added>` – Use when adding or updating documentation.
- `FEAT: <description>` – Use when adding a new feature or completing the endpoint.
- `FIX: <description>` – Use for bug fixes on your branch *before* merging to main.
- `HOTFIX: <description>` – Use *only* for critical bug fixes applied directly to the main branch.

---

### 🎯 Deliverable
- A merged PR containing the fully functional `POST /orders` endpoint.
- A passing test suite (run `pytest`) containing mocked tests for your new logic.
- A Git history showing adherence to the commit standards and branching strategy.
