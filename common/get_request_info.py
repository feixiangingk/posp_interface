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

        #这是针对充值接口做的处理，single_recharge_interface
        if excel_info.has_key("token"):
            if excel_info["token"].find("@")==-1:
                #判断applicationCode类型是不是str防止异常
                if type(excel_info['applicationCode'])!=str:
                    excel_info['token']=self.interfaceConfig.headers_applicationCode_1003.get("Token")
                else:
                    excel_info['token']=self.token_map.get(excel_info.get("applicationCode","1003"),self.interfaceConfig.headers_applicationCode_1003).get("Token")
            elif excel_info["token"].find("@")!=-1:
                excel_info["token"]=excel_info["token"].split("@")[0]

        if excel_info.has_key("batchNo") and type(excel_info.get("batchNo",1))==str:
            if excel_info["batchNo"].find("@")==-1:
                excel_info["batchNo"]=Create_Data.get_batchNo()
            elif excel_info["batchNo"].find("@")!=-1:
                excel_info["batchNo"]=excel_info["batchNo"].split("@")[0]

        #多重过滤，把tradeNo不为字符串型的数据过滤，不做处理
        if excel_info.has_key("tradeNo") and type(excel_info.get("tradeNo",1))==str:
            if excel_info["tradeNo"].find("@")==-1:
                excel_info['tradeNo']=Create_Data.get_tradeNo(interfaceId)
                if excel_info.has_key("buCode") and excel_info.get("buCode","false")!="C11":
                    excel_info['tradeNo']=excel_info['tradeNo'].replace("C11",str(excel_info['buCode']))
                if excel_info.has_key("applicationCode") and excel_info.get("applicationCode","false")!="1003":
                    excel_info['tradeNo']=excel_info['tradeNo'].replace("1003",str(excel_info['applicationCode']))
            elif excel_info["tradeNo"].find("@")!=-1:
                excel_info["tradeNo"]=excel_info["tradeNo"].split("@")[0]

        #把入参以外的数据除去，比如断言、response字段，所以interface_config中interface字段必填
        parmas = interface_info['parmas']
        for i in excel_info.keys():
            if i not in parmas.keys():
                del excel_info[i]
        datas = json.dumps(excel_info)
        datas.strip()
        return url,headers,datas

class ResponseFormat():

    #递归算法，排除字典里的true
    @staticmethod
    def format_Re(json_info):
        new_json={}
        for key,value in json_info.iteritems():
            if type(value)==unicode and "{"in value :
                value = value.replace("false", "False").replace("true", "True")
                new_json[key]=ResponseFormat.format_Re(eval(value))
            else:
                new_json[key]=value
        return new_json




if __name__=="__main__":
    # if type("Dd")==str:
    #     print 111
    json_date='''{"code":"200","msg":"请求成功","data":"{"payChannel":"01","currentSucceedAmount":"0",
    "succeedAmount":"0","synFlag":false,"tradeNo":"10C1110030012201708110150505055019","tradeStatus":10,"finishDateTime":"2017-08-11 09:51:19"}"}'''

    json_date2='''{"code": "200", "msg": "请求成功",
     "data": "{\"payChannel\":\"01\",\"currentSucceedAmount\":\"0\",
     \"succeedAmount\":\"0\",\"synFlag\":false,
     \"tradeNo\":\"10C1110030012201708110341169991257\",\"tradeStatus\":10,
     \"finishDateTime\":\"2017-08-11 11:41:46\"}"}'''

    json_data3={u'msg': u'\u8bf7\u6c42\u6210\u529f', u'code': u'200', u'data': u'{"payChannel":"01",'
                                                                               u'"currentSucceedAmount":"0","succeedAmount":"0","synFlag":false,'
                                                                               u'"tradeNo":"10C1110030012201708110352355084171","tradeStatus":10,"finishDateTime":"2017-08-11 11:53:05"}'}

    print ResponseFormat.format_Re(json_data3)
    print ResponseFormat.format_Re(json_data3).get('data').get('tradeNo')
    # print json_data3.get("data").get('tradeNo')
    # print type(json_data3)