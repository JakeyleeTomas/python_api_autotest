import pytest
import requests

from common.yaml_util import write_yaml, clean_yaml, read_yaml, read_testcases_yaml


class TestWeComToken:

    @pytest.mark.parametrize("caseinfo", read_testcases_yaml("test_wecom_access_token.yml"))
    def test_get_access_token(self, caseinfo):
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        params = caseinfo['request']['params']
        result = requests.request(method=method, url=url, params=params)
        if "access_token" in result.text:
            token = result.json()["access_token"]
            extract_data = {"access_token": token}
            write_yaml(extract_data)
        print(result.text)

