# coding=utf-8

"""
运行所有的测试用例并发送 自动化报告
"""
#from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
#
from email.mime.multipart import MIMEMultipart
from email.header import Header
import HTMLTestRunner
import unittest
import smtplib
import time
import os

import sys
reload(sys)
sys.setdefaultencoding('utf8')   # 网上方法,解决unicodeError, ascii can't

#==============定义发送带有附件邮件的==========
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    # TODO 提取接收者的邮箱
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("Auto Test Report", 'utf-8')

    # 发送的附件
    att = MIMEText(mail_body, 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename =Result.html'

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Auto Test Report'
    msgRoot.attach(att)



    smtp = smtplib.SMTP()
    # 需要配置邮箱,才开发送
    smtp.connect('smtp.sina.com')
    smtp.login('xiaolong_8405@sina.com', 'chen3460725')
    smtp.sendmail('xiaolong_8405@sina.com', '15010968405@163.com', msgRoot.as_string())
    smtp.quit()
    print('email has send out!')


#============查找测试报告目录,找到最新的测试文件========

def new_report(testreport):

    lists = os.listdir(testreport) # 返回指定路径下的文件和文件夹列表
    lists.sort(key=lambda fn: os.path.getmtime(testreport + '\\' + fn))
    #sort sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
    file_new = os.path.join(testreport, lists[-1]) # os.path.join连接目录和文件名
    return file_new


if __name__ == '__main__':
    # 时间戳
    now = time.strftime('%Y-%m-%d %H_%M_%S')

    # path 不对会IO Error
    filename = 'D:\\Code\\Python\\AutoTestFrame\\bbs\\report\\' + now + '_result.html'

    fp = open(filename, 'wb')
    # 测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Sina login Auto Test Report',
                            description='Env:windows 10 Browser:chrome')
    # 查找 test  case
    discover = unittest.defaultTestLoader.discover('D:\\Code\\Python\\AutoTestFrame\\bbs\\test_case', pattern='*_sta.py')

    runner.run(discover)
    fp.close()
    file_path = new_report('D:\\Code\\Python\\AutoTestFrame\\bbs\\report\\')  # 查找新生成的报告
    print file_path
    send_mail(file_path)                     # 发送邮件
