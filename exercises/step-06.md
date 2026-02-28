# Step 6: Create cleanup Tekton task

Congratulations on successfully creating the GitHub CI workflow to checkout, lint, and test your code.\
The next step is to create the CD workflow in OpenShift.\
Before you can do that, create the cleanup task that will clean the output workspace so that the CD pipeline can start fresh.

Open the `.tekton/tasks.yml` file and complete the following tasks.

## Your task

**Add a cleanup task with the following details:**

1. apiVersion: `tekton.dev/v1beta1`
2. kind: `Task`
3. name: `cleanup`
4. spec.workspaces.name: `source`

**This task will have a single step called `remove` as follows:**

1. name: `remove`
2. image: `alpine:3`
3. env:
    - name: `WORKSPACE_SOURCE_PATH`
    - value: `$(workspaces.source.path)`
4. workingDir: `$(workspaces.source.path)`
5. securityContext
    - runAsNonRoot: `false`
    - runAsUser: `0`
6. script:

    ```bash
    #!/usr/bin/env sh
      set -eu
      echo "Removing all files from ${WORKSPACE_SOURCE_PATH} ..."
      # Delete any existing contents of the directory if it exists.
      #
      # We don't just "rm -rf ${WORKSPACE_SOURCE_PATH}" because ${WORKSPACE_SOURCE_PATH} might be "/"
      # or the root of a mounted volume.
      if [ -d "${WORKSPACE_SOURCE_PATH}" ] ; then
        # Delete non-hidden files and directories
        rm -rf "${WORKSPACE_SOURCE_PATH:?}"/*
        # Delete files and directories starting with . but excluding ..
        rm -rf "${WORKSPACE_SOURCE_PATH}"/.[!.]*
        # Delete files and directories starting with .. plus any other character
        rm -rf "${WORKSPACE_SOURCE_PATH}"/..?*
      fi
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
  description: This task will clean up a workspace by deleting all the files.
  workspaces:
    - name: {placeholder}
  steps:
    - name: {placeholder}
      image: {placeholder}
      env:
        - name: {placeholder}
          value: {placeholder}
      workingDir: {placeholder}
      securityContext:
        runAsNonRoot: {placeholder}
        runAsUser: {placeholder}
      script: |
        {placeholder}
```
