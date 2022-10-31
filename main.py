import functions.function_test
import functions.function_test_2
# import run.jobs.job_test1
import pandas as pd


def call_func(event, context):
  functions.function_test.hello_func()
  data = ['hello', 'from', 'main.call_func']
  df = pd.DataFrame(data, columns=['test'])
  print(df)


def call_func_2(event, context):
  functions.function_test_2.hello_func_2()
  data = ['hello', 'from', 'main.call_func_2']
  df = pd.DataFrame(data, columns=['test'])
  print(df)


# def call_job():
#   run.jobs.job_test1.main()
#   data = ['hello', 'from', 'main.call_job']
#   df = pd.DataFrame(data, columns=['test'])
#   print(df)
