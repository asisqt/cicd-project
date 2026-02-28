# Step 7: Create test Tekton task

You have added the `cleanup` task to the tekton file.\
Next, add the test task called `nose` right under the `cleanup` task.

Open the `.tekton/tasks.yml` file and complete the following tasks.

## Your Task

Add a testing task with the following details:

1. apiVersion: `tekton.dev/v1beta1`
2. kind: `Task`
3. name: `nose`
4. spec.workspaces.name: `source`
5. params:
    - name: `args`
    - description: `Arguments to pass to nose`
    - type: `string`
    - default: `"-v"`

**This task will have a single step called `nosetests` as follows:**

1. name: `nosetests`
2. image: `python:3.9-slim`
3. workingDir: `$(workspaces.source.path)`
4. script:

```bash
#!/bin/bash
set -e
python -m pip install --upgrade pip wheel
pip install -r requirements.txt
nosetests $(params.args)
```

You can also refer to the videos and labs in the module 3 of the course in case you want to familiarize yourself with the concepts before proceeding further.

### Hint

**You can use the following file as a template for this exercise:**

```yml
apiVersion: {placeholder}
kind: {placeholder}
metadata:
  name: {placeholder}
spec:
  workspaces:
    - name: {placeholder}
  params:
    - name: {placeholder}
      description: {placeholder}
      type: {placeholder}
      default: {placeholder}
  steps:
    - name: {placeholder}
      image: {placeholder}
      workingDir: {placeholder}
      script: |
        {placeholder}
```
