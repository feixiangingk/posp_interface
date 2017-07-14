#coding=utf-8
from common.interface_init import *
import os


class ExecSuiteCase():


    def __init__(self):
        self.result = interface_init.initial.project_path + "\\result\\"
        # 获取系统当前时间
        self.now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        self.day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        # 定义个报告存放路径，支持相对路径
        self.tdresult = self.result + self.day


    def exec_cases(self,test_case):
        #在这里加载HTMLTestRunner1的原因是，HTMLTestRunner1里面需要inital实例化读取配置文件，延迟调用就能等实例化以后保证有值
        from common.HTMLTestRunner1 import HTMLTestRunner
        if os.path.exists(self.tdresult)!=True:
            os.mkdir(self.tdresult)
        filename = self.tdresult +"\\" + self.now + "_result.html"
        #mail_name = self.tdresult + "\\" + self.now + "_send_mail.html"
        fp = file(filename, 'wb')
        #fp1 = file(mail_name, 'wb')

        # 定义测试报告
        runner = HTMLTestRunner(stream=fp, title=u'posp接口自动化测试报告', description=u'用例详情：',verbosity=2)

        # 运行测试用例
        runner.run(test_case)

        fp.close()

