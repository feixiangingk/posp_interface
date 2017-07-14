#coding:utf-8
__author__ = 'FanGu'

import unittest,sys
sys.path.append("..")
from common.interface_init import *

class LoadCases():

    @staticmethod
    def get_cases(testcase):
        testSuite=unittest.TestSuite()
        loader=unittest.defaultTestLoader

        initial=interface_init.initial
        cases_path = initial.project_path + "\\test_cases"

        if isinstance(testcase,dict)!=True:
            initial.logger.info('LoadCases.get_cases:plz check "testcase" type!')

        if testcase['load_all'] in ['Y','y','*']:
            caselist=loader.discover(cases_path,pattern="*.py")
            for module in caselist:
                testSuite.addTests(module)
            initial.logger.info("get_cases | load all cases!")
            initial.logger.info('get_cases | load case number is %d' % testSuite.countTestCases())
            return testSuite

        if testcase['case_discover']=="" and testcase['case_module'] in ["",[]]:
            print('cases_list is null,plz input cases in appium_config.ini')
            return None

        if testcase['case_module'] not in ["",[],None]:
            for module in testcase['case_module']:
                if module.startswith('#')==False:
                    module="test_cases."+module
                    caselist=loader.loadTestsFromModule(__import__(module,fromlist=True))
                    testSuite.addTests(caselist)

        if testcase['case_discover'] not in ["", [], None]:
            for case_discover in testcase['case_discover']:
                if case_discover.startswith('#')==False:
                    caselist=loader.discover(cases_path,pattern=case_discover)
                    for module in caselist:
                        testSuite.addTests(module)

        initial.logger.info('get_cases | load case number is %d'%testSuite.countTestCases())
        return testSuite



if __name__=="__main__":
    Init()
    LoadCases.get_cases(interface_init.initial.testcase)
