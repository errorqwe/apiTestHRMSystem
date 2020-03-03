import json
import pymysql

from app import BASE_DIR


def assert_emp(self, response, statu_code, success, code, message):
    self.assertEqual(statu_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))


def login_data():
    filename = BASE_DIR + "/data/login.json"

    with open(filename, encoding="utf8") as f:
        jsonData = json.load(f)

    result_list = []

    for case in jsonData:
        mobile = case.get("mobile")
        password = case.get("password")
        http_code = case.get("http_code")
        success = case.get("success")
        code = case.get("code")
        message = case.get("message")
        result_list.append((mobile, password, http_code, success, code, message))

        # result_list.append(tuple(case.values()))

    return result_list


def add_emp():
    filename = BASE_DIR + "/data/emp.json"

    with open(filename, encoding="utf8") as f:
        jsonData = json.load(f)

    result_list = []

    add_data = jsonData.get("add_emp")

    username = add_data.get("username")

    mobile = add_data.get("mobile")

    status_code = add_data.get("status_code")

    success = add_data.get("success")

    code = add_data.get("code")

    message = add_data.get("message")

    result_list.append((username, mobile, status_code, success, code, message))

    return result_list


def query_emp():
    filename = BASE_DIR + "/data/emp.json"

    with open(filename, encoding="utf8") as f:
        jsonData = json.load(f)

    result_list = []

    query_data = jsonData.get("query_emp")

    status_code = query_data.get("status_code")

    success = query_data.get("success")

    code = query_data.get("code")

    message = query_data.get("message")

    result_list.append((status_code, success, code, message))

    return result_list


def modify_emp():
    filename = BASE_DIR + "/data/emp.json"
    with open(filename, encoding="utf8") as f:
        jsonDate = json.load(f)

    result_list = []

    modify_data = jsonDate.get("modify_emp")

    username = modify_data.get("username")

    status_code = modify_data.get("status_code")

    success = modify_data.get("success")

    code = modify_data.get("code")

    message = modify_data.get("message")

    result_list.append((username, status_code, success, code, message))

    return result_list


if __name__ == "__main__":
    login_data()

    add_emp()

    query_emp()

    modify_emp()


# 封装数据库
class DBUtils:
    # 初始化类时要运行的代码
    def __init__(self, host="182.92.81.159", user="readuser", password="iHRM_user_2019", database="ihrm"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    # 代表使用with语法时进入函数时会先运行enter的代码
    def __enter__(self):
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        # 获取游标
        self.cursor = self.conn.cursor()
        return self.cursor

    # 代表退出with语句块时会运行exit的代码
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 关闭游标和关闭连接
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()


