import csv
import os
from os.path import split

import pytest
import xlrd
import openpyxl
from allure_commons import fixture

from data.file_data.data_py import ERROR_INFO


class GetData:
    def __init__(self, filename):
        self.datalist = []
        self.filename = filename

    # 通过py文件获取数据
    def getData_By_Py(self):
        # 第一种
        # self.datalist.append(TITLE)
        # self.datalist.append(LOGIN_RIGHT_INFO)
        # self.datalist.append(LOGIN_ERROR_INFO)
        # self.datalist.append(LOGIN_ERROR_INFO1)
        # self.datalist.append(LOGIN_ERROR_INFO2)
        # self.datalist.append(LOGIN_ERROR_INFO3)
        # 第二种
        # self.datalist = RIGHT_INFO
        self.datalist = ERROR_INFO
        return self.datalist

    # 通过txt文件获取数据
    def getData_By_Txt(self):
        with open(r'{}'.format(self.filename), mode='r',
                  encoding='utf-8') as f:
            result = f.readlines()
            result = [line.strip().split('\t') for line in result]
            self.datalist = result
        f.close()
        return self.datalist

    # 通过csv文件获取数据
    def getData_By_Csv(self):
        with open(r'{}'.format(self.filename), mode='r',
                  encoding='utf-8') as f:
            result = f.readlines()
            result = [line.strip().split(',') for line in result]
            self.datalist = result
        f.close()
        return self.datalist

    # 通过导入csv模块解析获取数据
    def impCsv_getData_By_Csv(self):
        with open(r'{}'.format(self.filename), mode='r',
                  encoding='utf-8') as f:
            result = csv.reader(f)
            for i in result:
                self.datalist.append(i)
        f.close()
        return self.datalist

    # 通过excel文件获取
    def getData_By_Xlsx(self):
        xl = xlrd.open_workbook(r'{}'.format(self.filename))
        xllist = xl.sheets()
        row = xllist[0].nrows
        col = xllist[0].ncols
        for i in range(1, row):
            self.datalist.append(xllist[0].row_values(i))

        return self.datalist

    def excel_to_matrix(self):
        workbook = openpyxl.load_workbook(self.filename)
        sheet = workbook.active  # 获取第一个工作表
        data = []
        for row in sheet.iter_rows(values_only=True):
            data.append(list(row))
        return data

def one():
    mo=[
        "点击",
        "输入",
        "等待",
        "获取"
    ]
    none=''
    ntwo=''
    os_path_file = os.path.dirname(os.path.abspath('.')) + r"\data\file_data\\"
    Gdata = GetData(os_path_file + r"data_csv.csv")
    Dlist = Gdata.impCsv_getData_By_Csv()
    listone = []
    # pamr.split(",")
    # listone.append(pamr.split(","))
    for NexList in Dlist:
        if NexList[2] == mo[0] and NexList[1] != '' and NexList[4] != '':
            listone.append(NexList[3].split(","))
            yield listone,NexList[1],NexList[4],NexList
        elif NexList[2] == mo[1] and NexList[1] != '' and NexList[4] != '':
            listone.append(NexList[3].split(","))
            yield listone,NexList[1],NexList[4],NexList
        elif NexList[2] == mo[2] and NexList[1] != '' and NexList[4] != '':
            listone.append(NexList[3].split(","))
            yield listone, NexList[1],NexList[4],NexList
        elif NexList[2] == mo[3] and NexList[1] != '' and NexList[4] != '':
            listone.append(NexList[3].split(","))
            yield listone, NexList[1],NexList[4],NexList
        else:
            listone.append(NexList[3].split(","))
            yield listone,none,ntwo,NexList


@pytest.mark.parametrize("pamr,pamr1,pamr2,NexList",one())
def test_meth(pamr,pamr1,pamr2,NexList):
    """
    :param 元素路径
    :param1 要输入的内容
    :param2 断言
    :NexList 全部内容
    """
    print("我是原始数据："+pamr)
    listone=[]
    print("_______")
    pamr.split(",")
    listone.append(pamr.split(","))
    for i  in range(len(listone)):
        print(listone[i])

    print("_____________")
    # print(pamr[0])
    # for item in listone:
    #     print(item)



if __name__ == '__main__':
    # os_path_file = os.path.dirname(os.path.abspath('.'))+r"\data\file_data\\"
    # # print("路径:"+os_path_file)
    # Gdata = GetData(os_path_file+r"data_csv.csv")
    # # Dlist = Gdata.getData_By_Py()
    # # Dlist = Gdata.getData_By_Txt()
    # # Dlist = Gdata.getData_By_Csv()
    # # Dlist = Gdata.impCsv_getData_By_Csv()
    # # Dlist = Gdata.excel_to_matrix()
    # Dlist = Gdata.impCsv_getData_By_Csv()
    # print(len(Dlist))
    # print(Dlist)

    # two=one()
    # for d in two:
    #     print(d)
    test_meth()






