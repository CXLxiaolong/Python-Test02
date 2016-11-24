# coding=utf-8

class Page(object):

    '''
    页面 基础类, 用于所有页面的继承
    '''
    bbs_url = 'http://mail.sina.com.cn/'

    def __init__(self, selenium_driver, base_url = bbs_url):

        self.driver = selenium_driver
        self.driver.get(base_url)
     # 元组作为参数,要加*
     # 定位元素
    def find_element(self, *loc):
        # TODO log 捕捉异常
        return self.driver.find_element(*loc)


    # 定位一组元素
    def find_elements(self, *loc):
        # TODO log 捕捉异常
        return self.driver.find_elements(*loc)

    # 执行js
    def script(self, src):
        return self.driver.excute_script(src)

    # TODO 更多 Webdriver 方法