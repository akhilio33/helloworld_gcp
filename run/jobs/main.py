# import json
# import os
# import random
# import sys
# import time

import sys
sys.path.append('..')

import wrappers.wrapper_test

# Define main script
def main():
  print(f"Hello World!!")  

  wt = wrappers.wrapper_test.testObject()
  wt.test_func('tst str')


# Start script
if __name__ == "__main__":
  try:
    main()
  except Exception as err:
    message = f"{str(err)}"
    print(message)
