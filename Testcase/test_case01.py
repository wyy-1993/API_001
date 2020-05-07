#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:简凡
@file: test_case01.py
@time: 2020/02/05  15:33
"""
import json
import re
import unittest
from ddt import ddt, data
# import ddt
from Conf import testfile_path
from Common.Mylog import Mylog
from Common.excel_Nosql import Noexcel
from Common.New_http import NewHttp


file_path = testfile_path.test_data_path
result_path = testfile_path.test_result_path
case_list = Noexcel(file_path, "test_data").read_file()
logging = Mylog()
TOKENS = None

@ddt
class TestCase1(unittest.TestCase):
    def setUp(self):
        self.headers = {"Content-Type": "application/json",
                        "Authorization": "Bearer %s" % TOKENS}
        self.testdata = Noexcel(testfile_path.test_data_path, 'test_data')
        self.passfile = Noexcel(testfile_path.test_result_path, 0)
        self.failfile = Noexcel(testfile_path.test_result_path, 1)
        logging.info("开始执行测试")

    @data(*case_list)
    def test_case(self, data):
        global res, relist, TOKENS
        assert_code = data['assert_code']
        assert_content = data['assert_content']
        url = data['url']
        param = data['param']
        count = url.count("$url")  # 统计url中有几个变量
        regular = data['regular']

        if regular!= None:
            relist = regular.split(",")

        if count == 0:
            url = url
        else:
            for i in range(0, count):
                pattern = relist[i]
                a = re.findall(pattern, res.text)
                # 将列表类型的a 转化为 字符串类型
                a = "".join(a)
                newurl = url.replace('$url', a, 1)
                url = newurl

        logging.info("执行的是第%s条用例" % data['case_id'])
        logging.info("测试用例标题：%s" % data['case_name'])
        logging.info('接口请求地址是：%s' % url)
        logging.info('接口请求参数是：%s' % param)
        logging.info('接口请求方式是：%s' % data['method'])
        logging.info("接口请求头是 %s" % self.headers)

        res = NewHttp(url=url, headers=self.headers).http_method(data['method'], params=param)
        print(res.text)
        if '"token"' in res.text:
            print("diyici")
            TOKENS = res.json()['payload']["token"]
            print("获取token成功，token=%s" % TOKENS)

        try:
            self.assertIn(str(assert_code), json.dumps(res.status_code))

            try:
                self.assertIn(str(assert_content), res.text)
                result = 'PASS'
                self.passfile.Write_pass(url, data['method'], param, str(res.json()), result)
            except AssertionError as err:
                result = 'FAIL'
                self.failfile.Write_fail(url, data['method'], param, str(res.json()), result)
                logging.error("报错的信息是%s" % err)
                raise AssertionError("报错的信息是%s" % err)
        except AssertionError as err:
            result = 'FAIL'
            self.failfile.Write_fail(url, data['method'], param, str(res.json()), result)
            logging.error("报错的信息是%s" % err)
            raise AssertionError("报错的信息是%s" % err)

    def tearDown(self):
        logging.info("测试结束")
