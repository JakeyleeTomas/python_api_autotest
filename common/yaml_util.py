# 读取yaml文件
import os

import yaml


# 读取yaml文件
def read_yaml(key):
    with open(os.getcwd() + '/extract.yml', encoding="UTF-8") as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[key]


# 写入yaml文件
def write_yaml(data):
    with open(os.getcwd() + '/extract.yml', encoding="UTF-8", mode="a") as f:
        value = yaml.dump(data, stream=f, allow_unicode=True)
        return value


# 清空yaml文件
def clean_yaml():
    with open(os.getcwd() + '/extract.yml', encoding="UTF-8", mode='w') as f:
        f.truncate()


# 读取测试用例yaml数据
def read_testcases_yaml(yaml_name):
    with open(os.getcwd() + '\\testcases\\' + yaml_name, encoding="UTF-8") as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value
