# import wrappers.wrapper_test
import functions.function_test
import run.jobs.job_test
import pandas as pd


def call_func(event, context):
  # functions.function_test.hello_func()
  # data = ['hello', 'from', 'main.call_func']
  # df = pd.DataFrame(data, columns=['test'])
  # print(df)
  print("call_func success")


def call_job():
  run.jobs.job_test.hello_run()
  data = ['hello', 'from', 'main.call_job']
  df = pd.DataFrame(data, columns=['test'])
  print(df)
