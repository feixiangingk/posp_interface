#coding:utf-8
__author__ = 'FanGu'
import sys,json
sys.path.append('..')
from common.random_data import Create_Data


class GetRequestInfo():



    def __init__(self,initial):
        self.initial=initial
        self.interfaceConfig=self.initial.interfaceConfig

        self.token_map = {'1000': self.interfaceConfig.headers_applicationCode_1000,
                     '1001': self.interfaceConfig.headers_applicationCode_1001,
                     '1002':self.interfaceConfig.headers_applicationCode_1002,
                     '1003':self.interfaceConfig.headers_applicationCode_1003,
                     '1004':self.interfaceConfig.headers_applicationCode_1004,
                     '1005':self.interfaceConfig.headers_applicationCode_1005,
                     '1006':self.interfaceConfig.headers_applicationCode_1006}

    def get_post_info(self,interfaceId,excel_info):
        interfaceName = self.interfaceConfig.interface_map[interfaceId]
        interface_info = getattr(self.interfaceConfig, interfaceName)
        url =interface_info['url']



        headers = interface_info['headers']
        if excel_info.has_key("applicationCode"):
            if excel_info.get("applicationCode") in ['100'+x for x in '0123456']:
                headers=self.token_map.get(excel_info.get("applicationCode"))
        if excel_info.has_key("tradeNo"):
            excel_info['tradeNo']=Create_Data.get_tradeNo()

        #把入参以外的数据除去，比如断言、response字段，所以interface_config中interface字段必填
        parmas = interface_info['parmas']
        for i in excel_info.keys():
            if i not in parmas.keys():
                del excel_info[i]
        datas = json.dumps(excel_info)
        datas.strip()
        return url,headers,datas
