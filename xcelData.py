import xlrd
file_location = "C:/Users/palas/PycharmProjects/Python_learning/UEC 14.09.15 (11).xls"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
print(sheet.nrows)
print(sheet.ncols)
data = []
print(type(data))
for row in range(sheet.nrows):

    for col in range(sheet.ncols):
        data = sheet.cell_value(row,col)

        print(data)

    print(".................................................................")
print(type(data))