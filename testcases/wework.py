from testcases.baseapi import BaseApi


class WeWork(BaseApi):
    def __init__(self, secret):
        self.token = self.get_token(secret)

    def get_token(self, secret):
        req = {
            "method":"get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": "ww08701ecf7ef7ffc5",
                "corpsecret": secret
            }
        }
        result = self.send(req)
        return result.json()["access_token"]
