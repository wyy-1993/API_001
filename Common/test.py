import collections
import json
import pandas
import re
import unittest

import requests
from ddt import ddt, data
from Conf import testfile_path
from Common.Mylog import Mylog
from Common.excel_Nosql import Noexcel
from Common.New_http import NewHttp
import HTMLTestRunner

# token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50SWQiOiI0Nzg1NTc4NTgyMjNiYmUxODVhMzE1N2ZlN2JiMDA4ZCIsImlzcyI6IlpEVTR6dHFXU2hkWVIzZTZ2RXdLMTRQNE9DMGJnRHhqIiwidGVuYW50SWQiOiI2YTBkZWExMDZmN2Q3N2NjNDZhZGZjNGQ3MTk0OWMwNCIsImNoYW5uZWwiOiJwbXMiLCJleHAiOjE1ODA4MTE4ODUsImlhdCI6MTU4MDgwNDY4NX0.hZXUXehA2q_jgIZo458Rr748msz13SuF_oE1A3MmOOs"
# token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50SWQiOiI0Nzg1NTc4NTgyMjNiYmUxODVhMzE1N2ZlN2JiMDA4ZCIsImlzcyI6InBJS2s5a0JTSUlFQ3lhWTVuNXI3STZPTzRLNGQ4OXEyIiwidGVuYW50SWQiOiI2YTBkZWExMDZmN2Q3N2NjNDZhZGZjNGQ3MTk0OWMwNCIsImNoYW5uZWwiOiJwbXMiLCJleHAiOjE1ODMxMzkyMzksImlhdCI6MTU4MzEzMjAzOX0.c5LhwX5GAE26fxZoV9ujKqQ5YAFp0-1GWPEMUfdTJ4w"
# headers = {"Content-Type": "application/json","Authorization":"Bearer %s" %token}
# headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50SWQiOiI0Nzg1NTc4NTgyMjNiYmUxODVhMzE1N2ZlN2JiMDA4ZCIsImlzcyI6IlVhek96WFI1MkJZMzdMM0ZWdkVPR05nMG9GVk56ZjNvIiwidGVuYW50SWQiOiI2YTBkZWExMDZmN2Q3N2NjNDZhZGZjNGQ3MTk0OWMwNCIsImNoYW5uZWwiOiJwbXMiLCJleHAiOjE1ODMxNDEwMTgsImlhdCI6MTU4MzEzMzgxOH0.K6S-udZx1SLRcnFAL-8zOPQ1Ceq0cqlB65IbsAQCDD4'}
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50SWQiOiI0Nzg1NTc4NTgyMjNiYmUxODVhMzE1N2ZlN2JiMDA4ZCIsImlzcyI6IkJqOVZYVVYxQ2VJVEMxMmxhZDdOM3F6RVd1VUJjYlpoIiwidGVuYW50SWQiOiI2YTBkZWExMDZmN2Q3N2NjNDZhZGZjNGQ3MTk0OWMwNCIsImNoYW5uZWwiOiJwbXMiLCJleHAiOjE1ODQzNzMzOTAsImlhdCI6MTU4NDM2NjE5MH0.RIAi2946jGu73A_YNFSMy72zznBu3lotNju3UwFrQdE'}
# url = "https://dcp.deepexi.top/dcp-api/api/v1/users/login"
# body = {"channel":"pms","code":"deepexi","username":"18826478943","password":"abcd1234"}
url = "https://dcp.deepexi.top/dcp-api/api/v1/users/changePassword/478557858223bbe185a3157fe7bb008d?tenantId=6a0dea106f7d77cc46adfc4d71949c04&userId=478557858223bbe185a3157fe7bb008d"
# token = None
body = {"password":"abcd1234"}
res = requests.put(url, json=body, headers=headers)
# res = NewHttp(url, headers).http_method(method='post', params=body)

# global token
print(res.text)
print(res.headers)
# if "token" in res.text:
#     # TOKENS = res.json()['payload']["token"]
#     token =res.json()["payload"]["token"]
#     print("oo")
#
#     print(token)










# file_path = testfile_path.test_data_path
# result_path = testfile_path.test_result_path
# case_list = Noexcel(file_path, "test_data").read_file()
# headers = {"Content-Type": "application/json"}
# relist = []

# global res
# for i in range(0, 2):
#     data = case_list[i]
#     url = data['url']
#     param = data['param']
#     count = url.count("$url")  # 统计url中有几个变量
#     regular = data['regular']
#     # print(regular)
#     # print(type(regular))
#     if regular != None:
#         relist = regular.split(",")
#         # print(relist)
#         # print(relist[0])
#
#     if count == 0:
#         url = url
#     # elif count == 1:
#     #     urlnew = data['url'].replace("$url", "test")
#     else:
#         for i in range(0, count):
#             pattern = relist[i]
#             # print(type(pattern))
#             print(pattern)

            # a = re.findall(pattern, res.text)
            # 将列表类型的a 转化为 字符串类型
            # a = "".join(a)
            # print(a)
            # print(type(a))
            # newurl = url.replace('$url', a, 1)
            # print(newurl)
            # url = newurl

    # url = urlnew
    # res = NewHttp(url=url, headers=headers).http_method(data['method'], param)
    # print(res.text)

"""-----------------------------------------------------"""
# datare = case_list[0]
# regular = datare['regular']
# relist = regular.split(",")
# print(regular)
# print(relist)
# print(type(relist))
# print(relist[0])



# count = url.count("$url")  # 统计url中有几个变量
#
# if count == 0:
#     urlnew = data['url']
# elif count == 1:
#     urlnew = data['url'].replace("$url", "test")
# else:
#     for i in range(0, count):
#         urlnew = data['url'].replace('$url', 'test')
#
# url = urlnew
# print(url)
#
# print(type(url))
#
# print(count)
