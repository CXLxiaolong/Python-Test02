# coding=utf-8

"""
定义driver 文件
"""

from selenium import webdriver
from selenium.webdriver import Remote

# 启动浏览器

def browser(Browser, timeout=30):
    if Browser == "Chrome":
        driver = webdriver.Chrome()
    elif Browser == "Firefox":
        driver = webdriver.Firefox()
    elif Browser == "ie":
        driver = webdriver.Ie()
    elif Browser == "PhantomJS":
        driver = webdriver.PhantomJS()

    """
    远程driver
    host = '127.0.0.1:4444'  # 运行主机: 端口号
    dc  = {"browserName":"chrome"}
    driver = Remote(command_executor="http://" + host + "/wd/hub",
                    desired_capabilities=dc)
    """
    # 设置等待时间
    driver.implicitly_wait(timeout)
    # 设置最大化浏览器
    # TODO logging
    driver.maximize_window()

    return driver

if __name__ == "__main()__":
    print 'start'
    dr = browser("Firefox")
    dr.get("http://www.baidu.com")
    dr.quit()
    print 'end'
