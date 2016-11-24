# coding=utf-8
from selenium import webdriver
import os

'''
创建截图函数,为了保持自动化项目的移植性,采用相对路径将测试截图保存到 .\ report\image 目录中
'''

def insert_img(driver,file_name):

    # os.path.dirname() 获取脚本.py全路径
    base_dir = os.path.dirname(os.path.dirname(__file__))
    # str() 将对象转化为字符串
    base_dir = str(base_dir)
    #   / 替换 \\ replace(oldStr, 'newStr')
    base_dir = base_dir.replace('\\', '/')
   # split 以'/test_case'分割字符串 返回[0]
    base = base_dir.split('/test_case')[0]
    file_path = base + "/report/image/" + file_name

    # 截图
    driver.get_screenshot_as_file(file_path)

if __name__ == '__main__':
    driver = webdriver.PhantomJS()
    driver.get("http://www.baidu.com")
    insert_img(driver, 'baidu.jpg')
    driver.quit()