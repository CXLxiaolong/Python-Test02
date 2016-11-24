# coding=utf-8

from time import sleep

from selenium.webdriver.common.by import By
from bbs.test_case.page_obj.base import Page


class login(Page):
    '''
    用户登录页面
    '''
    # 定位元素位置 元组
    login_username_loc = (By.ID, 'freename')
    login_password_loc = (By.ID, 'freepassword')
    login_loc = (By.LINK_TEXT, '登录')

    #Element
    def login_username(self):
        return self.find_element(*self.login_username_loc)

    def login_password(self):
        return self.find_element(*self.login_password_loc)

    def login_button(self):
        return self.find_element(*self.login_loc)

    #OpearTion
