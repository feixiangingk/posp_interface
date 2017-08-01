#coding:utf-8
__author__ = 'FanGu'
import unittest
from common.interface_init import *
from common.read_excel import ExecExcel

class InterFaceCase(unittest.TestCase):

    def __init__(self,methodName="runTest",test_data=None,initial=None):
        super(InterFaceCase, self).__init__(methodName)
        if isinstance(interface_init.initial,Initialization)!=True:
            Init()
        self.initial=interface_init.initial
        self.execExcel=ExecExcel()
        self.test_data=test_data


