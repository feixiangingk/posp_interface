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
    list_excel_info= execExcel.get_info_ddt('interface11')
    return  list_excel_info


@ddt
class CaseInterface11(InterFaceCase):

    @classmethod
    def setUpClass(cls):

        interface_init.initial.result=[]
        cls.interfaceId='interface11'

    def setUp(self):
        #接口ID，标识唯一接口信息
        self.interfaceId='interface11'
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
            self.assertEqual(str(response.json().get('code')),assert_code)
            interface_init.initial.result.append((case_index,'success','OK'))
        #将错误异常捕获并抛出
        except AssertionError as e:
            interface_init.initial.result.append((case_index,'Fail',str(e)))
            raise e


    @data(get_excel_info()[1],get_excel_info()[2],get_excel_info()[3],get_excel_info()[4],
          get_excel_info()[5],get_excel_info()[6],get_excel_info()[7],get_excel_info()[8],
          get_excel_info()[9],get_excel_info()[10],get_excel_info()[11],get_excel_info()[12],
          get_excel_info()[13],get_excel_info()[14],get_excel_info()[15],get_excel_info()[16],
          get_excel_info()[17],get_excel_info()[18],get_excel_info()[19],get_excel_info()[20],
          get_excel_info()[21],get_excel_info()[22],get_excel_info()[23],get_excel_info()[24],
          get_excel_info()[25],get_excel_info()[26],get_excel_info()[27],get_excel_info()[28],
          get_excel_info()[29],get_excel_info()[30],get_excel_info()[31],get_excel_info()[32],
          get_excel_info()[33],get_excel_info()[34],get_excel_info()[35],get_excel_info()[36],
          get_excel_info()[37],get_excel_info()[38],get_excel_info()[39],get_excel_info()[40],
          get_excel_info()[41],get_excel_info()[42],get_excel_info()[43],get_excel_info()[44],
          get_excel_info()[45],get_excel_info()[46],get_excel_info()[47],get_excel_info()[48],
          get_excel_info()[49], get_excel_info()[50], get_excel_info()[51], get_excel_info()[52],
          get_excel_info()[53], get_excel_info()[54], get_excel_info()[55], get_excel_info()[56],
          get_excel_info()[57], get_excel_info()[58], get_excel_info()[59], get_excel_info()[60],
          get_excel_info()[61], get_excel_info()[62], get_excel_info()[63], get_excel_info()[64],
          get_excel_info()[65], get_excel_info()[66], get_excel_info()[67], get_excel_info()[68],
          get_excel_info()[69], get_excel_info()[70], get_excel_info()[71], get_excel_info()[72],
          get_excel_info()[73], get_excel_info()[74], get_excel_info()[75], get_excel_info()[76],
          get_excel_info()[77], get_excel_info()[78],get_excel_info()[79], get_excel_info()[80],
          get_excel_info()[81], get_excel_info()[82], get_excel_info()[83], get_excel_info()[84],
          get_excel_info()[85], get_excel_info()[86], get_excel_info()[87], get_excel_info()[88],
          get_excel_info()[89], get_excel_info()[90], get_excel_info()[91], get_excel_info()[92],
          get_excel_info()[93], get_excel_info()[94], get_excel_info()[95], get_excel_info()[96],
          get_excel_info()[97], get_excel_info()[98], get_excel_info()[99], get_excel_info()[100],
          get_excel_info()[101], get_excel_info()[102], get_excel_info()[103])
    def test_interface11(self,excel_info):
        if excel_info =='placeholder':
            self.logger.info("CaseTest.test_interface08|data drivern:skip this placeholder case!")
            return True
        case_index=excel_info['case_index']

        #接口用例为N则不执行直接成功
        if excel_info['exec'] in ['N','n']:
            self.logger.info('CaseTest.test_interface11|data drivern:skip this use case!')
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
        self.logger.info('Run case:CaseTest.test_interface11|data drivern')
        try:
            self.assertEqual(str(response.json().get('code')),assert_code)
            interface_init.initial.result.append((case_index,'success','OK'))
        #将错误异常捕获并抛出
        except AssertionError as e:
            interface_init.initial.result.append((case_index,'Fail',str(e)))
            self.logger.info("Run case:CaseTest.test_interface11|data drivern error: %s" %str(e))
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