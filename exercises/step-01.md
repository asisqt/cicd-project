# Step 1: Create basic workflow

Your GitHub repository has an empty workflow file, `.github/workflows/workflow.yml.`\
You will create the CI workflow by writing several steps in this workflow file.

## Your task

Open the `.github/workflows/workflow.yml` file and add the following:

1. name: `CI workflow`
2. workflow triggers: `push on main branch` and `pull_request on main branch`
3. Jobs
    - runs-on: `ubuntu-latest`
    - container: `python:3.9-slim`
4. Checkout step:
    - name: `Checkout`
    - uses: `actions/checkout@v3`
5. Install Dependencies step:
    - name: `Install dependencies`
    - run `python -m pip install --upgrade pip` and `pip install -r requirements.txt` commands

You can also refer to the videos and labs in the module 2 of the course in case you want to familiarize yourself with the concepts before proceeding further.

---

### Hint

**You can use the following file as a template for this exercise:**

```yml
name: {name of workflow}
on:
  push:
    branches: {array of branches}
  pull_request:
    branches: {array of branches}
jobs:
  build:
    runs-on: {placeholder}
    container: {placeholder}
    steps:
      - name: {placeholder}
        uses: {placeholder}
      - name: {placeholder}
        run: |
        {first command}
        {second command}
```
