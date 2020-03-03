import requests
import logging
import unittest
from api.login_api import LoginApi
from utils import assert_emp


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login_api = LoginApi()

    def tearDown(self):
        pass

    # 创建登陆的测试函数
    # 测试登陆成功
    def test01_login_success(self):
        response = self.login_api.login("13800000002", "123456")
        logging.info("登陆成功:{}".format(response.json()))
        assert_emp(self, response, 200, True, 10000, "操作成功")

    # 测试用户名不存在
    def test02_username_is_not_exist(self):
        response = self.login_api.login("13900000002", "123456")
        logging.info("用户名不存在:{}".format(response.json()))
        assert_emp(self, response, 200, False, 20001, "用户名或密码错误")

    # 测试密码错误
    def test03_password_is_error(self):
        response = self.login_api.login("13800000002", "1234566")
        logging.info("密码错误:{}".format(response.json()))
        assert_emp(self, response, 200, False, 20001, "用户名或密码错误")

    # 测试无参
    def test04_none_params(self):
        response = requests.post("http://182.92.81.159/api/sys/login")
        logging.info("无参:{}".format(response.json()))
        assert_emp(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试！")

    # 用户名为空
    def test05_username_is_null(self):
        response = self.login_api.login2({"mobile": "", "password": "123456"})
        logging.info("用户名为空:{}".format(response.json()))
        assert_emp(self, response, 200, False, 20001, "用户名或密码错误")

    # 密码为空
    def test06_password_is_empty(self):
        response = self.login_api.login2({"mobile": "13800000002", "password": ""})
        logging.info("密码为空:{}".format(response.json()))
        assert_emp(self, response, 200, False, 20001, "用户名或密码错误")

    # 少参-缺少mobile
    def test07_less_mobile(self):
        response = self.login_api.login2({"password": "123456"})
        logging.info("少参-缺少mobile:{}".format(response.json()))
        assert_emp(self, response, 200, False, 20001, "用户名或密码错误")

    # 少参-缺少password
    def test08_less_password(self):
        response = self.login_api.login2({"mobile": "13800000002"})
        logging.info("少参-缺少password:{}".format(response.json()))
        assert_emp(self, response, 200, False, 20001, "用户名或密码错误")

    # 多参-增加1个参数
    def test09_add_params(self):
        response = self.login_api.login2({"mobile": "13800000002", "password": "123456",
                                          "add": "params"})
        logging.info("多参-增加1个参数:{}".format(response.json()))
        assert_emp(self, response, 200, True, 10000, "操作成功")

    # 错误参数
    def test10_error_params(self):
        response = self.login_api.login2({"mbile": "13800000002", "password": "123456"})
        logging.info("错误参数:{}".format(response.json()))
        assert_emp(self, response, 200, False, 20001, "用户名或密码错误")
