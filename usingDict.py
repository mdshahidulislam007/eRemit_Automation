
import xlrd
file_location = "C:/Users/palas/PycharmProjects/Python_learning/UEC 14.09.15 (11).xls"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
print(sheet.nrows)
print(sheet.ncols)
"""dict = {
    "Sl_No":'',
    "TT_No":'',
    "Date":'',
    "Amount":'',
    "Beneficiary":'',
    "AC_No":'',
    "Bank":'',
    "Branch":'',
    "Payment":'',
    "Remitter":'',
    "City_remitter":'',
    "Amount_words":'',
    "Cont_Benef":''

}"""
#l = list(dict.keys())

for row in range(1,sheet.nrows):
    for col in range(sheet.ncols):
       # dict ={ l[col] : sheet.cell_value(row,col)}
        dict = {sheet.cell_value(0,col) : sheet.cell_value(row,col)}

        print(dict)
    print("#######################")