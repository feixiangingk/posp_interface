#coding:utf-8
__author__ = 'FanGu'

import sys,unittest,requests
sys.path.append("..")
from common.interface_case import InterFaceCase
from common.interface_init import *
from common.get_request_info import GetRequestInfo
from common.read_excel import ExecExcel
from ddt import ddt,data,unpack




@ddt
class CaseInterface11(InterFaceCase):
    execExcel=ExecExcel()


    @classmethod
    def setUpClass(cls):
        interface_init.initial.result=[]
        cls.interfaceId='interface11'


    def setUp(self):
        #接口ID，标识唯一接口信息
        self.interfaceId='interface11'
        self.logger=self.initial.logger
        self.s=requests.session()



    @data(execExcel.get_info_ddt("interface11")[80])
    def test_interface11(self,excel_info):
        if excel_info =='placeholder':
            self.logger.info("CaseTest.test_interface11|data drivern:skip this placeholder case!")
            return True
        case_index=excel_info['case_index']

        #接口用例为N则不执行直接成功
        if excel_info['exec'] in ['N','n']:
            self.logger.info('CaseTest.test_interface11|data drivern:skip this use case!')
            return 'success'

        #从接口用例信息读取的断言信息，用于断言
        assert_code=excel_info['re-code']
        assert_tradeStatus=excel_info['re-tradeStatus']


        #封装一个GetRequestInfo类，用于获取接口参数信息
        getRequestInfo=GetRequestInfo(self.initial)
        url,headers,datas=getRequestInfo.get_post_info(self.interfaceId,excel_info)
        # print datas

        #执行POST请求
        response=self.s.post(url=url,data=datas,headers=headers)

        #写日志，并且根据response值做断言
        self.logger.info('Run case:CaseTest.test_interface11|data drivern datas:{one}'.format(one=datas))
        try:
            #如果返回状态码不是200，则把msg写进日志里
            if str(response.json().get("code"))!="200":
                self.logger.info("Run case:CaseTest.test_interface11|error:{one}".format(one=response.text))

            if str(response.json().get('code')) == "200":
                self.assertEqual(str(eval(response.json().get('data')).get('tradeStatus')), assert_tradeStatus)

            # 根据code进行断言，如果断言成功，则在结果集result添加元组，标致为success
            self.assertEqual(str(response.json().get('code')), assert_code)
            interface_init.initial.result.append((case_index, 'success', 'OK'))

        #将错误异常捕获并抛出
        except AssertionError as e:
            interface_init.initial.result.append((case_index,'Fail',str(e)))
            self.logger.info("Run case:CaseTest.test_interface11|data drivern error: %s" %str(e))
            raise e


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        CaseInterface11.execExcel.write_info(cls.interfaceId,interface_init.initial.result)



if __name__=="__main__":
    if isinstance(interface_init.initial,Initialization)!=True:
        Init()
    unittest.main()
    # module_init=__import__("common.interface_init",fromlist=True)
    # init=getattr(module_init,"Initialization")()
    # print init.html_runner_url

