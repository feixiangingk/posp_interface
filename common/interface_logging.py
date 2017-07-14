#coding:utf-8
__author__ = 'FanGu'
from datetime import datetime
import logging,os

class InterfaceLog():

    def __init__(self,project_path):
        self.now=datetime.now().strftime("%Y_%m_%d %H-%M-%S")
        self.date=datetime.now().strftime("%Y_%m_%d")
        log_path = project_path + "\\log\\" + self.date + "\\"

        if os.path.exists(log_path)!=True:
            os.mkdir(log_path)
        log_name=log_path+"interface"+self.now+".log"

        self.logger = logging.Logger('interface_logger')

        # 创建写日志句柄
        fh1 = logging.FileHandler(log_name)
        fh1.setLevel(logging.INFO)

        # 创建控制台输出句柄
        fh2 = logging.StreamHandler()
        fh2.setLevel(logging.DEBUG)

        # 定义日志输出规则
        formatter = logging.Formatter('%(levelname)s| %(asctime)s |%(message)s')

        # 日志句柄绑定规则
        fh1.setFormatter(formatter)
        fh2.setFormatter(formatter)

        # 给logger添加句柄
        self.logger.addHandler(fh1)
        self.logger.addHandler(fh2)



if __name__=="__main__":
    from common.interface_init import Initialization
    logger=InterfaceLog("D:\\quarkscript\\posp_interface")
    print logger.now

