1. Create a project directory with the following folder structure

functions
main.py
run
jobs
main.py
Dockerfile
cloudbuild.yaml
requirements.txt

2. file details -

functions/main.py - [Cloud Functions example](https://cloud.google.com/functions/docs/writing/write-event-driven-functions)
run/jobs/main.py - [Cloud Run job example](https://cloud.google.com/run/docs/quickstarts/jobs/build-create-python#:~:text=jobs%0Acd%20jobs-,Create,-a%20main.py)
run/jobs/Dockerfile - [deploying a web app example](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/run/helloworld/Dockerfile) - [running a python script example](https://www.geeksforgeeks.org/how-to-run-a-python-script-using-docker/)
cloudbuild.yaml - [Cloud Function steps](https://cloud.google.com/build/docs/deploying-builds/deploy-functions?hl=en_US#yaml)
step 1 - define the environment and install requirements
step 2 - create a step for a each function in functions/main.py that you want to deploy with the following args:
args: [
'functions', 'deploy', 'NAME_OF_FUNCTION',
'--source', './functions/',
'--project', 'PROJECT_ID',
'--runtime', 'python39',
'--region', 'FUNCTION_REGION',
'--memory', 'ALLOCATED_MEMORY',
'--timeout', 'MAX_540s',
'--trigger-topic', '[PUB_SUB_TOPIC_LINKED_WITH_CLOUD_SCHEDULER]'(https://cloud.google.com/scheduler/docs/tut-pub-sub#create_a_job)
] - [Cloud Run steps](https://cloud.google.com/build/docs/deploying-builds/deploy-cloud-run?hl=en_US)
step 3 - build the container image using docker via cloud build
step 4 - push the container image to Container Registry
step 5 - deploy container image to Cloud Run - on first run, utilize 'create' argument; on subsequent run, utilize 'update' argument

3. Submit the build by running the following command within the project root directory, where REGION is the same region in cloudbuild.yaml
   << gcloud builds submit --region=REGION >>

4. Executing the Cloud Run job

- manually executing - go to Cloud Run in Cloud Console, select the job, and then press “EXECUTE” along the top bar
- [executing the job on a schedule](https://cloud.google.com/run/docs/execute/jobs-on-schedule#console)

5. [Connect Cloud build to a Git repository](https://cloud.google.com/build/docs/automating-builds/github/connect-repo-github) [and set up continous deployment](https://cloud.google.com/run/docs/continuous-deployment-with-cloud-build)
