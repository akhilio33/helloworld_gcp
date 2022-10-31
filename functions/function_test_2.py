# import json
# import os
# import random
# import sys
# import time
import sys
sys.path.append('..')

import wrappers.wrapper_test

def hello_func_2():
  print(f"Hello World! - from functions/function_test.hello_func_2")

  wt = wrappers.wrapper_test.testObject()
  wt.test_func('tst str passed to wrapper test_func from functions/function_test.hello_func_2')

# # Start scriptgit a
# if __name__ == "__main__":
#   try:
#     hello_func()
#   except Exception as err:
#     message = f"{str(err)}"
#     print(message)
