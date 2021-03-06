# coding=utf-8
import unittest,time,os,sys
Path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(Path)[0]
sys.path.append(rootPath)
from BeautifulReport import BeautifulReport
from common.readconfig import report_path
from common.send_mail import sendmail

if __name__ == '__main__':

    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    report_title = '测试报告' + now + '.html'
    suite_tests = unittest.defaultTestLoader.discover(".",pattern="test*.py",top_level_dir=None)
    #"."表示当前目录，"*tests.py"匹配当前目录下所有test.py结尾的用例
    reportPath = report_path
    BeautifulReport(suite_tests).report(filename=report_title, description='全部用例测试',report_dir=reportPath,theme="theme_cyan")
    sendmail.send()