import pytest

from common.yaml_util import clean_yaml


@pytest.fixture(scope="session", autouse=True)
def execute_database_sql():
    clean_yaml()
    print("连接数据库")
    yield
    print("断开数据库")
