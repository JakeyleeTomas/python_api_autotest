import json
from testcases.department import Department
import pytest
import yaml


# python运行无结果，点击edit configrations进行编辑 删除之前的记录
class Test_Department:
    def setup_class(self):
        conf = yaml.load(open("config.yml"))
        secret = conf["department_secret"]
        self.department = Department(secret=secret)

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("name, name_en, parentid, department_id", [
        ("广州研发中心1111111111111111111111111111111111111111111111111111111111111111111111111", "GZYF1", 1, 4),
        ("广州研发中心2", "GZYF5", 1, 5)])
    def test_create_department(self, name, name_en, parentid, department_id):
        result = self.department.create_department(name, name_en, parentid, department_id)
        print(result.json())
        if len(name) > 32:
            assert result.json()["errcode"] == 40058
        else:
            assert result.json()["errcode"] == 0

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("name, name_en, parentid, department_id", [("深圳研发", "SZYF", 1, 5)])
    def test_update_department(self, name, name_en, parentid, department_id):
        # 新增部门-》查找部门-》断言
        # result = self.department.update_department(self, name, name_en, parentid, department_id)要去掉self
        result = self.department.update_department(name, name_en, parentid, department_id)
        assert result.json()["errmsg"] == "updated"

    @pytest.mark.run(order=3)
    def test_search_department(self):
        result = self.department.search_department(1)
        r2 = result.json()
        print(json.dumps(r2, ensure_ascii=False))
        assert result.json()["errmsg"] == "ok"
        name_list = self.department.jsonpath_res(r2, "$..name")
        department_name = self.department.jsonpath_res(r2, "$..department[?(@.id==5)].name")[0]
        assert "深圳研发" in name_list
        assert department_name == "深圳研发"

    @pytest.mark.run(order=4)
    def test_delete_department(self):
        result = self.department.delete_department(5)
        assert result.json()["errmsg"] == "deleted"


