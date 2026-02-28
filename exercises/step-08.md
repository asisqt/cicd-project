# Step 8: Create OpenShift pipeline

**You are almost done with the final project.\
Now that you have the tasks created, you will need to:**

- Install the tasks in the lab OpenShift cluster
- Create CD pipeline

**Please follow the porcess mentioned in the Hands-on Lab: CI/CD with OpenShift Pipelines for doing the below tasks.**

## Your task

1. In the terminal, install the `cleanup` and `nose` tasks by applying the `tasks.yml` file with `kubectl apply -f .tekton/tasks.yml` command.
2. Open the OpenShift console from the lab environment.
3. Create a PVC from the `Administrator` perspective with
    - storageclass: `skills-network-learner`
    - select a PVC: `oc-lab-pvc`
    - size: 1GB
4. Create a new pipeline and a workspace called `output`
5. Add the following steps in this order:
    - cleanup
    - git clone
    - flake8 linting
    - nose tests
    - buildah task
6. Test the pipeline works. Take a screenshot as described in this exercise's `Solutions` section.
7. Add the final step of deploying the application to the lab openshift cluster using the `openShift-client` task and the *oc deploy command*.
    - `oc create deployment $(params.app-name) --image=$(params.build-image) --dry-run=client -o yaml | oc apply -f -`

You can refer to the videos and other content in the module 4 of the course in case you want to familiarize yourself with the concepts before proceeding further.

### Hint

**The PVC opions should look as follows:**

![PVC details](https://github.com/user-attachments/assets/ddfe5cfa-c229-4ab9-aea9-df6bbf361ca8)

At the end of this exercise, you can validate the solution as follows:

### Solution

1. Confirm the pipeline has the following steps:

![Deploy task final](https://github.com/user-attachments/assets/5abde1b5-89eb-4e31-a1e3-bee0d264f5e2)

2. Confirm the pipeline runs as shown:

![Deploy task green](https://github.com/user-attachments/assets/0d80d49e-8110-434d-b53d-9275726c1179)

3. Confirm you can see the application logs in the OpenShift console:

![Application logs](https://github.com/user-attachments/assets/80c51375-e46d-4055-81c8-7714bc6bd47b)
