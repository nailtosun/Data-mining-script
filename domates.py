from builtins import int
import time
import xlrd
import xlwt
import format
import pandas as pd

path = r'C:\Users\nailt\Desktop\data-mining-git\table.xlsx'
file_read = open(path,'r')
excel_data = file_read.readlines
wb = xlrd.open_workbook(path)
sheet_names = wb.sheet_names()

for sheet in wb.sheets():
    nrows = sheet.nrows
    ncols = sheet.ncols
    dataframe = []
    for row in range(nrows):
        row_carrier = []
        for col in range(ncols):
            value = sheet.cell(row,col).value
            try:
                value = str(int(value))
            except ValueError:
                pass
            finally:
                row_carrier.append(value)
        dataframe.append(row_carrier)

adres_list = []
for i in range(1,nrows-1):
    if dataframe[i][0] != dataframe[i+1][0]:
        adres_list.append(dataframe[i][0])
    else:
        pass
dataframe[1]
df = pd.DataFrame(adres_list)
df.to_csv('adres_list.csv',index = False)

hashed_list = []

for i in range(len(adres_list)):
    hashed_list.append(adres_list[i])

counter = 0
for i in range(len(adres_list)):
    for j in range(nrows):
        if dataframe[j][0] == adres_list[i]:
            hashed_list[i].append(dataframe[j][2] , dataframe [j][4])
            counter = counter + 1
            if counter == 12:
                break
        else:
            counter = 0
