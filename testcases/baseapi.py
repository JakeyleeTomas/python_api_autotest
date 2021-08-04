import requests
from jsonpath import jsonpath


class BaseApi:
    def send(self, req):
        return requests.request(**req)

    #  一个*号表示解析元组，两个*表示解析字典
    def jsonpath_res(self, obj, expr):
        return jsonpath(obj, expr)
