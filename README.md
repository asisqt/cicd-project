<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>

# Building CI/CD Pipelines
<!-- TABLE OF CONTENTS -->
<details open>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#introduction">Introduction</a></li>
    <li>
      <a href="#course-information">Course Information</a>
    </li>
    <li>
      <a href="#information-about-the-project">Information about the Project</a>
      <ul>
        <li><a href="#general">General</a></li>
        <li><a href="#tech-stack">Tech Stack</a></li>
      </ul>
    </li>
    <li>
      <a href="#what-i-have-done-as-part-of-the-project">What I have done as part of the project</a></li>
      <ul>
        <li><a href="#task-1---setup-of-github-actions-and-implement-a-workflow">Task 1 - Setup of GitHub Actions and implement a workflow</a></li>
        <li><a href="#task-2---building-a-tekton-pipeline">Task 2 - Building a Tekton Pipeline</a></li>
        <li><a href="#task-3---adding-github-triggers">Task 3 - Adding GitHub Triggers</a></li>
        <li><a href="#task-4---using-tekton-continous-delivery-catalog">Task 4 - Using Tekton Continous Delivery Catalog</a></li>
        <li><a href="#task-5---integrating-linting-and-unit-test-automation">Task 5 - Integrating Linting and Unit Test Automation</a></li>
        <li><a href="#task-6---building-an-image">Task 6 - Building an Image</a></li>
        <li><a href="#task-7---deploy-to-openshift">Task 7 - Deploy to OpenShift</a></li>
      </ul>
    </li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>
<br>


## Introduction
This repository was created as part of IBM's "Continuous Integration and Delivery (CI/CD)" course.<br>
It's a project about building a CI/CD pipeline.<br>
Much of the code was cloned from the IBM repository: https://github.com/ibm-developer-skills-network/wtecc-CICD_PracticeCode<br>
<br>
Preview images of the project:<br>

