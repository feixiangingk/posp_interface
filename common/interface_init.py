#coding:utf-8
__author__ = 'FanGu'

import sys,time
sys.path.append("..")
from config.interface_config import InterfaceConfig
from common.interface_logging import InterfaceLog
import interface_init

initial=None

class Initialization():

    def __init__(self):
        self.__doc__='initialization operation class'
        self.interfaceConfig = InterfaceConfig()

        self.project_path=self.interfaceConfig.project_path
        interfaceLog=InterfaceLog(self.project_path)

        self.html_runner_url =self.project_path+ "\\result\\"

        self.testcase = self.interfaceConfig.testcase

        self.logger=interfaceLog.logger
        self.logger.info("Initialization has complate!")

class Init():
    def __init__(self):
        interface_init.initial=Initialization()

if __name__=="__main__":
    init=Init()
    # print interface_init.initial.interfaceConfig.successful_notice_of_single_recharge
    print getattr(interface_init.initial.interfaceConfig,'successful_notice_of_single_recharge')






