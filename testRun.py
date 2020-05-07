#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:简凡
@file: testRun.py
@time: 2020/02/05  17:23
"""

__author__ = 'xuan'

import time
import unittest
# import HTMLTestRunner

from Common.HTMLTestReportCN import HTMLTestRunner
# from Common.HTMLREPORT import HTMLTestRunner
from Conf import testfile_path
# from Testcase.test_case02 import TestCase2
from Testcase.test_case01 import TestCase1


suite = unittest.TestSuite()  # 放置测试用例
loader = unittest.TestLoader()  # 加载测试用例
suite.addTests(loader.loadTestsFromTestCase(TestCase1))

now = time.strftime('%Y-%m-%d %H_%M_%S')  #时间戳
file_name = testfile_path.report_path + '\\'+now + '.html'

#执行测试用例
with open(file_name, "wb") as file:
    runner = HTMLTestRunner(stream=file, verbosity=2, title="接口测试报告", description="API验证",
                                              tester="jianfan")

    # runner = HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2, title="接口测试报告", description="API验证")
    runner.run(suite)

#t=Email().email_to(file_name)


