#coding:utf-8
__author__ = 'FanGu'
import sys,json
sys.path.append('..')


class GetRequestInfo():

    def __init__(self,initial):
        self.initial=initial
        self.interfaceConfig=self.initial.interfaceConfig

    def get_post_info(self,interfaceId,excel_info):
        interfaceName = self.interfaceConfig.interface_map[interfaceId]
        interface_info = getattr(self.interfaceConfig, interfaceName)
        url = self.interfaceConfig.ip + interface_info['url']

        headers = interface_info['headers']
        parmas = interface_info['parmas']
        for i in excel_info.keys():
            if i not in parmas.keys():
                del excel_info[i]
        datas = json.dumps(excel_info)
        return url,headers,datas
