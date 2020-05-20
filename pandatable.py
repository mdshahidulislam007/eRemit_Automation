# import pandas as pd
import pandas as pd
import xlrd
file_location = "C:/Users/palas/PycharmProjects/Python_learning/UEC 14.09.15 (11).xls"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)

# list of strings
df = []

for row in range(sheet.nrows):

    for col in range(sheet.ncols):

        df = pd.DataFrame(sheet.cell_value(row,col))
        print(df)