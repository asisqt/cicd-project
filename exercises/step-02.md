# Step 2: Add the linting step to CI workflow

Next, you will add the `Lint` step to the GitHub workflow.\
You will use `Flake8` module for linting.\
Open the `.github/workflows/workflow.yml` file and complete the following tasks.

## Your task

Add a linting task with the following details:

1. name: `Lint with flake8`
2. commands:
    - `flake8 service --count --select=E9,F63,F7,F82 --show-source --statistics`
    - `flake8 service --count --max-complexity=10 --max-line-length=127 --statistics`

You can refer to the videos and labs in the module 2 for help.

### Hint

**You can use the following file as a template for this exercise:**

```yml
    - name: {placeholder}
    run: |
      {first command}
      {second command}
```
