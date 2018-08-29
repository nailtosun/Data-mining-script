from builtins import int
import time
import xlrd
import xlwt
import pandas as pd

class Kcedas(object):
    def __init__(self, adres, aktiftuk , ortalama, ay, kesim):
        self.adres = adres
        self.aktiftuk = aktiftuk
        self.ortalama = ortalama
        self.ay = ay
        self.kesim = kesim

path = r'C:\Users\nailt\Desktop\data-mining-git\KCEDAS.xlsx'
file_read = open (path, 'r')
excel_data = file_read.readlines
wb = xlrd.open_workbook(path)
sheet_names = wb.sheet_names()
for sheet in wb.sheets():
    nrows = sheet.nrows
    ncols = sheet.ncols
    dataframe = []
    for row in range (nrows):
        row_carrier = []
        for col in range (ncols):
            value_cell = sheet.cell(row, col).value
            try:
                value_cell = value_cell
            except ValueError:
                pass
            finally:
                row_carrier.append(value_cell)
        df_row = Kcedas(*row_carrier)
        dataframe.append(df_row)
KCEDAS_firstcol = []
for df_row in dataframe:
    KCEDAS_firstcol.append(df_row.adres)
KCEDAS_ADRES = []
for i in range(len(KCEDAS_firstcol)):
    if KCEDAS_firstcol[i] != KCEDAS_firstcol[i+1]:
        KCEDAS_ADRES.append(KCEDAS_firstcol[i])

df = pd.DataFrame(KCEDAS_ADRES)
df.to_csv('adres.csv',index = False)
df
