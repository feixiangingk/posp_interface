#coding:utf-8
import xlrd,sys
sys.path.append('..')
reload(sys)
sys.setdefaultencoding('utf-8')
from common.interface_init import *
from openpyxl import  load_workbook
from datetime import datetime

class ExecExcel():

    def __init__(self):
        self.initial=interface_init.initial
        self.file_path=self.initial.project_path+"\\testData\\interface_Data.xlsx"

        self.interface_map = self.initial.interfaceConfig.interface_map


    def get_info(self,sheetName):
        #formatting_info=True打开时保留格式
        EL_data=xlrd.open_workbook(self.file_path)
        table=EL_data.sheet_by_name(sheetName)

        #读取接口信息字典
        interfaceInfo=getattr(self.initial.interfaceConfig,self.interface_map[sheetName])
        interfaceIndex=self.interface_map[sheetName+"Index"]


        #确定表格一共多少行数据
        excel_info={}
        for i in xrange(table.nrows):
            #从第四行开始读取excel，前面标题忽略
            if i <=3:
                continue
            rows_info=table.row_values(i)

            excel_info[int(rows_info[0])]={}

            for n in xrange(len(interfaceIndex)):
                if interfaceIndex[n] in ['tradeAmount', 'currentSucceedAmount', 'succeedAmount','amount','totalAmount','notifyUrl']:
                    excel_info[rows_info[0]][interfaceIndex[n]] = str(rows_info[n + 1])

                else:
                    excel_info[rows_info[0]][interfaceIndex[n]]=str(rows_info[n+1]).split('.')[0]

        return excel_info

    #数据驱动读取格式
    def get_info_ddt(self, sheetName):
        # formatting_info=True打开时保留格式
        EL_data = xlrd.open_workbook(self.file_path)
        table = EL_data.sheet_by_name(sheetName)

        # 读取接口信息字典
        interfaceInfo = getattr(self.initial.interfaceConfig, self.interface_map[sheetName])
        interfaceIndex = self.interface_map[sheetName + "Index"]

        # 确定表格一共多少行数据
        excel_info = ['placeholder']

        #用字典映射方法完成 switch case语句
        format_data={"int":lambda x:int(x),
                     "float":lambda x:float(x),
                     "True":lambda x:bool(1),
                     "False":lambda x:bool(0),
                     "list":lambda x:[x],
                     #将字符串转换为json格式
                     "json":lambda x:eval(str(x).replace("\n","").replace("\t",""))}



        for i in xrange(table.nrows):
            # 从第四行开始读取excel，前面标题忽略
            if i <= 3:
                continue
            rows_info = table.row_values(i)


            dict_info={'case_index':i-3}
            for n in xrange(len(interfaceIndex)):
                if interfaceIndex[n] in ['tradeAmount', 'currentSucceedAmount', 'succeedAmount','amount','totalAmount','notifyUrl']:
                    dict_info[interfaceIndex[n]] = str(rows_info[n + 1])
                else:
                    dict_info[interfaceIndex[n]] = str(rows_info[n + 1]).split('.')[0]

                if dict_info[interfaceIndex[n]].find('@')!=-1:

                    #用dict.get()方法防止keyerror;用strip()去掉空格
                    try:
                        dict_info[interfaceIndex[n]]=format_data.get(dict_info[interfaceIndex[n]].split('@')[1].strip())(dict_info[interfaceIndex[n]].split('@')[0])

                    #捕获多个异常的写法
                    except (TypeError,ValueError),e:
                        print "i is {one};n is {two}".format(one=(i-3),two=n+2)
                        interface_init.initial.logger.info("i is {one};n is {two}".format(one=(i-3),two=n+2))
                        raise e

            excel_info.append(dict_info)

        return excel_info

    def write_info(self,sheetName,result_list):
        EL_data = load_workbook(self.file_path)

        sheet_data = EL_data.get_sheet_by_name(sheetName)
        for case_index,flag,result in result_list:
            row_info=case_index+4
            interfaceIndex = self.interface_map[sheetName + "Index"]

            #写入执行结果
            sheet_data.cell(coordinate=None,row=row_info,column=len(interfaceIndex)+2,value=flag)
            #写详情
            sheet_data.cell(coordinate=None,row=row_info,column=len(interfaceIndex)+3,value=result)

        EL_data.save(self.file_path)






if __name__=="__main__":
    Init()
    execExcel=ExecExcel()
    list_excel_info=execExcel.get_info_ddt('interface11')
    print list_excel_info[1]
    # execExcel.write_info('interface06',[(1,'success','OK')])