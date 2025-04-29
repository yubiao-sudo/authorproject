# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/15 11:38
@Auth ： PandaYu
@File ：duqu_excel.py
@IDE ：PyCharm
"""
'''读excel表数据
		open_workbook 打开文件;
		sheets 读取所有工作簿，返回列表;
		sheet_by_index  通过索引读取工作簿;
		sheet_by_name   通过名字读取工作簿;
		nrows 获取行数；
		ncols ；获取列数
		row_values(行，开始列（包含），结束的列（不包含）) 获取行值，返回列表;
		col_values(列，开始行（包含），结束的行（不包含）) 获取列值，返回列表;
		cell_value(行,列) 根据单元格获取值.
'''
# 1. 导入 xlrd
import xlrd
# 2. 打开文件
wb = xlrd.open_workbook(r'E:\汇智动力\Selenium自动化\selenium教学课程\project\SeleniumStudy\data\data_xlsx.xlsx')

# 3. 获取工作簿
table1 = wb.sheet_by_index(0) # 通过下标获取工作簿
table2 = wb.sheet_by_name('Sheet2') # 通过名字获取工作簿  # table2 = wb.sheet_by_name(u'Sheet2') # 通过名字获取工作簿
table3 = wb.sheets() # 获取所有工作簿，返回列表
# print(table1,table2,table3)
# 4. 获取 行数，列数
print(table1.nrows) # 获取行数
print(table1.ncols) # 获取列数

# 5. 获取 行值，列值
print(table1.row_values(0)) # 获取整行的值
print(table1.col_values(0)) # 获取整列的值
print(table1.col_values(1,8,10)) # 获取整列的值
print(table1.row_values(12,1,-1))

# 7.获取单元格的值 cell_value(行，列)
print(table1.cell_value(12,2))

# 获取单元格内容
cell_A1 = table1.cell(0, 0).value
cell_B1 = table1.row(0)[1].value  # 使用行索引
cell_C2 = table1.col(3)[1].value  # 使用列索引
print(cell_A1, cell_B1, cell_C2)


# 获取单元格内容的数据类型
# ctype:0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
print('cell(0,0)数据类型:', Data_sheet.cell(0, 0).ctype)
print('cell(1,0)数据类型:', Data_sheet.cell(1, 0).ctype)
print('cell(1,1)数据类型:', Data_sheet.cell(1, 1).ctype)
print('cell(1,2)数据类型:', Data_sheet.cell(1, 2).ctype)

# 获取单元格内容为日期的数据
date_value = xlrd.xldate_as_tuple(Data_sheet.cell_value(1,0),workbook.datemode)
print(type(date_value), date_value)
print('%d:%d:%d' % (date_value[0:3]))



'''创建 excel 并写入数据'''
import xlwt
def set_style(name, height, bold=False):
    style = xlwt.XFStyle()   # 初始化样式
    font = xlwt.Font()       # 为样式创建字体
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style


def write_excel(path):
    # 创建工作簿
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建sheet
    data_sheet = workbook.add_sheet('demo')
    row0 = ['字段名称', '大致时段', 'CRNTI', 'CELL-ID']
    row1 = ['测试', '15:50:33-15:52:14', 22706, 4190202]
    # 生成第一行和第二行
    for i in range(len(row0)):
        data_sheet.write(0, i, row0[i], set_style('Times New Roman', 220, True))
        data_sheet.write(1, i, row1[i], set_style('Times New Roman', 220, True))

    # 保存文件
    workbook.save(path)