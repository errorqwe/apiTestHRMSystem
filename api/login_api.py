import requests


class LoginApi:
    def __init__(self):
        self.login_url = "http://182.92.81.159/api/sys/login"

    def login(self, mobile, password):
        json = {"mobile": mobile, "password": password}

        return requests.post(self.login_url, json=json)

    def login2(self, jsonData):
        return requests.post(self.login_url, json=jsonData)
