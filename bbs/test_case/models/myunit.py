# coding=utf-8
'''
定义 Mytest()类用于继承unittest.TestCase 类, 因为所有的测试类中setUp() 与 tearDown() 方法所做的事情相同,
所以将他们抽象为 Mytest()类,好处在编写测试用例时,不用再考虑这两个类的实现

'''

import unittest
import os
from selenium import webdriver
from driver import browser


class MyTest(unittest.TestCase):
    def setUp(self):
        # TODO config file
        self.driver = browser('Chrome')

    def tearDown(self):
        self.driver.quit()

