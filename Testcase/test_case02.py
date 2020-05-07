#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:简凡
@file: test_case02.py
@time: 2020/02/28  18:08
"""
import unittest
from Common.Mylog import Mylog

logging = Mylog()
class TestCase2(unittest.TestCase):
    def setUp(self):

        logging.info("开始执行测试")



    def test_case1(self):
        print("excute test1")


    def test_case2(self):
        print("excute test2")
        raise AssertionError("test2 fail")



    def tearDown(self):
        logging.info("测试结束")