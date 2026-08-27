## FastAPI ORM Exercise
# Table of Contents
[Branch Workflow](#branch-workflow)
[Design Guidelines](#design-guidelines)
- [Technical Requirements](#technical-requirements)
- [Rules and Validations](#rules-and-validations)
- [API Requirements by Level](#api-requirements-by-level)
   - [Level A - Must Win](#level-a---must-win)
   - [Level B - Important](#level-b---important)
   - [Level C - Nice To Have](#level-c---nice-to-have)
- [Going Further](#going-further)
   - [Writing Tests](#writing-tests)
   - [Adding CI](#adding-ci)
   - [Creating a Dockerfile](#creating-a-dockerfile)
   - [Deploying on OpenShift](#deploying-on-openshift)
- [Timeframe & Guidelines](#timeframe--guidelines)
   - [Technical Notes](#technical-notes)
   - [Need Help?](#need-help)

## Goal

This exercise has three goals:

1. Introduce FastAPI components and useful Python libraries.
2. Show what it means to expose a product through an API.
3. Give hands-on experience with design and implementation.

## Background

You will build a Python application that exposes an API for managing HDFS directory
configurations stored in a database. Each directory configuration is called a **deployment**.

> **Important:** You will not manage real HDFS directories. You will work with a database
> that stores their configuration details.

You are given the  SQLite datebase file [`exercise.db`](./exercise.db). Your task is to
explore the dataabse and implement an API that manages deployments, permissions, and
related entities while enforcing the business rules below. See the
[Database Overview Document](./db-overview.md) for the full schema description

## Setup

Set up your development environment first.

1. Fork this repository from the GitLab UI.
2. Give your mentor **Maintainer** access to your fork.

## Branch Workflow

Work on a fork of this repository and progress through feature branches.
Create each branch from `main`, open a merge request back into `main`, and wait for your
mentor's approval before moving to the next branch.

Use the following branch order:

1. `feature/development-level-a-must-win`
2. `feature/development-level-b-important`
3. `feature/development-level-c-nice-to-have`
4. `feature/writing-tests`
5. `feature/adding-ci`
6. `feature/adding-dockerfile`

See [Development Conventions](./CONVENTIONS.md) for full branch, commit, and merge request conventions.

## Design Guidelines

- Log to **stdout**.
- Return correct HTTP status codes and avoid exposing internal exceptions.
- Keep a clean separation between **API**, **business logic**, and **database access**.
- Provide a file that makes the project easy to run and installs all dependencies
  (for example, from `requirements.txt`).

### Technical Requirements

Apply the concepts you have learned so far and use the following in your implementation:

- FastAPI `Query` and `Depends`
- Pydantic (for schema validation and for settings)
- SQLAlchemy

## Rules and Validations

1. Each deployment has **exactly one** email address, which must be valid.
2. Deleting a deployment is a **soft delete**: set `IsDeleted` to `1`; do not remove the row.
3. Set `CreationTime` on insert and `ModificationTime` on insert/update.
4. Each deployment must have **at least one Owner and one Group** permission principal.
5. No duplicate permission principals are allowed for the same deployment.
6. You cannot add an ACL principal for an entity that is already an **Owner** or **Group**.
7. Deployment paths must be unique.
8. `FileQuota` and `SpaceQuota` must be greater than `0`.
9. `DataReplicas` must be `1`, `2`, or `3`.

Choose where and how to run these validations so they are maintainable by admins and clear to users.

## API Requirements by Level

### Level A - Must Win

1. Get all deployments.
2. Get all non-deleted deployments.
3. CRUD on deployments (soft delete is marked in `IsDeleted`).
4. Get all DataRoles.
5. Get all FileFormats.

### Level B - Important

1. CRUD on deployment permissions.
2. Get deployment mail address.
3. Search deployments by partial path.
4. Health check endpoint.
5. Log to **file** in addition to stdout.
6. Filter deployments by role or other criteria using **query parameters**.

### Level C - Nice To Have

1. Get all deployments where an entity has permission to do a specific operation.

   > Example: given entity `garib` and permission `r-x`, return all deployments where
   > `garib` has read and execute permissions. This includes deployments where `garib`
   > is the owner or group, or where `garib` has `rwx`.

2. Rolling file logger.
3. Protect the API with credentials: require authentication for endpoints, and do not
   hard-code credentials. Use environment variables or a config file instead.

## Going Further

After you finish the development part of the exercise, continue with the steps below **in order**.
Do not move to the next step before updating your mentor and getting approval.

### Writing Tests

Once the development part is complete, talk to your mentor. Your mentor will tell you
**what to test** and which testing tools to use.

Common areas to test:

- Validation rules (invalid email format, duplicate paths, invalid quota values)
- Soft-delete behavior
- CRUD operations on deployments and permissions
- Authorization behavior, if authentication is implemented

Wait for your mentor's instructions before writing any tests.

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

### Deploying on OpenShift

After your Dockerfile is ready and approved, deploy the application on OpenShift using a
minimal Helm chart.

The deployment must:

- Run **3 replicas** of the application.
- Make the application **accessible from outside the cluster**.

Before deploying, **ask your mentor**:

- Which OpenShift cluster and project to deploy to.
- How to authenticate and access the cluster.
- Whether any organizational conventions or existing Helm charts should be used.

Your mentor will help you with the deployment process.

## Timeframe & Guidelines

The exercise is divided into the following phases:

- **Development part**: 3 full work days
- **Testing**: 1 full work day
- **CI and Dockerfile and Openshift deployment**: 1.5 work days

Do not move to the next phase before updating your mentor and getting approval.

### Technical Notes

- Focus first on writing clean, compliant code for the development part.
- Your mentor will not serve as a linter; follow the project's linting configuration.
- If you need to disable additional linting rules beyond the existing configuration, get
  your mentor's approval first.
- Tests, CI, and Docker are follow-up steps described in [Going Further](#going-further).
  Do not work on them before completing the development part and consulting your mentor.

### Need Help?

If anything is unclear or confusing, **please reach out to your mentor for clarification**.

---
Good luck! 🍀
