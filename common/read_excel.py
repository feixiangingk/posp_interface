#coding:utf-8
import xlrd,sys
from win32com.client import Dispatch
import win32com.client
sys.path.append('..')
reload(sys)
sys.setdefaultencoding('utf-8')

from openpyxl import  load_workbook
from datetime import datetime
from interface_init import *

class ExecExcel():
    interfaceIndex=None

    def __init__(self):


        # self.initial=interface_init.initial
        self.file_path="D:\\quarkscript\\posp_interface\\testData\\interface_Data.xlsx"
        # self.file_path=self.initial.project_path+"\\testData\\interface_Data.xlsx"

        # self.interface_map = self.initial.interfaceConfig.interface_map




        #检查进程是否有excel处于激活状态，有则关闭
        excel=win32com.client.Dispatch('Excel.Application')
        excel.DisplayAlerts=False
        excel.Quit()


    def get_info(self,sheetName):
        #formatting_info=True打开时保留格式
        EL_data=xlrd.open_workbook(self.file_path)
        table=EL_data.sheet_by_name(sheetName)

        #读取接口信息字典
        # interfaceInfo=getattr(self.initial.interfaceConfig,self.interface_map[sheetName])
        # interfaceIndex=self.interface_map[sheetName+"Index"]

        # 不从配置文件读取接口参数列表，而从excel表格直接读取
        interfaceIndex1 = table.row_values(3)
        interfaceIndex1.pop(0)

        #用while循环过滤
        while "" in interfaceIndex1:
            interfaceIndex1.remove("")
        ExecExcel.interfaceIndex=[str(i) for i in interfaceIndex1]


        #确定表格一共多少行数据
        excel_info={}
        for i in xrange(table.nrows):
            #从第四行开始读取excel，前面标题忽略
            if i <=3:
                continue
            rows_info=table.row_values(i)

            excel_info[int(rows_info[0])]={}

            for n in xrange(len(ExecExcel.interfaceIndex)):
                if ExecExcel.interfaceIndex[n] in ['tradeAmount', 'currentSucceedAmount', 'succeedAmount','amount','totalAmount','notifyUrl','email']:
                    excel_info[rows_info[0]][ExecExcel.interfaceIndex[n]] = str(rows_info[n + 1])

                else:
                    excel_info[rows_info[0]][ExecExcel.interfaceIndex[n]]=str(rows_info[n+1]).split('.')[0]



        return excel_info

    #数据驱动读取格式
    def get_info_ddt(self, sheetName):
        # formatting_info=True打开时保留格式
        EL_data = xlrd.open_workbook(self.file_path)
        table = EL_data.sheet_by_name(sheetName)

        # 读取接口信息字典
        # interfaceInfo = getattr(self.initial.interfaceConfig, self.interface_map[sheetName])
        # interfaceIndex = self.interface_map[sheetName + "Index"]

        #不从配置文件读取接口参数列表，而从excel表格直接读取
        interfaceIndex1=table.row_values(3)
        interfaceIndex1.pop(0)

        #用while循环过滤
        # while "" in interfaceIndex1:
        #     interfaceIndex1.remove("")

        #用for循环过滤
        for i in xrange(interfaceIndex1.count("")):
            interfaceIndex1.remove("")

        ExecExcel.interfaceIndex=[str(i) for i in interfaceIndex1]


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

            dict_info={'case_index':int(i-3)}
            for n in xrange(len(ExecExcel.interfaceIndex)):
                if self.interfaceIndex[n] in ['tradeAmount', 'currentSucceedAmount', 'succeedAmount','amount','totalAmount','notifyUrl','email']:
                    dict_info[ExecExcel.interfaceIndex[n]] = str(rows_info[n + 1])
                else:
                    dict_info[ExecExcel.interfaceIndex[n]] = str(rows_info[n + 1]).split('.')[0]

                #第一个if判断值包含@
                if dict_info[ExecExcel.interfaceIndex[n]].find('@')!=-1:
                    #第二个if判断定义的值在我们处理范围内
                    if dict_info[ExecExcel.interfaceIndex[n]].split('@')[1].strip() in ['int','float','list','json','True','Flase']:
                    #用dict.get()方法防止keyerror;用strip()去掉空格
                        try:
                            dict_info[ExecExcel.interfaceIndex[n]]=format_data.get(dict_info[ExecExcel.interfaceIndex[n]].split('@')[1].strip())(dict_info[self.interfaceIndex[n]].split('@')[0])

                        #捕获多个异常的写法
                        except (TypeError,ValueError),e:
                            print "i is {one};n is {two}".format(one=(i-3),two=n+2)
                            # interface_init.initial.logger.info("i is {one};n is {two}".format(one=(i-3),two=n+2))
                            raise e

            excel_info.append(dict_info)

        return excel_info

    def write_info(self,sheetName,result_list):
        EL_data = load_workbook(self.file_path)

        sheet_data = EL_data.get_sheet_by_name(sheetName)

        for case_index,flag,result in result_list:
            row_info=case_index+4
            # interfaceIndex = self.interface_map[sheetName + "Index"]


            #写入执行结果
            sheet_data.cell(coordinate=None,row=row_info,column=len(ExecExcel.interfaceIndex)+2,value=flag)
            #写详情
            sheet_data.cell(coordinate=None,row=row_info,column=len(ExecExcel.interfaceIndex)+3,value=result)

        EL_data.save(self.file_path)






if __name__=="__main__":
    # if isinstance(interface_init.initial,Initialization) !=True:
    #     Init()
    execExcel=ExecExcel()
    list_excel_info=execExcel.get_info_ddt('interface03')
    print list_excel_info[1]

