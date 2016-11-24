# coding=utf-8

'''
登录功能页面
'''

from time import sleep
import unittest, random, sys
sys.path.append('./models')
sys.path.append('./page_obj')
from models import myunit, function
from page_obj.LoginPage import login

class LoginTest(myunit.MyTest):
    '''
    社区登录测试
    '''
    def test_login01(self):
        '''用户名/密码 登录 '''
        po = login(self.driver)
        function.insert_img(self.driver, "user_pwd_login00.jpg")
        po.login_username().send_keys('xiaolong_8405@sina.com')
        po.login_password().send_keys('chen3460725')
        function.insert_img(self.driver, "user_pwd_login01.jpg")
        sleep(3)

    def test_login02(self):
        '''用户名正确,密码为空'''
        login(self.driver)
        function.insert_img(self.driver, 'user_pwd_empty01.png')
        sleep(3)

if __name__ == '__main__':

    '''
    单独验证一条case通过
    '''
    # 构造 测试集
    suite = unittest.TestSuite
    suite.addTest(LoginTest.test_login01())
    suite.addTest(LoginTest('test_login02'))

    runner = unittest.TextTestRunner
    runner(suite)
