# import json
# import os
# import random
# import sys
# import time

import sys
sys.path.append('../..')
import wrappers.wrapper_test


# Define main script

def hello_run():
  print(f"Hello World!! - from run/jobs/hello_run")

  wt = wrappers.wrapper_test.testObject()
  wt.test_func('tst str passed to wrapper test_func from run/jobs/job_test.hello_run')


# # Start script
# if __name__ == "__main__":
#   try:
#     hello_run()
#   except Exception as err:
#     message = f"{str(err)}"
#     print(message)