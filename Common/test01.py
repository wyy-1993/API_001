#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:简凡
@file: test01.py
@time: 2020/03/16  21:25
"""
import unittest

import Common.Mylog

logging = Common.Mylog.Mylog()
class TestCase2(unittest.TestCase):
    def setUp(self):
        self.s = s

        logging.info("开始执行测试")

    def test001(self,a=1,b=2):
        global s
        s1 = a*b
        s = s*s1

