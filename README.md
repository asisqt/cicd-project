# Automated CI/CD Pipeline Implementation

## Project Overview
This repository contains the final project implementation for the IBM Continuous Integration and Continuous Delivery (CI/CD) course. The objective of this project is to build a robust, automated pipeline that seamlessly integrates code changes, enforces code quality, and deploys the application to a Red Hat OpenShift cluster.

## Technology Stack
* **Version Control:** Git & GitHub
* **Continuous Integration (CI):** GitHub Actions
* **Continuous Delivery (CD):** Tekton Pipelines
* **Container Orchestration:** Red Hat OpenShift / Kubernetes
* **Code Quality & Testing:** Flake8 (Linting), Nose (Unit Testing)

## Pipeline Architecture

### 1. Continuous Integration (GitHub Actions)
The CI workflow is defined in the `.github/workflows/` directory. It is configured to trigger automatically on push events to the repository. The workflow performs the following automated steps:
* Provisions a continuous integration environment.
* Installs all necessary project dependencies.
* **Linting:** Executes code quality checks to enforce stylistic consistency and identify syntactical errors.
* **Unit Testing:** Runs the automated test suite to ensure application logic remains intact after modifications.

### 2. Continuous Delivery (Tekton on OpenShift)
The CD pipeline is defined within the `.tekton/` directory. It is executed on an OpenShift Kubernetes cluster and orchestrates the deployment process:
* **Workspace Initialization:** Clones the repository into the pipeline workspace.
* **Pre-deployment Checks:** Executes `cleanup` tasks and runs automated tests directly within the cluster environment.
* **Build & Deploy:** Containerizes the application and deploys it to the OpenShift environment, utilizing PersistentVolumeClaims (PVCs) for state management.

## Author
Ashish Khatri
