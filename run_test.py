import time, sys
sys.path.append('./testCase')
sys.path.append('/db_initdata')
from HTMLTestRunner import HTMLTestRunner
import unittest
from db_initdata import test_data

test_dir = './testCase'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

if __name__ == "__main__":

    test_data.init_data()
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='Guest Manage system Interface Test Report', description='Implementation Example with:')
    runner.run(discover)
    fp.close()