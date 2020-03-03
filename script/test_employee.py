import unittest, logging
import requests
from parameterized import parameterized
import app
import pymysql
from api.emp_api import EmpApi
from utils import assert_emp, add_emp, query_emp, modify_emp, DBUtils


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp_api = EmpApi()

    def tearDown(self):
        pass

    # 登陆
    def test01_emp_success(self):
        response_verify = self.emp_api.login("13800000002", "123456")

        logging.info("登陆成功:{}".format(response_verify.json()))

        token = "Bearer " + response_verify.json().get("data")

        logging.info("令牌:{}".format(token))

        headers = {"Content-Type": "application/json", "Authorization": token}

        app.HEADERS = headers

    # 添加员工
    @parameterized.expand(add_emp)
    def test02e_add_emp(self, username, mobile, status_code, success, code, message):
        response_add = self.emp_api.add_emp(username, mobile, app.HEADERS)

        logging.info("添加员工:{}".format(response_add.json()))

        assert_emp(self, response_add, status_code, success, code, message)

        emp_id = response_add.json().get("data").get("id")

        app.ID = emp_id

        logging.info("{}".format(emp_id))

    # 查询员工
    @parameterized.expand(query_emp)
    def test03_query_emp(self,status_code, success, code, message):
        response_query = self.emp_api.emp_query(app.ID, app.HEADERS)

        logging.info("查询员工:{}".format(response_query.json()))

        assert_emp(self, response_query, status_code, success, code, message)

    # 修改员工
    @parameterized.expand(modify_emp)
    def test04_modify_emp(self, username, status_code, success, code, message):
        response_modify = self.emp_api.emp_modify(app.ID, username, app.HEADERS)

        logging.info("修改员工:{}".format(response_modify.json()))

        assert_emp(self, response_modify, status_code, success, code, message)

        # 数据库操作
        with DBUtils() as db:

            sql = "select username from bs_user where id = {};".format(app.ID)

            db.execute(sql)

            result = db.fetchone()

        logging.info("查询修改后用户名为:{}".format(result))

        self.assertEqual(username, result[0])

    # 删除员工
    @parameterized.expand(query_emp)
    def test05_delete_emp(self, status_code, success, code, message):
        response_delete = self.emp_api.emp_delete(app.ID, app.HEADERS)

        logging.info("删除员工:{}".format(response_delete.json()))

        assert_emp(self, response_delete, status_code, success, code, message)
