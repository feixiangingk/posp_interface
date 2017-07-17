#coding:utf-8
__author__ = 'FanGu'

import sys,unittest,requests
sys.path.append("..")
from common.interface_case import InterFaceCase
from common.interface_init import *
from common.get_request_info import GetRequestInfo
from common.read_excel import ExecExcel
from ddt import ddt,data,unpack

def get_excel_info():
    if isinstance(interface_init.initial,Initialization)!=True:
        Init()
    execExcel = ExecExcel()
    list_excel_info= execExcel.get_info_ddt('interface09')
    return  list_excel_info


@ddt
class CaseInterface09(InterFaceCase):

    @classmethod
    def setUpClass(cls):

        interface_init.initial.result=[]
        cls.interfaceId='interface09'

    def setUp(self):
        #接口ID，标识唯一接口信息
        self.interfaceId='interface09'
        self.logger=self.initial.logger
        self.s=requests.session()
        # self.result=[]

    @unittest.skip('skip')
    def test_1(self):

        #用例序号，对应excel表格中第几条用例的数据
        case_index=1
        #从excel表格读取的接口用例信息，编号代表第几条用例
        excel_info=self.execExcel.get_info(self.interfaceId)[case_index]


        #接口用例为N则不执行直接成功
        if excel_info['exec'] in ['N','n']:
            self.logger.info('CaseTest.test_1:skip this use case!')
            return 'success'

        #从接口用例信息读取的断言信息，用于断言
        assert_code=excel_info['re-code']
        assert_msg=excel_info['re-msg']

        #封装一个GetRequestInfo类，用于获取接口参数信息
        getRequestInfo=GetRequestInfo(self.initial)
        url,headers,datas=getRequestInfo.get_post_info(self.interfaceId,excel_info)

        #执行POST请求
        response=self.s.post(url=url,data=datas,headers=headers)

        #写日志，并且根据response值做断言
        self.logger.info('Run case:CaseTest.test_1')
        try:
            self.assertEqual(str(response.status_code),assert_code)
            interface_init.initial.result.append((case_index,'success','OK'))
        #将错误异常捕获并抛出
        except AssertionError as e:
            interface_init.initial.result.append((case_index,'Fail',str(e)))
            raise e


    @data(get_excel_info()[1])
    def test_interface09(self,excel_info):
        case_index=excel_info['case_index']

        #接口用例为N则不执行直接成功
        if excel_info['exec'] in ['N','n']:
            self.logger.info('CaseTest.test_interface09|data drivern:skip this use case!')
            return 'success'

        #从接口用例信息读取的断言信息，用于断言
        assert_code=excel_info['re-code']
        assert_msg=excel_info['re-msg']

        #封装一个GetRequestInfo类，用于获取接口参数信息
        getRequestInfo=GetRequestInfo(self.initial)
        url,headers,datas=getRequestInfo.get_post_info(self.interfaceId,excel_info)

        #执行POST请求
        response=self.s.post(url=url,data=datas,headers=headers)

        #写日志，并且根据response值做断言
        self.logger.info('Run case:CaseTest.test_interface09|data drivern')
        try:
            self.assertEqual(str(response.status_code),assert_code)
            interface_init.initial.result.append((case_index,'success','OK'))
        #将错误异常捕获并抛出
        except AssertionError as e:
            interface_init.initial.result.append((case_index,'Fail',str(e)))
            self.logger.info("Run case:CaseTest.test_interface09|data drivern error: %s" %str(e))
            raise e


    def tearDown(self):
        # self.execExcel.write_info(self.interfaceId, self.result)
        pass

    @classmethod
    def tearDownClass(cls):
        execExcel=ExecExcel()
        execExcel.write_info(cls.interfaceId,interface_init.initial.result)



if __name__=="__main__":
    if isinstance(interface_init.initial,Initialization)!=True:
        Init()
    unittest.main()
    # print get_excel_info()[0]
    # print get_excel_info()[1]