from testcases.wework import WeWork


class Department(WeWork):

    def create_department(self, name, name_en, parentid, department_id):
        req = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/create",
            "params": {"access_token": self.token},
            "json": {
                "name": name, "name_en": name_en,
                "parentid": parentid,
                "id": department_id
            }
        }
        result = self.send(req)
        return result

    def delete_department(self, department_id):
        req = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={department_id}"
        }
        result = self.send(req)
        return result

    def update_department(self, name, name_en, parentid, department_id):
        req = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}",
            "json": {
                "name": name,
                "name_en": name_en,
                "parentid": parentid,
                "id": department_id
            }
        }
        result = self.send(req)
        return result

    def search_department(self, department_id):
        req = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}&id={department_id}"
        }
        result = self.send(req)
        return result
