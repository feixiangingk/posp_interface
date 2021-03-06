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


    @unittest.skip("skip")
    @data(execExcel.get_info_ddt("interface11")[1])
    def test_interface11(self,excel_info):
        if excel_info =='placeholder':
            self.logger.info("CaseInterface11.test_interface11|data drivern:skip this placeholder case!")
            return True
        case_index=excel_info['case_index']

        #接口用例为N则不执行直接成功
        if excel_info['exec'] in ['N','n']:
            self.logger.info('CaseInterface11.test_interface11|data drivern:skip this use case!')
            return 'success'


        #从接口用例信息读取的断言信息，用于断言
        assert_code=excel_info.get("re-code",False)
        assert_tradeStatus=excel_info.get("re-tradeStatus",False)
        assert_accountFlag=excel_info.get("accountFlag",False)
        assert_bankFlag=excel_info.get("bankFlag",False)
        assert_pwdFlag=excel_info.get("pwdFlag",False)


        #封装一个GetRequestInfo类，用于获取接口参数信息
        getRequestInfo=GetRequestInfo(self.initial)
        url,headers,datas=getRequestInfo.get_post_info(self.interfaceId,excel_info)


        # 记录post出去的params
        self.logger.info('CaseInterface11.test_interface11 index {index} request is :{one}'.format(index=case_index,one=datas))
        #执行POST请求
        response=self.s.post(url=url,data=datas,headers=headers)

        # 记录返回的response
        self.logger.info("CaseInterface11.test_interface11 index {index} response is :{one}".format(index=case_index,one=response.text))

        try:
            if str(response.json().get("code"))!=assert_code:
                self.logger.info("CaseInterface12.test_interface12|re-code is {one};expection is {two}".format(one=str(response.json().get("code")),two=assert_code))
                interface_init.initial.result.append((case_index, 'Fail', response.text))
                return "Fail"
            #如果返回状态码不是200，则把msg写进日志里
            elif str(response.json().get("code"))==assert_code:
                if assert_code=="200":
                    self.assertEqual(str(eval(response.json().get('data')).get('tradeStatus')), assert_tradeStatus)
                    if assert_accountFlag not in [False, ""]:
                        self.assertEqual(str(eval(response.json().get('data')).get('accountFlag')), assert_accountFlag)

                    if assert_bankFlag not in [False, ""]:
                        self.assertEqual(str(eval(response.json().get('data')).get('bankFlag')),
                                         assert_bankFlag)

                    if assert_pwdFlag not in [False, ""]:
                        self.assertEqual(str(eval(response.json().get('data')).get('pwdFlag')),
                                         assert_pwdFlag)
                interface_init.initial.result.append((case_index, 'success', 'OK'))


        #将错误异常捕获并抛出
        except AssertionError as e:
            interface_init.initial.result.append((case_index,'Fail',str(e)))
            self.logger.info("CaseInterface12.test_interface12 index {index} error is {error}".format(index=case_index,error=str(e)))
            raise e



    # @unittest.skip("11")
    @data(execExcel.get_info_ddt("interface11")[111],
          execExcel.get_info_ddt("interface11")[112],
          execExcel.get_info_ddt("interface11")[113],
          execExcel.get_info_ddt("interface11")[114],
          execExcel.get_info_ddt("interface11")[115],
          execExcel.get_info_ddt("interface11")[116],
          execExcel.get_info_ddt("interface11")[117],
          execExcel.get_info_ddt("interface11")[118],
          execExcel.get_info_ddt("interface11")[119],
          execExcel.get_info_ddt("interface11")[120])
    def test_get_message(self, excel_info):
        if excel_info == 'placeholder':
            self.logger.info("CaseInterface11.test_interface11|data drivern:skip this placeholder case!")
            return True
        case_index = excel_info['case_index']

        # 接口用例为N则不执行直接成功
        if excel_info['exec'] in ['N', 'n']:
            self.logger.info('CaseInterface11.test_interface11|data drivern:skip this use case!')
            return 'success'

        # 从接口用例信息读取的断言信息，用于断言
        assert_code = excel_info.get("re-code", False)
        assert_tradeStatus = excel_info.get("re-tradeStatus", False)
        # assert_accountFlag = excel_info.get("accountFlag", False)
        # assert_bankFlag = excel_info.get("bankFlag", False)
        # assert_pwdFlag = excel_info.get("pwdFlag", False)

        # 封装一个GetRequestInfo类，用于获取接口参数信息
        getRequestInfo = GetRequestInfo(self.initial)
        url, headers, datas = getRequestInfo.get_post_info(self.interfaceId, excel_info)

        # 记录post出去的params
        self.logger.info(
            'CaseInterface11.test_interface11 index {index} request is :{one}'.format(index=case_index, one=datas))
        # 执行POST请求
        response = self.s.post(url=url, data=datas, headers=headers)

        # 记录返回的response
        self.logger.info("CaseInterface11.test_interface11 index {index} response is :{one}".format(index=case_index,
                                                                                                    one=response.text))

        try:
            # 如果返回状态码不是200，则把msg写进日志里
            if str(response.json().get("code")) != "200":
                self.logger.info("CaseInterface11.test_interface11|error:{one}".format(one=response.text))

            if str(response.json().get('code')) == "200":
                self.assertEqual(str(eval(response.json().get('data')).get('tradeStatus')), assert_tradeStatus)

                accountFlag=str(eval(response.json().get('data')).get('accountFlag'))
                bankFlag=str(eval(response.json().get('data')).get('bankFlag'))
                pwdFlag=str(eval(response.json().get('data')).get('pwdFlag'))


            # 根据code进行断言，如果断言成功，则在结果集result添加元组，标致为success
            self.assertEqual(str(response.json().get('code')), assert_code)
            interface_init.initial.result.append((case_index, 'success', "accountFlag is {one};bankFlag is {two}; pwdFlag is {three}".format(one=accountFlag,two=bankFlag,three=pwdFlag)))

        # 将错误异常捕获并抛出
        except AssertionError as e:
            interface_init.initial.result.append((case_index, 'Fail', str(e)))
            self.logger.info("CaseInterface11.test_interface11 index {index} error is {error}".format(index=case_index,
                                                                                                      error=str(e)))
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

