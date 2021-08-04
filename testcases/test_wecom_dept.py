import pytest
import requests

from common.yaml_util import write_yaml, clean_yaml, read_yaml, read_testcases_yaml


class TestWeComDept:
    @pytest.mark.parametrize("caseinfo", read_testcases_yaml("test_wecom_dept.yml"))
    def test_create_department(self, caseinfo):
        url = caseinfo['request']['url']
        params = {
            "access_token": read_yaml("access_token")
        }
        json = caseinfo['request']['json']
        result = requests.request(method="POST", url=url, params=params, json=json)
        assert result.json()["errmsg"] == "created"
        print(result.text)

    # def test_search_department(self):
    #     url = "https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token=" + read_yaml("access_token") + "&id=1"
    #     result = requests.request(method="get", url=url)
    #     print(result)
    #     return result

    # def test_update_department(self):
    #     url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
    #     payload = {
    #         "name": "广州研发中心111",
    #         "name_en": "RDGZ",
    #         "parentid": 1,
    #         "order": 1,
    #         "id": 2
    #     }
    #     result = requests.request(method="POST", url=url, json=payload)
    #     assert result.json()["errmsg"] == "updated"
    #     print(result.text)
    #
    # def test_delete_department(self):
    #     id = 2
    #     url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={id}"
    #     result = requests.request(method="GET", url=url)
    #     assert result.json()["errmsg"] == "deleted"
    #     print(result.text)


