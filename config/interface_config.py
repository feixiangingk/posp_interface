#coding:utf-8
__author__ = 'FanGu'

class InterfaceConfig():

    ip='http://172.16.5.128:8081'

    project_path='D:\\quarkscript\\posp_interface'

    common_headers={"Content-Type":"application/json; charset=UTF-8"}

    testcase={'load_all':'n',
              'case_discover':['#sdf'],
              'case_module':['case_interface11']}

    interface_map = {"interface01": "",

                     "interface06": 'successful_notice_of_single_recharge',
                     "interface06Index": ["tradeNo", "tradeStatus", "finishDateTime", "errorNo", "errorInfo",
                                          "tradeAmount", "currentSucceedAmount", "succeedAmount", "thirdFinishDateTime",
                                          "payChannel", "remark", "code", "msg",'exec'],

                     "interface07":"single_cash_payment",
                     "interface07Index":['interfaceId','merchantCode','buCode','applicationCode','interfaceSync','tradeNo',
                                         'productCode','tradeDate','tradeTime','accountNo','operAccount','operAccountType',
                                         'withdrawType','accountType','name','certType','certNo','bankCardNo','bankCardType',
                                         'reservedPhone','bankCode','bankName','amount','clientProperty','isAdvance','cityCode',
                                         'feeAmount','openBranch','payChannel','currency','token','validDay','notifyUrl','remark',
                                         're-code','re-tradeNo','re-tradeStatus','re-finishDateTime','re-msg','re-errorNo','re-errorInfo',
                                         're-data(json)','re-thirdFinishDateTime','re-payChannel','re-remark','exec'],

                     "interface08": 'successful_notice_of_single_withdraw_cash',
                     "interface08Index": ["tradeNo", "tradeStatus", "finishDateTime", "errorNo", "errorInfo",
                                           "thirdFinishDateTime","payChannel", "remark", "code", "msg", 'exec'],

                     "interface09":'batch_of_investors_recharge_offline',
                     "interface09Index":['interfaceId','merchantCode','buCode','applicationCode','interfaceSync','batchNo',
                                         'tradeDate','tradeTime','totalNum','totalAmount','dataList(json)','tradeNo','accountNo',
                                         'operAccount','operAccountType','chargeType','name','certType','certNo','transTradeNo',
                                         'amount','validDay','notifyUrl','currency','remark','re-code','re-batchNo','re-batchStatus',
                                         're-msg','re-remark','exec'],

                     "interface10": 'notice_of_batch_of_investors_recharge_offline',
                     "interface10Index": ["batchNo","tradeNo", "tradeStatus", "finishDateTime", "errorNo", "errorInfo",
                                          "thirdFinishDateTime", "remark", "code", "msg", 'exec'],

                     "interface11":'customer_status_info_query',
                     "interface11Index": ['interfaceId','merchantCode','buCode','applicationCode','interfaceSync','tradeNo',
                                         'tradeDate','tradeTime','accountNo','certType','certNo','accountType','remark',
                                         're-code','re-tradeNo','re-tradeStatus','re-data','re-msg','accountFlag','re-accountNo',
                                         're-certNo','bankFlag','pwdFlag','re-errorNo','re-errorInfo','exec']
                     }

    bind_card_interface={
        'url':'',
        'interfaceType':'POST',
        "interfaceNo":"",
        'headers':{},
        'parmas':{},
        'response':{}
    }

    #单笔代扣充值通知接口信息
    successful_notice_of_single_recharge={
        'url':'/api/deposnotify/rechargenotify',
        'interfaceType': 'POST',
        "interfaceNo": "interface06",
        'headers':common_headers,
        'parmas':{
            #接口参数列表，第一项为类型、第二项为参数最大长度，第三项为是否必填，第四项为可选列表
            'tradeNo':['string',50,'Y',[]],
            'tradeStatus':['string',2,'Y',['30','40']],
            'errorNo': ['string', 5, 'N', []],
            'errorInfo': ['string', 500, 'N', []],
            'tradeAmount': ['string', 20, 'N', []],
            'currentSucceedAmount': ['string', 20, 'N', []],
            'succeedAmount': ['string', 20, 'N', []],
            'finishDateTime': ['string', 19, 'Y', []],
            'thirdFinishDateTime': ['string', 19, 'N', []],
            'payChannel': ['string', 2, 'N', ['00','01','02','03','04','05','06']],
            'remark': ['string', 600, 'N', []]
        },
        #响应参数详细信息
        'response': {
            'code': ['string', 3, 'Y', ['200','400','402','601']],
            'msg': ['string', 500, 'N', []]
        }
    }

    #单笔代付提现接口信息
    single_cash_payment={
        'url':'',
        'interfaceType':'POST',
        'interfaceNo':'interface07',
        'headers':common_headers,
        'parmas': {
            # 接口参数列表，第一项为类型、第二项为参数最大长度，第三项为是否必填，第四项为可选列表
            'interfaceId': ['string', 100, 'Y', []],
            'merchantCode': ['string', 32, 'Y', ['01', '02']],
            'buCode': ['string', 4, 'Y', ['1000', '1001', '1002', '1003']],
            'applicationCode': ['string', 4, 'Y', ['1000', '1001', '1002', '1003', '1004', '1005', '1006']],
            'interfaceSync': ['string', 1, 'Y', ['0', '1', '2']],
            'tradeNo': ['string', 50, 'Y', []],
            'productCode': ['string', 10, 'Y', []],
            'tradeDate': ['string', 10, 'Y', ['yyyy-MM-dd']],
            'tradeTime': ['string', 8, 'Y', ['hh:mm:ss']],
            'accountNo': ['string', 32, 'Y', []],
            'operAccount': ['string', 1000, 'Y', []],
            'operAccountType': ['string', 50, 'Y', []],
            'withdrawType': ['string', 1, 'Y', ['1', '2']],
            'accountType': ['string', 2, 'Y', ['1', '2']],
            'name': ['string', 50, 'Y', []],
            'certType': ['string', 3, 'Y',
                         ['101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '201', '202', '999']],
            'certNo': ['string', 50, 'Y', []],
            'bankCardNo': ['string', 32, 'Y', []],
            'bankCardType': ['string', 1, 'Y', ['1', '2']],
            'reservedPhone': ['string', 20, 'Y', []],
            'bankCode': ['string', 10, 'Y', []],
            'bankName': ['string', 100, 'Y', []],
            'openBranch': ['string', 255, 'N', []],
            'payChannel': ['string', 100, 'N', []],
            'currency': ['string', 4, 'N', ['CNY']],
            'amount': ['string', 20, 'Y', []],
            'feeAmount': ['string', 20, 'N', []],
            'clientProperty': ['string', 1, 'Y', ['0', '1']],
            'isAdvance': ['string', 1, 'Y', ['1', '2']],
            'cityCode': ['string', 10, 'Y', []],
            'token': ['string', 100, 'N', []],
            'validDay': ['string', 3, 'N', []],
            'notifyUrl': ['string', 100, 'N', []],
            'remark': ['string', 600, 'N', []]
        },
        # 响应参数详细信息
        'response': {
            'code': ['string', 4, 'Y', ['200', '400', '402', '601']],
            'msg': ['string', 500, 'N', []],
            'data': ['json', 500, 'N', []],
            'tradeNo': ['string', 50, 'Y', []],
            'tradeStatus': ['string', 2, 'Y', ['10', '20', '30', '40']],
            'errorNo': ['string', 5, 'N', []],
            'errorInfo': ['string', 500, 'N', []],
            'finishDateTime': ['string', 19, 'Y', []],
            'thirdFinishDateTime': ['string', 19, 'N', []],
            'payChannel': ['string', 2, 'N', ['00', '01', '02', '03', '04', '05', '06']],
            'remark': ['string', 600, 'N', []]
        }
    }


    #单笔代付提现通知接口信息
    successful_notice_of_single_withdraw_cash={
        'url': '/api/deposnotify/withdrawnotify',
        'interfaceType': 'POST',
        "interfaceNo": "interface08",
        'headers': common_headers,
        'parmas': {
            # 接口参数列表，第一项为类型、第二项为参数最大长度，第三项为是否必填，第四项为可选列表
            'tradeNo': ['string', 50, 'Y', []],
            'tradeStatus': ['string', 2, 'Y', ['10', '20', '30', '40']],
            'errorNo': ['string', 5, 'N', []],
            'errorInfo': ['string', 500, 'N', []],
            'finishDateTime': ['string', 19, 'Y', []],
            'thirdFinishDateTime': ['string', 19, 'N', []],
            'payChannel': ['string', 2, 'N', ['00', '01', '02', '03', '04', '05', '06']],
            'remark': ['string', 600, 'N', []]
        },
        # 响应参数详细信息
        'response': {
            'code': ['string', 3, 'Y', ['200', '400', '402', '601']],
            'msg': ['string', 500, 'N', []]
        }
    }

    # 投资人批量线下认领充值接口信息
    batch_of_investors_recharge_offline={
        'url':'',
        'interfaceType':'POST',
        'interfaceNo':'interface09',
        'headers': common_headers,
        'parmas': {
            # 接口参数列表，第一项为类型、第二项为参数最大长度，第三项为是否必填，第四项为可选列表
            'interfaceId': ['string', 100, 'Y', []],
            'merchantCode': ['string', 32, 'Y', ['01','02']],
            'buCode': ['string', 4, 'Y', ['1000', '1001', '1002','1003']],
            'applicationCode': ['string', 4, 'Y', ['1000', '1001', '1002', '1003', '1004', '1005', '1006']],
            'interfaceSync': ['string', 1, 'Y', ['0', '1', '2']],
            'batchNo':['string',50,'Y',[]],
            'tradeDate': ['string', 10, 'Y', ['yyyy-MM-dd']],
            'tradeTime': ['string', 8, 'Y', ['hh:mm:ss']],
            'validDay':['string',3,'N',[]],
            'notifyUrl':['string',500,'N',[]],
            'totalNum':['string',5,'Y',[]],
            'totalAmount':['string',20,'Y',[]],
            'dataList':['json',10000,'Y',[]],
            'tradeNo':['string',50,'Y',[]],
            'accountNo':['string',32,'Y',[]],
            'operAccount':['string',1000,'Y',[]],
            'operAccountType':['string',50,'Y',[]],
            'chargeType':['string',1,'Y',['1','2']],
            'name':['string',50,'Y',[]],
            'certType':['string',3,'Y',
                        ['101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '201', '202', '999']],
            'certNo':['string',50,'Y',[]],
            'transTradeNo':['string',50,'Y',[]],
            'currency':['string',4,'N',['CNY']],
            'amount':['string',20,'Y',[]],
            'remark': ['string', 600, 'N', []]
        },
        # 响应参数详细信息
        'response': {
            'code': ['string', 3, 'Y', ['200', '400', '402', '601']],
            'msg': ['string', 500, 'N', []],
            'data': ['json', 500, 'N', []],
            'batchNo':['string',500,'Y',[]],
            'batchStatus':['string',2,'Y',['10','20']],
            'remark':['string',600,'N',[]]
        }

    }



    #投资人批量线下认领充值通知接口信息
    notice_of_batch_of_investors_recharge_offline={
        'url': '/api/deposnotify/investclaimbatchrechargenotify',
        'interfaceType': 'POST',
        "interfaceNo": "interface10",
        'headers': common_headers,
        'parmas': {
            # 接口参数列表，第一项为类型、第二项为参数最大长度，第三项为是否必填，第四项为可选列表
            'batchNo':['string',50,'Y',[]],
            'tradeNo': ['string', 50, 'Y', []],
            'tradeStatus': ['string', 2, 'Y', ['20', '30', '40']],
            'errorNo': ['string', 5, 'N', []],
            'errorInfo': ['string', 500, 'N', []],
            'finishDateTime': ['string', 19, 'Y', []],
            'thirdFinishDateTime': ['string', 19, 'N', []],
            'remark': ['string', 600, 'N', []]
        },
        # 响应参数详细信息
        'response': {
            'code': ['string', 3, 'Y', ['200', '400', '402', '601']],
            'msg': ['string', 500, 'N', []]
        }
    }

    #客户状态信息查询接口信息
    customer_status_info_query={
        'url':'',
        'interfaceType': 'POST',
        'interfaceNo': 'interface11',
        'headers': common_headers,
        'parmas': {
            # 接口参数列表，第一项为类型、第二项为参数最大长度，第三项为是否必填，第四项为可选列表
            'interfaceId': ['string', 100, 'Y', []],
            'merchantCode': ['string', 32, 'Y', ['01', '02']],
            'buCode': ['string', 4, 'Y', ['1000', '1001', '1002', '1003']],
            'applicationCode': ['string', 4, 'Y', ['1000', '1001', '1002', '1003', '1004', '1005', '1006']],
            'interfaceSync': ['string', 1, 'Y', ['0', '1', '2']],
            'tradeNo': ['string', 50, 'Y', []],
            'tradeDate': ['string', 10, 'Y', ['yyyy-MM-dd']],
            'accountNo': ['string', 32, 'Y', []],
            'certType': ['string', 3, 'Y',
                         ['101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '201', '202', '999']],
            'certNo': ['string', 50, 'Y', []],
            'accountType': ['string', 1, 'Y', ['1', '2']],
            'remark': ['string', 600, 'N', []]
        },
        # 响应参数详细信息
        'response': {
            'code': ['string', 3, 'Y', ['200', '400', '402', '601']],
            'msg': ['string', 500, 'N', []],
            'data': ['json', 500, 'N', []],
            'tradeNo': ['string', 50, 'Y', []],
            'tradeStatus': ['string', 2, 'Y', ['30', '40']],
            'accountFlag':['string',1,'N',['0','1']],
            'accountNo': ['string', 32, 'N', []],
            'certNo': ['string', 20, 'N', []],

            'bankFlag': ['string', 1, 'N', ['0','1']],
            'pwdFlag': ['string', 1, 'N', ['0', '1']],
            'errorNo': ['string', 5, 'N', []],
            'errorInfo': ['string', 500, 'N', []]
        }
    }


    def __init__(self):
        self.__doc__="record interface information"

