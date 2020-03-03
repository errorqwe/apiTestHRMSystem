import requests
import logging
import unittest
from utils import login_data


from parameterized import parameterized

from api.login_api import LoginApi
from utils import assert_emp


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login_api = LoginApi()

    def tearDown(self):
        pass


    # 测试登陆成功
    @parameterized.expand(login_data)
    def test01_login(self,mobile, password, http_code, success, code, message):
        response = self.login_api.login(mobile, password)
        logging.info("登陆结果:{}".format(response.json()))
        assert_emp(self, response, http_code, success, code, message)