import unittest

from HTMLTestRunner_PY3 import HTMLTestRunner

from script.test_employee import TestEmployee
from script.test_login import TestLogin
import time
import app
# 实例化suite
suite = unittest.TestSuite()
# 生成测试套件
suite.addTest(unittest.makeSuite(TestEmployee))

suite.addTest(unittest.makeSuite(TestLogin))

# filename = app.BASE_DIR + "/report/report_{}.html".format(time.strftime("%Y%m%d%H%M%S"))

filename = app.BASE_DIR + "/report/ihrm.html".format

with open(filename, "wb") as f:
    runner = HTMLTestRunner(stream=f, title="接口自动化测试", description="v1.0")

    # 执行测试套件
    runner.run(suite)


