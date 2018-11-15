import xlrd

from app.testcase.models import TestCaseModule

data = xlrd.open_workbook('static/test_case_demo.xls')
# data = xlrd.open_workbook('test_case_demo.xls')

# sheet_names = data.sheet_names()[0]
# print(sheet_names)
for s in range(1, len(data.sheets())):
    table = data.sheets()[s]  # 打开第一张表
    nrows = table.nrows  # 获取表的行数
    for i in range(2, nrows):  # 循环逐行打印
        j = 1
        item = table.row_values(i)
        testcase = TestCaseModule(doucument_id=1, func_id=j, name=item[2], method=item[3], expection=item[4],
                                  remarks=item[8])
        testcase.save()
        j = j + 1
