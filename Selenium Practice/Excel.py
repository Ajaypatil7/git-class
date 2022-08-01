#  xlrd It is a library which helps us to work with excels.
from xlrd import open_workbook
# It is a function which is used to open the excel sheet and it takes path as an argument
wb= open_workbook('C:\\Users\\Admin\\Desktop\\selpractice.xls')

ws= wb.sheet_by_name('loginpage')
#It is used to open a perticular sheet from the excel file.

used_rows= ws.nrows
#it is used to get the no of rows that are used
print(used_rows)
locators={}
for i in range(0,used_rows):
    data= ws.row_values(i)    #It is used to read that row
    print(data)
    locators[data[0]]=(data[1],data[2])

print(locators)

