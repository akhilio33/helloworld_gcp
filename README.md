1. Create a project directory with the following folder structure

   - functions
     - function_01.py
     - [one function/file for each Cloud Function to be deployed]
   - run
     - jobs
       - job_01.py
       - Dockerfile_01
       - [one function/file and respective Dockerfile for each Cloud Run Job to be deployed]
   - helpers
     - helper functions
   - main.py
   - cloudbuild.yaml
   - requirements.txt

2. File details

   - functions/function_01.py - [Cloud Functions](https://cloud.google.com/functions/docs/writing/write-event-driven-functions)
   - run/jobs/job_01.py - [Cloud Run job](https://cloud.google.com/run/docs/quickstarts/jobs/build-create-python#:~:text=jobs%0Acd%20jobs-,Create,-a%20main.py)
   - run/jobs/Dockerfile_01
     - [deploying a web app](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/run/helloworld/Dockerfile)
     - [running a python script](https://www.geeksforgeeks.org/how-to-run-a-python-script-using-docker/)
   - cloudbuild.yaml
     - [Cloud Function steps](https://cloud.google.com/build/docs/deploying-builds/deploy-functions?hl=en_US#yaml)  
        i. step 1 - define the environment and install requirements  
        ii. steps 2+ - create a step for a each function in functions/main.py to be deployed as a Cloud Function  
          - [Trigger the Cloud Function with Pub/Sub and Cloud Scheduler](https://cloud.google.com/scheduler/docs/tut-pub-sub#create_a_job)'
     - [Cloud Run Job steps](https://cloud.google.com/build/docs/deploying-builds/deploy-cloud-run?hl=en_US)  
        iii. step 3 - build the container image using docker via cloud build  
        iv. step 4 - push the container image to Container Registry  
        v. step 5 - deploy container image to Cloud Run - on first run, utilize 'create' argument; on subsequent run, utilize 'update' argument
        vi. steps 6+ - repeat steps 3-5 for each Cloud Run Job to be deployed

3. Submit the build by running the following command within the project root directory, where REGION is the same region in cloudbuild.yaml
   << gcloud builds submit --region=REGION >>

4. Executing the Cloud Run job
   - manually executing - go to Cloud Run in Cloud Console, select the job, and then press “EXECUTE” along the top bar
   - [executing the job on a schedule](https://cloud.google.com/run/docs/execute/jobs-on-schedule#console)

5. [Connect Cloud build to a Git repository](https://cloud.google.com/build/docs/automating-builds/github/connect-repo-github)

6. [Set up continous deployment](https://cloud.google.com/run/docs/continuous-deployment-with-cloud-build)
