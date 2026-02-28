# Step 3: Add the test step to CI workflow

Next, you will add the `Test` step to the GitHub workflow.\
You will use the `Nose` module for running the tests.\
Open the `.github/workflows/workflow.yml` file and complete the following tasks.

## Your task

Add a test step with the following details:

1. name: `Run unit tests with nose`
2. command:
    - `nosetests -v --with-spec --spec-color --with-coverage --cover-package=app`

You can refer to the videos and labs in the module 2 for help.

### Hint

**You can use the following file as a template for this exercise:**

```yml
  - name: Run unit tests with nose
    run: {insert command here}
```
