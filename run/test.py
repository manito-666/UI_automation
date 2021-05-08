#encoding:utf-8
import os,sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest,warnings,time
from common.readconfig import *
from util.log.mylog import log
from BeautifulReport import BeautifulReport
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from case.contract import m
# from case.message import community
# from case.image_review import R
# from case.block import Block
warnings.filterwarnings("ignore")


# class TestCase_message(unittest.TestCase):
#     '''内容管理模块'''
#     @classmethod
#     def setUpClass(cls):
#         log().info('******************** 内容管理测试开始 ********************')
#     @classmethod
#     def tearDownClass(cls):
#         log().info('********************  测试结束  ********************')
#
#     def testcase01(self):
#         '''社区官方发布资讯'''
#         result = community.send()
#         self.assertIn("成功", result, "测试失败")

class TestCase_image(unittest.TestCase):
    '''舆论管理'''
    @classmethod
    def setUpClass(cls):
        log().info('******************** 舆论管理测试开始 ********************')
    @classmethod
    def tearDownClass(cls):
        log().info('********************  测试结束  ********************')

    def testcase01(self):
        '''社区动态审核'''
        result=m.check()
        self.assertIn("操作成功",result,"测试失败")

    # def testcase02(self):
    #     '''图片审核'''
    #     result=m.review()
    #     self.assertIn('通过',result,'测试失败')
#
# class TestCase_contract(unittest.TestCase):
#     '''用户管理'''
#     @classmethod
#     def setUpClass(cls):
#         log().info('******************** OA测试开始 ********************')
#     @classmethod
#     def tearDownClass(cls):
#         log().info('********************  测试结束  ********************')
#
#     def testcase01(self):
#         '''封禁用户'''
#         result=Block.block()
#         self.assertIn("成功",result,"测试失败")
#
#     def testcase02(self):
#         pass


if __name__=='__main__':
    suite = unittest.TestSuite()
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    report_title = 'ui测试报告' + now + '.html'
    testcases = unittest.TestLoader().loadTestsFromTestCase(TestCase_image)
    suite.addTest(testcases)
    BeautifulReport(testcases).report(filename=report_title, description="测试",report_dir=report_path,theme="theme_candy")

