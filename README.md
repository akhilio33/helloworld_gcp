1. Create a project directory with the following folder structure

   - functions
     - function_01.py
   - run
     - jobs
       - job_01.py
       - Dockerfile_01
   - helpers
     - helper functions
   - main.py
   - cloudbuild.yaml
   - requirements.txt

2. File details

   - functions/function_01.py - [Cloud Functions](https://cloud.google.com/functions/docs/writing/write-event-driven-functions)
      - [one function/file for each Cloud Function to be deployed]
   - run/jobs/job_01.py - [Cloud Run job](https://cloud.google.com/run/docs/quickstarts/jobs/build-create-python#:~:text=jobs%0Acd%20jobs-,Create,-a%20main.py)
      - [one function/file for each Cloud Run Job to be deployed]
   - run/jobs/Dockerfile_01
     - [deploying a web app](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/run/helloworld/Dockerfile)
     - [running a python script](https://www.geeksforgeeks.org/how-to-run-a-python-script-using-docker/)
     - [one Dockerfile for each Cloud Run Job to be deployed]

3. Deploying a new Cloud Run Job
  1. [Set up environment, install Docker, and add the gcloud Docker credential helper](https://cloud.google.com/run/docs/setup)
  1. Open Docker Desktop 
  1. [Create a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#iam-service-accounts-create-gcloud) for each Cloud Run Job to be deployed.
    - Use the naming convention sa_your_function_name; for example, if your Cloud Function was named hubspot_save_owners(), name its service account sa_hubspot_save_owners
    << gcloud iam service-accounts create SA_NAME \
    --description="DESCRIPTION" \
    --display-name="DISPLAY_NAME" >>
    - If this Cloud Run Job will be reading data from the Secret Manager, add the role roles/secretmanager.secretAccessor
    << gcloud projects add-iam-policy-binding PROJECT_ID \
    --member="serviceAccount:SA_NAME@PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/secretmanager.secretAccessor" >>
  1. [Build the container using Docker](https://cloud.google.com/run/docs/building/containers#docker)
      << docker build . -t IMAGE_URL -f  PATH_TO_DOCKERFILE >> docker build . -t gcr.io/clever-hangar-351317/call_job_3 -f run/jobs/Dockerfile_job3
  1. [Push the container image to Container Registry](https://cloud.google.com/run/docs/building/containers#:~:text=Push%20the%20container%20image%20to%20Container%20Registry)
      << docker push IMAGE_URL >>
      docker push gcr.io/clever-hangar-351317/call_job_3
  1. [Deploy container image to Cloud Run Jobs](https://cloud.google.com/run/docs/create-jobs#job), along with the newly created [respective service account](https://cloud.google.com/run/docs/securing/service-identity#gcloud) and [necessary secrets](https://cloud.google.com/run/docs/configuring/secrets#command-line) exposed as environment variables.
    << gcloud beta run jobs create JOB-NAME --image IMAGE_URL --region REGION --service-account SERVICE_ACCOUNT --update-secrets=ENV_VAR_NAME=SECRET_NAME:VERSION>>
    gcloud beta run jobs create call-job-3 --image gcr.io/clever-hangar-351317/call_job_3 --region us-east4
  1. Executing the Cloud Run job (single execution)
    << gcloud beta run jobs execute JOB_NAME >>
    gcloud beta run jobs execute call-job-3
    - manually executing - go to Cloud Run in Cloud Console, select the job, and then press “EXECUTE” along the top bar
  1. [executing the job on a schedule](https://cloud.google.com/run/docs/execute/jobs-on-schedule#command-line)
    <<  
      gcloud scheduler jobs create http SCHEDULER_JOB_NAME \
      --location SCHEDULER_REGION \
      --schedule="SCHEDULE" \
      --uri="https://CLOUD_RUN_REGION-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/PROJECT-ID/jobs/JOB-NAME:run" \
      --http-method POST \
      --oauth-service-account-email PROJECT-NUMBER-compute@developer.gserviceaccount.com
    >>
    gcloud scheduler jobs create http test-every-min \
      --location us-east4 \
      --schedule="* * * * *" \
      --uri="https://us-east4-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/clever-hangar-351317/jobs/call-job-3:run" \
      --http-method POST \
      --oauth-service-account-email 467888596638-compute@developer.gserviceaccount.com
  1. Service Account and secrets
  1. Configure
      - [Memory limits](https://cloud.google.com/run/docs/configuring/memory-limits)
      

4. Continuous Deployment and Integration with Github
   - [Set up continous deployment](https://cloud.google.com/run/docs/continuous-deployment-with-cloud-build)

   - [Connect Cloud build to a Git repository](https://cloud.google.com/build/docs/automating-builds/github/connect-repo-github)
   
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