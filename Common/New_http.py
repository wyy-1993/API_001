#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:简凡
@file: New_http.py
@time: 2020/02/04  14:23
"""
"""
主要是用于封装http请求，目前仅支持 post、get、put、delete四种请求方式，其他暂不支持
"""

import requests

class NewHttp:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def http_method(self, method, params=None):
        global res
        if method.upper() == 'GET':
            # get参数，目前列举最常见的param、headers
            res = requests.get(self.url, eval(params), headers=self.headers)
        elif method.upper() == "POST":
            # 关于此处，传参是json还是data，与参数类型有关，一般是 Application/json，都是用参数json
            res = requests.post(self.url, json=eval(params), headers=self.headers)
        elif method.upper() == "PUT":
            res = requests.put(self.url, json=eval(params), headers=self.headers)

        elif method.upper() == "DELETE":
            res = requests.delete(self.url)
        else:
            print("请求方式暂不支持")
        return res


# if __name__ == '__main__':
#     url = "https://dcp.deepexi.top/dcp-api/api/v1/users/login?tenantId=&userId="
#     param = {"channel": "pms", "code": "deepexi", "username": "18826478943", "password": "abcd1234"}
#     headers = {"User-Agent": "Mozilla/5.0",
#                "Content-Type": "application/json"}
#     t = NewHttp(url, headers).http_method("post", param)
#     print(t.json())
#     print(t.headers)





