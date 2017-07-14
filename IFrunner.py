#coding:utf-8
__author__ = 'FanGu'
from common.interface_init import *
from common.load_cases import LoadCases
from common.exec_Suitecase import ExecSuiteCase

if __name__=="__main__":
    if isinstance(interface_init.initial,Initialization)!=True:
        Init()
    testSuite=LoadCases.get_cases(interface_init.initial.testcase)
    execSuite=ExecSuiteCase()
    execSuite.exec_cases(testSuite)
