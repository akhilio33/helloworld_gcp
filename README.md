1. Create a project directory with the following folder structure:
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

2. File details:
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
        - Use the naming convention sa_your_function_name; for example, if your Cloud Run Job was named hubspot_save_owners(), name its service account sa_hubspot_save_owners \
        ```bash
        gcloud iam service-accounts create SA-NAME \
        --description="DESCRIPTION" \
        --display-name="DISPLAY_NAME" \
        --project="PROJECT_ID"
        ```
        ```bash
gcloud iam service-accounts create sa-gcal-seed-appts-open-bigq \
--description="Service account for Cloud Run Job googlecalendar_seed_appts_open_bigquery()" \
--display-name="sa_googlecalendar_seed_appts_open_bigquery" \
--project="inlaid-particle-342220"
        ```
        - If this Cloud Run Job will be reading data from the Secret Manager, add the role roles/secretmanager.secretAccessor
        ```bash
        gcloud projects add-iam-policy-binding inlaid-particle-342220 \
        --member="serviceAccount:SA-NAME@inlaid-particle-342220.iam.gserviceaccount.com" \
        --role="roles/secretmanager.secretAccessor"
        ```
```bash
gcloud projects add-iam-policy-binding inlaid-particle-342220 \
--member="serviceAccount:sa-gcal-seed-appts-open-bigq@inlaid-particle-342220.iam.gserviceaccount.com" \
--role="roles/secretmanager.secretAccessor"
```
        - If this Cloud Run Job will be reading or writing data to BigQuery, add the Cloud Run Job's service account to the ```bash vitahealth-dw``` project IAM with the roles 'BigQuery Data Editor' and 'BigQuery Job User'.

    ```bash
    
    gcloud projects add-iam-policy-binding utility-tempo-331020 \
    --member="serviceAccount:SA-NAME@inlaid-particle-342220.iam.gserviceaccount.com" \
    --role="roles/bigquery.jobUser"
    gcloud projects add-iam-policy-binding utility-tempo-331020 \
    --member="serviceAccount:SA-NAME@inlaid-particle-342220.iam.gserviceaccount.com" \
    --role="roles/bigquery.dataEditor"

    gcloud projects add-iam-policy-binding utility-tempo-331020 \
    --member="serviceAccount:sa-gcal-seed-appts-open-bigq@inlaid-particle-342220.iam.gserviceaccount.com" \
    --role="roles/bigquery.jobUser"
    gcloud projects add-iam-policy-binding utility-tempo-331020 \
    --member="serviceAccount:sa-gcal-seed-appts-open-bigq@inlaid-particle-342220.iam.gserviceaccount.com" \
    --role="roles/bigquery.dataEditor"
    ```

        - If this Cloud Run Job will be reading or writing data to Cloud SQL, add the Cloud Run Job's service account to the ```bash vitahealth-admin``` project IAM with the role 'Cloud SQL Client'.

    ```bash
    
    gcloud projects add-iam-policy-binding steel-ridge-352016 \
    --member="serviceAccount:SA-NAME@inlaid-particle-342220.iam.gserviceaccount.com" \
    --role="roles/cloudsql.client"

    gcloud projects add-iam-policy-binding steel-ridge-352016 \
    --member="serviceAccount:sa-gcal-seed-appts-open-bigq@inlaid-particle-342220.iam.gserviceaccount.com" \
    --role="roles/cloudsql.client"
    ```

    1. [Build the container using Docker.](https://cloud.google.com/run/docs/building/containers#docker)
        ```bash
        docker build . -t="IMAGE_URL" -f="PATH_TO_DOCKERFILE"
        docker build . -t="gcr.io/inlaid-particle-342220/googlecalendar_seed_appts_open_bigquery" -f="run/jobs/Dockerfile_googlecalendar_seed_appts_open_bigquery"
        ```
    1. [Push the container image to Container Registry](https://cloud.google.com/run/docs/building/containers#:~:text=Push%20the%20container%20image%20to%20Container%20Registry). Image should now be visible in the [Container Registry](https://console.cloud.google.com/gcr/images/inlaid-particle-342220?project=inlaid-particle-342220).
        ```bash
        docker push IMAGE_URL
        docker push gcr.io/inlaid-particle-342220/googlecalendar_seed_appts_open_bigquery
        ```
    1. [Deploy container image to Cloud Run Jobs](https://cloud.google.com/run/docs/create-jobs#job), along with the newly created [respective service account](https://cloud.google.com/run/docs/securing/service-identity#gcloud) and [necessary secrets](https://cloud.google.com/run/docs/configuring/secrets#command-line) exposed as environment variables. Cloud Run Job should now be visible [here](https://console.cloud.google.com/run/jobs?project=inlaid-particle-342220).
        ```bash
        gcloud beta run jobs create JOB-NAME --project="inlaid-particle-342220" --image="IMAGE_URL" --region="REGION" --service-account="SERVICE-ACCOUNT" --set-secrets="ENV_VAR_NAME=SECRET_NAME:VERSION" --set-secrets="ENV_VAR_NAME2=SECRET_NAME2:VERSION" --task-timeout="INT_SECONDS"
gcloud beta run jobs create googlecalendar-seed-appts-open-bigquery \
    --project="inlaid-particle-342220" \
    --image="gcr.io/inlaid-particle-342220/googlecalendar_seed_appts_open_bigquery" \
    --region="us-east4" \
    --service-account="sa-gcal-seed-appts-open-bigq@inlaid-particle-342220.iam.gserviceaccount.com" \
    --set-secrets="GCAL_DOMAINWIDE_DELEGATION_KEY=GCAL_DOMAINWIDE_DELEGATION_KEY:latest" \
    --set-secrets="VITAHEALTH_ADMIN_DB_USER=VITAHEALTH_ADMIN_DB_USER:latest" \
    --set-secrets="VITAHEALTH_ADMIN_DB_PASS=VITAHEALTH_ADMIN_DB_PASS:latest" \
    --set-secrets="VITAHEALTH_ADMIN_DB_NAME=VITAHEALTH_ADMIN_DB_NAME:latest" \
    --set-secrets="VITAHEALTH_ADMIN_INSTANCE_CONNECTION_NAME=VITAHEALTH_ADMIN_INSTANCE_CONNECTION_NAME:latest" \
    --task-timeout="3599"
        ```
    1. Executing the Cloud Run job (single execution)
        ```bash
        gcloud beta run jobs execute JOB-NAME --project="inlaid-particle-342220"
        gcloud beta run jobs execute googlecalendar-seed-appts-open-bigquery --project="inlaid-particle-342220"
        ```
        - manually executing - go to Cloud Run in Cloud Console, select the job, and then press “EXECUTE” along the top bar
    1. [executing the job on a schedule](https://cloud.google.com/run/docs/execute/jobs-on-schedule#command-line)
        ```bash 
          gcloud scheduler jobs create http SCHEDULER_JOB_NAME \
          --location SCHEDULER_REGION \
          --schedule="SCHEDULE" \
          --uri="https://CLOUD_RUN_REGION-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/PROJECT-ID/jobs/JOB-NAME:run" \
          --http-method POST \
          --oauth-service-account-email PROJECT-NUMBER-compute@developer.gserviceaccount.com
        gcloud scheduler jobs create http test-every-min \
          --location us-east4 \
          --schedule="* * * * *" \
          --uri="https://us-east4-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/clever-hangar-351317/jobs/call-job-3:run" \
          --http-method POST \
          --oauth-service-account-email 467888596638-compute@developer.gserviceaccount.com
        ```
    1. Configure
        - [Memory limits](https://cloud.google.com/run/docs/configuring/memory-limits)
    1. Repeat steps iii - ix for each Cloud Run Job that is being deployed for the first time.
        

4. Continuous Deployment and Integration with Github
    1. [Set up continous deployment](https://cloud.google.com/run/docs/continuous-deployment-with-cloud-build)

    1. [Connect Cloud build to a Git repository](https://cloud.google.com/build/docs/automating-builds/github/connect-repo-github)
   
    1. cloudbuild.yaml
        - [Cloud Function steps](https://cloud.google.com/build/docs/deploying-builds/deploy-functions?hl=en_US#yaml)  
            - step 1 - define the environment and install requirements  
            - steps 2+ - create a step for a each function in functions/main.py to be deployed as a Cloud Function  
                - [Trigger the Cloud Function with Pub/Sub and Cloud Scheduler](https://cloud.google.com/scheduler/docs/tut-pub-sub#create_a_job)'
        - [Cloud Run Job steps](https://cloud.google.com/build/docs/deploying-builds/deploy-cloud-run?hl=en_US)  
            - step 3 - build the container image using docker via cloud build  
            - step 4 - push the container image to Container Registry  
            - step 5 - deploy container image to Cloud Run
                - first time deploying Cloud Run Jobs, utilize command line steps outlined aboe
                - on subsequent times, for updating Jobs, utilize 'update' arguement instead of 'create' argument
            - steps 6+ - repeat steps 3-5 for each Cloud Run Job 