![7 start pipelinerun](https://github.com/user-attachments/assets/10f0b010-47fe-47c8-bce8-38bf20a6cb1b)

![1 Tekton Hub git clone](https://github.com/user-attachments/assets/a25361d2-578a-476b-849b-9a454aaa65df)

![3 running pipeline yaml](https://github.com/user-attachments/assets/b885e717-6936-4095-8f71-2e306d728e9f)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


## Course Information
Title: Continuous Integration and Delivery (CI/CD)<br>
Type: Practice Project<br>
Course Provider: IBM<br>
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


## Information about the Project
### General
- Client: Myself
- Project Goal: Building a CI/CD pipeline. Gain a deeper understanding of Continous Integration and Continous Delivery.
- Number of Project Participants: 1 (Cloned repository of IBM. Developed the rest on my own)
- Time Period: November - December, 2024
- Industry / Area: DevOps
- Role: Developer
- Languages: English
- Result: CI/CD pipeline successfully built. Improved understanding of implementing Continous Integration and Continous Delivery.
<br>

### Tech Stack
With regard to my role:
- CI/CD Tool: GitHub Actions
- CI/CD Tool: Tekton
- Container Orchestration: Kubernetes
- Container Orchestration: Red Hat OpenShift
- IBM Cloud IDE (based on Theia and Container)
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>



## What I have done as part of the project

### Task 1 - Setup of GitHub Actions and implement a workflow
First implemented the setup for GitHub Actions: The creation of a .github/workflows folder with a workflow YML file.<br>
The name of the workflow as well as the events, the job and the runner including the container were defined.<br>

![Implement empty workflow](https://github.com/user-attachments/assets/d3d3f45d-a6e6-4123-ba7c-97f773486752)

If you check the Actions tab on the GitHub website, you will see failed workflows, as the workflow has been triggered but not yet fully implemented.

![Failed workflows](https://github.com/user-attachments/assets/c0988e0a-4227-4744-bcfa-7da8ee302a27)

After the workflow file was created, the steps were added:

![3 Adding Steps to workflow](https://github.com/user-attachments/assets/7be106b4-808f-4422-b555-3a19ca4ce973)

The changes were pushed into the repository. This triggered the workflow again.<br>
It is now running successfully thanks to the implemented steps:

![4 Workflow successful](https://github.com/user-attachments/assets/3f758410-a722-4f49-bfaf-b319a38ba068)

After clicking on the build job, exact details of the individual steps can be viewed:

![5 Details of Workflow Steps](https://github.com/user-attachments/assets/f1720b37-6542-4e02-b174-59a6d89d619f)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Task 2 - Building a Tekton Pipeline
The first step of the task was to create a traditional Hello World program / pipeline in Tekton.<br>
<br>
The Tekton object "Task" is used for this.<br>
According to the Tekton documentation, a Task is a collection of Steps that you define and arrange in a specific order of execution as part of your continuous integration flow.<br>
<br>
The corresponding Task has been implemented in the tasks.yaml file:<br>

![Implement tasks yaml](https://github.com/user-attachments/assets/30aea9c6-0edb-43df-8f59-cd2fec5dfa5e)

It is then applied to the cluster with the following command:<br>

```
kubectl apply -f tasks.yaml
```

The Task has been successfully created:<br>

![2 Task created](https://github.com/user-attachments/assets/505756ef-3db7-44ba-8242-5aa85265b1db)

Next, a Tekton object called "Pipeline" is created that uses and executes the Task object.<br>
The implementation is in the pipeline.yaml:<br>

![3 Implement pipeline yaml](https://github.com/user-attachments/assets/dfa30ea1-423c-4bb8-8059-e14211e1b187)

It is then applied to the cluster with the following command:<br>

```
kubectl apply -f pipeline.yaml
```

The Pipeline has been successfully created:<br>

![4 Pipeline created](https://github.com/user-attachments/assets/2c57f1a8-3427-44ba-843a-ff273dd3030d)

The Pipeline is now executed with the following command:<br>

```
tkn pipeline start --showlog hello-world-pipeline
```

Output of the Pipeline:

![5 Run pipeline and display output](https://github.com/user-attachments/assets/ffafdd0b-b44f-4341-ae94-328388339d2a)

Parameters are now added to make the pipeline more flexible.<br>
Both the task and the pipeline are changed for this.<br>
<br>
The modified tasks.yaml file:<br>

![6 Add params to task](https://github.com/user-attachments/assets/a20a242e-1ad7-4f01-a71e-44a01a111414)

The changes are then applied to the cluster with the following command:<br>

```
kubectl apply -f tasks.yaml
```

The Task has been successfully created:<br>

![7 Task created](https://github.com/user-attachments/assets/2c3c3eca-24ab-4c3e-9326-fed60f870597)

The modified pipeline.yaml file:<br>

![7 5 Add params to pipeline yaml](https://github.com/user-attachments/assets/3419235b-9cb6-47f7-b614-d5dafd1ee0b0)

The changes are then applied to the cluster with the following command:<br>

```
kubectl apply -f pipeline.yaml
```

The Pipeline has been successfully created:<br>

![8 Pipeline update configured](https://github.com/user-attachments/assets/a8ca390e-5347-416a-a8dd-846b652f42b3)

The Pipeline is now executed with the following command:<br>

```
tkn pipeline start hello-world-pipeline \
  --showlog \
  -p message="Hello Tekton! I added params to pipeline!"
```

Output of the Pipeline:<br>

![9 Output of updated pipeline](https://github.com/user-attachments/assets/af834715-e163-4a79-b51e-14cdce40ef29)

To embellish the whole thing a little, another Pipeline is added: cd-pipeline with checkout Task.<br>
The checkout task with parameters and the clone command have been added to the tasks.yaml file:<br>

![10 Add task checkout to tasks yaml](https://github.com/user-attachments/assets/8a9e3d7c-4ade-4443-961c-e8699b3ac965)

The output after applying to the cluster with the following command:<br>

```
kubectl apply -f tasks.yaml
```

![11 Apply new tasks yaml](https://github.com/user-attachments/assets/c8d62118-2ca9-46fb-aa39-46b62c675da1)

The pipeline.yaml file has been extended by the cd-pipeline:<br>

![12 Add cd pipeline](https://github.com/user-attachments/assets/21f4728c-2d08-4875-a2fc-f1a70e565f1b)

The output after applying to the cluster with the following command:<br>

```
kubectl apply -f pipeline.yaml
```

![13 Apply new pipeline](https://github.com/user-attachments/assets/62878edc-b8c9-4560-9a21-d71abe489f22)

If you execute the new Pipeline with the following command, the output appears:

```
tkn pipeline start cd-pipeline \
    --showlog \
    -p repo-url="https://github.com/christian-schw/cicd-practice-project.git" \
    -p branch="main"
```

![14 Output new pipeline checkout](https://github.com/user-attachments/assets/359156e7-05c9-439e-985c-c3c280738c72)

As a final exercise in this section, four placeholder Tasks (lint, tests, build and deploy) are added to the cd-pipeline.<br>
The echo Task already created is used as a placeholder.<br>
The placeholders are replaced in the following sections below.<br>
<br>
The modified pipeline.yaml:<br>

![15 Add placeholder echo tasks to pipeline](https://github.com/user-attachments/assets/119c1096-7a1d-42df-b4cb-7de141144ab5)

The output after applying the changes to the cluster and executing the following command:

```
tkn pipeline start cd-pipeline \
    --showlog \
    -p repo-url="https://github.com/christian-schw/cicd-practice-project.git" \
    -p branch="main"
```

![16 Output placeholder echo pipeline](https://github.com/user-attachments/assets/b14d6de8-fced-4a9b-9474-538b2e27f67b)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Task 3 - Adding GitHub Triggers
Since it is tedious and offers limited possibilities to run the pipeline manually, Tekton objects EventListener, TriggerBinding and TriggerTemplate are created.<br>
This makes it possible for the pipeline to be started automatically by external events (e.g. changes in the GitHub repository).<br>
The corresponding files are located in the folder: ../labs/02_add_git_trigger/<br>
<br>
First, the EventListener was implemented to be able to listen to events on GitHub:<br>

![1 Add eventlistener yaml](https://github.com/user-attachments/assets/c91f1f49-1b87-4d7c-b567-20181de811bb)

The output after applying to the cluster with the following command:<br>

```
kubectl apply -f eventlistener.yaml
```

![2 Verify tekton eventlistener](https://github.com/user-attachments/assets/57509883-3388-435d-b4e2-551c7f769aee)

Next, the TriggerBinding was implemented to be able to bind the incoming data from the event to pass on to the pipeline:<br>

![3 Add triggerbinding yaml](https://github.com/user-attachments/assets/9a358a21-f95b-4ce7-a599-be8238fe57af)

The output after applying to the cluster with the following command:<br>

```
kubectl apply -f triggerbinding.yaml
```

![4 Verify tekton triggerbinding](https://github.com/user-attachments/assets/b0a16e83-0763-49db-8925-fc7ab13b0181)

The TriggerTemplate takes the parameters passed in from the TriggerBinding and creates a PipelineRun to start the pipeline:<br>

![5 Implement triggertemplate yaml](https://github.com/user-attachments/assets/029bb60c-a6c2-42ab-8824-5d9e7e006fa9)

The output after applying to the cluster with the following command:<br>

```
kubectl apply -f triggertemplate.yaml
```

![6 Verify tekton triggertemplate](https://github.com/user-attachments/assets/6368c9d0-6746-4d51-9f41-fa8c00877d54)

To test the Pipeline Run, the curl command is used (Note: localhost port of IBM Cloud IDE is 8090):<br>

```
curl -X POST http://localhost:8090 \
  -H 'Content-Type: application/json' \
  -d '{"ref":"main","repository":{"url":"https://github.com/christian-schw/cicd-practice-project.git"}}'
```

The output:<br>

![7 start pipelinerun](https://github.com/user-attachments/assets/10f0b010-47fe-47c8-bce8-38bf20a6cb1b)

The red marked PipelineRun is the pipeline in this task. Everything works!<br>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Task 4 - Using Tekton Continous Delivery Catalog
The self-created clone task is very small and hardly robust.<br>
To improve the whole thing, a prefabricated task in the Tekton Hub is integrated into our pipeline.<br>
<br>

![1 Tekton Hub git clone](https://github.com/user-attachments/assets/a25361d2-578a-476b-849b-9a454aaa65df)

With the help of the Tekton CLI, this task is installed in our cluster in the current active namespace:<br>

![2 Tekton Hub install git clone](https://github.com/user-attachments/assets/bae64e74-94a7-43e7-b5f3-1b19baa10ffe)

The task requires two inputs:
- The URL of a Git repo to clone ('url' param)
- A workspace / disk volume that can be shared across tasks ('output' param)

To create the workspace, the PersistentVolumeClaim file (pvc.yaml) already predefined by the IBM course is used:<br>

![3 provided pvc yaml](https://github.com/user-attachments/assets/303aa1a0-6e2e-4bf1-9a2c-4b1be702904e)

The output after applying to the cluster with the following command:<br>

```
kubectl apply -f pvc.yaml
```

![4 verifying pvc](https://github.com/user-attachments/assets/810e265c-79be-445b-9235-8a6285f46bb7)

This persistent volume can now be referenced by its name 'pipelinerun-pvc' when creating workspaces for the Tekton tasks.<br>
<br>
The pipeline.yaml is then changed so that the Tekton Hub Task is now used instead of the self-created task.<br>
At the same time, the workspace is defined (as a required parameter according to Tekton Hub):<br>

![5 changing pipeline yaml](https://github.com/user-attachments/assets/fe5b4d7a-9b8b-4ef8-ba07-53bafac6d0d7)

The output after applying to the cluster with the following command:<br>

```
kubectl apply -f pipeline.yaml
```

![6 verifying pipeline](https://github.com/user-attachments/assets/420e0a51-436b-44bf-83f6-3aa8dcc68a94)

A PipelineRun is then created to run the pipeline:<br>

```
tkn pipeline start cd-pipeline \
    -p repo-url="https://github.com/christian-schw/cicd-practice-project.git" \
    -p branch="main" \
    -w name=pipeline-workspace,claimName=pipelinerun-pvc \
    --showlog
```

The logs already show significantly more information than before:<br>

![7 starting the pipeline](https://github.com/user-attachments/assets/1c4c749c-9451-4a86-a058-c9d5bba469fe)

The pipeline was successfully executed and the Tekton Hub Task integrated:<br>

![8 pipeline succeeded](https://github.com/user-attachments/assets/da2d626b-01e5-4f06-89a4-a1a43c568a2b)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Task 5 - Integrating Linting and Unit Test Automation
Two further tasks in the pipeline (folder: /labs/04_unit_test_automation/) are replaced, which previously acted as placeholders: lint and tests.<br>
<br>
First the lint task.<br>
Flake8 is used for the linting. There is already a predefined task for this in the Tekton Hub, which will be installed:<br>

![1 installing flake8](https://github.com/user-attachments/assets/09e86e6a-d7f3-4a9c-a3b1-3d0e4c34c62f)

The existing task reference in the pipeline is adapted and the corresponding required task parameters are implemented:<br>

![2 implemented pipeline yaml labs04](https://github.com/user-attachments/assets/0a6e1168-c994-4372-b54c-7a437e4b3671)

The output after applying to the cluster with the following command:<br>

```
kubectl apply -f pipeline.yaml
```

![3 apply pipeline yaml](https://github.com/user-attachments/assets/189e0932-d56f-4e29-9bbe-acfea263e8f2)

If you run the pipeline with the following command, you will see that the new task is working and is being executed:<br>

```
tkn pipeline start cd-pipeline \
    -p repo-url="https://github.com/christian-schw/cicd-practice-project.git" \
    -p branch="main" \
    -w name=pipeline-workspace,claimName=pipelinerun-pvc \
    --showlog
```

![4 running pipeline with flake8 task](https://github.com/user-attachments/assets/96285cfb-5f10-4cdf-af1e-6f992d3be3d2)

Linting is done, now the unit test task will be implemented.<br>
<br>
The testing framework nose is used.<br>
However, there is nothing ready-made for this in the Tekton Hub.<br>
This means that I have to define this task myself:<br>

![5 adding nose task](https://github.com/user-attachments/assets/74ffb9f6-2347-4265-b567-b6232d97dcfd)

The existing task reference in the pipeline is adapted and the corresponding required task parameters are implemented:<br>

![6 changing taskref in pipeline yaml](https://github.com/user-attachments/assets/cf369b01-a278-412f-a67e-0128ac3ae93a)

The changes are then applied to the cluster with the following command:<br>

```
kubectl apply -f pipeline.yaml
```

The output after running the pipeline with the following command:<br>

```
tkn pipeline start cd-pipeline \
    -p repo-url="https://github.com/christian-schw/cicd-practice-project.git" \
    -p branch="main" \
    -w name=pipeline-workspace,claimName=pipelinerun-pvc \
    --showlog
```

![7 running pipeline](https://github.com/user-attachments/assets/1a3e745c-5864-459e-a6ee-bf528e20cd4e)

The status of the PipelineRun object is succeeded.<br>
Everything works as intended!<br>

![8 status succeeded pipelinerun](https://github.com/user-attachments/assets/0525c7b3-5d86-4689-8329-3f6c1570619d)


<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Task 6 - Building an Image
The next placeholder task in the pipeline to be replaced is the build task.<br>
Before the application can be deployed, it's necessary to build a Docker image and push it to an image registry (in this case: OpenShift Image Registry).<br>
The Tekton Hub buildah task is used for this.<br>
<br>
First of all, it is necessary to check whether the task has already been installed in the cluster.<br>
This step was previously omitted in the previous tasks (for learning reasons).<br>
<br>
Tasks that are available for pipelines in the entire cluster are called ClusterTasks in Tekton.<br>
According to the Tekton documentation, ClusterTasks are deprecated and cluster resolvers should be used instead.<br>
A ClusterTask is used / required in the practice project, so a ClusterTask is also used here.<br>
<br>
The output after running the pipeline with the following command:<br>

```
tkn clustertask ls
```

![1 Check for buildah ClusterTask](https://github.com/user-attachments/assets/1e3041d1-b1f7-4cc4-aca0-0bf567902416)

The buildah task is listed. This means that it has already been installed and can be used for the pipeline.<br>
The task reference in the pipeline is then changed to the buildah task (folder: /labs/05_build_an_image/):<br>

![2 part 1 of changing pipeline yaml](https://github.com/user-attachments/assets/67606e1c-de3b-46b5-960a-ba380f7c2d73)

![2 part 2 of changing pipeline yaml](https://github.com/user-attachments/assets/b45b3d26-b91d-4839-8eba-fc3336bdfcbb)

The changes are then applied to the cluster with the following command:<br>

```
kubectl apply -f pipeline.yaml
```

It has also been checked whether the PVC for the workspace exists.<br>
The output:<br>

![3 applying pipeline and verifying pvc](https://github.com/user-attachments/assets/8a8fec69-9635-4124-831c-645f2d255e50)

The extended pipeline is now executed with the following command and the logs are examined:<br>

```
tkn pipeline start cd-pipeline \
    -p repo-url="https://github.com/christian-schw/cicd-practice-project.git" \
    -p branch=main \
    -p build-image=image-registry.openshift-image-registry.svc:5000/$SN_ICR_NAMESPACE/tekton-lab:latest \
    -w name=pipeline-workspace,claimName=pipelinerun-pvc \
    --showlog
```

![4 running pipeline](https://github.com/user-attachments/assets/fdcef62c-886d-440b-9493-6c9a9f7427b8)

To make sure that everything worked, we also check whether the image exists in the OpenShift image registry - and yes, it does! Everything fits.<br>

![5 verifying image in openshift image registry](https://github.com/user-attachments/assets/cfbd3bf6-c8c7-45d3-a540-daa11c12303c)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Task 7 - Deploy to OpenShift
The last step of this pipeline: Deploy the Docker image to an OpenShift cluster.<br>
There is an already defined task for this in the Tekton Hub: openshift-client.<br>
<br>
First check whether the (cluster) task openshift-client is already installed.<br>
The output after the following command:<br>

```
tkn clustertask ls
```

![1 check for openshift-client clustertask](https://github.com/user-attachments/assets/f97518e4-20ec-4800-9d3c-d8035c0100ab)

It's already installed.<br>
The task reference in the pipeline is then changed to the openshift-client task (folder: /labs/06_deploy_to_kubernetes/):<br>

![2 part 1 change pipeline yaml](https://github.com/user-attachments/assets/66778e81-cb64-4978-b11a-689d99607f86)

![2 part 2 change pipeline yaml](https://github.com/user-attachments/assets/f1d9bff5-a6e9-4681-a25a-1f46344685ae)

The extended pipeline is now executed with the following command and the logs are examined:<br>

```
tkn pipeline start cd-pipeline \
    -p repo-url="https://github.com/christian-schw/cicd-practice-project.git" \
    -p branch=main \
    -p app-name=hitcounter \
    -p build-image=image-registry.openshift-image-registry.svc:5000/$SN_ICR_NAMESPACE/tekton-lab:latest \
    -w name=pipeline-workspace,claimName=pipelinerun-pvc \
    --showlog
```

![3 running pipeline yaml](https://github.com/user-attachments/assets/b885e717-6936-4095-8f71-2e306d728e9f)

Finally, check whether the deployment has worked.<br>

![4 verifying successful deployment](https://github.com/user-attachments/assets/1f05864c-145c-48eb-aa0e-a8b7ea3bd1d1)

The pod of the deployment is running which means the application has been successfully deployed!<br>
The pipeline is now fully implemented and the practice project is complete.<br>
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


## Getting Started
The code was only executable with the help of the IBM Cloud IDE.<br>
The IDE had many necessary tools and accesses preconfigured. These include, for example, Kubernetes installation or IBM Cloud Container Registry.
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>



## Contact
If you have any questions, please feel free to reach out via email: christian-schwanse (at) gmx.net<br>
<p align="right">(<a href="#readme-top">back to top</a>)</p>
