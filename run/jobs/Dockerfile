# Copyright 2020 Google, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START cloudrun_helloworld_dockerfile]
# [START run_helloworld_dockerfile]

# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.10-slim
  
# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
WORKDIR /root
COPY . .

# Install production dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# CMD instruction should be used to run the software
# contained by your image, along with any arguments.
CMD [ "python", "job_test.py"]

# [END run_helloworld_dockerfile]
# [END cloudrun_helloworld_dockerfile]