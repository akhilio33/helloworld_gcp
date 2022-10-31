# import json
# import os
# import random
# import sys
# import time

import sys
sys.path.append('../..')
import wrappers.wrapper_test

# Define main script


def job1():
  print(f"Hello World!! - from run/jobs/job_test - JOB 1")

  wt = wrappers.wrapper_test.testObject()
  wt.test_func(
      'tst str passed to wrapper test_func from run/jobs/job_test1.main')


# def job2():
#   print(f"Hello World!! - from run/jobs/job_test - JOB 2")

#   wt = wrappers.wrapper_test.testObject()
#   wt.test_func(
#       'tst str passed to wrapper test_func from run/jobs/job_test1.main')

job1()
# job2()
