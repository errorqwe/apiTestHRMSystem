import requests


class EmpApi():
    def __init__(self):
        pass

    def login(self, mobile, password):
        login_url = "http://182.92.81.159/api/sys/login"
        json = {"mobile": mobile, "password": password}
        return requests.post(login_url, json=json)

    def add_emp(self, username, mobile, headers):
        add_emp_url = "http://182.92.81.159/api/sys/user"

        jsonData = {"username": username,
                    "mobile": mobile,
                    "timeOfEntry": "2020-02-02",
                    "formOfEmployment": 1,
                    "departmentName": "酱油2部",
                    "departmentId": "1205026005332635648",
                    "correctionTime": "2020-02-03T16:00:00.000Z"}
        return requests.post(add_emp_url, json=jsonData, headers=headers)

    def emp_query(self, emp_id, headers):
        query_url = "http://182.92.81.159/api/sys/user" + "/" + emp_id

        return requests.get(query_url, headers=headers)

    def emp_modify(self, emp_id, username, headers):
        modify_url = "http://182.92.81.159/api/sys/user" + "/" + emp_id
        return requests.put(modify_url, json={"username": username},
                            headers=headers)

    def emp_delete(self, emp_id, headers):

        delete_url = "http://182.92.81.159/api/sys/user" + "/" + emp_id

        return requests.delete(delete_url, headers=headers)


