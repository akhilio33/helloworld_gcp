import pandas as pd


class testObject(object):
  def __init__(self):
    # access secrets
    data = ['hello', 'from', 'wrapper object']
    self.df = pd.DataFrame(data, columns=['test'])

  def test_func(self, str):
    print('wrapper test function works')
    print(self.df)
    print(str)
