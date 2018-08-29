from builtins import int
import time
import xlrd
import xlwt
import pandas as pd

AY = ['OCAK', 'ŞUBAT', 'MART', 'NİSAN', 'MAYIS', 'HAZİRAN', 'TEMMUZ', 'AĞUSTOS', 'EYLÜL', 'EKİM', 'KASIM', 'ARALIK']

class Kcedas(object):
    def __init__(self, adres, abone_no, abone_tip, aktiftuk, ortalama, kesim):
        self.adres = adres
        self.abone_no = abone_no
        self.abone_tip = abone_tip
        self.aktiftuk = aktiftuk
        self.ortalama = ortalama
        self.kesim = kesim

path = r'C:\Users\nailt\Downloads\kilicaslan2_rev.xlsx'
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

KCETAS_ABONE_TIPI = []
for df_row in dataframe:
    if df_row.abone_tip != '':
        KCETAS_ABONE_TIPI.append(df_row.abone_tip)
df = pd.DataFrame(KCETAS_ABONE_TIPI)
df.to_csv('kilicaslan2_rev_tipi.csv',index=False)

KCETAS_AKTIFTUK = []
for df_row in dataframe:
    if df_row.aktiftuk != '':
        KCETAS_AKTIFTUK.append(df_row.aktiftuk)
df = pd.DataFrame(KCETAS_AKTIFTUK)
df
df.to_csv('kilicaslan2_rev_aktiftuk.csv',index=False)

KCETAS_ORTALAMA = []
for df_row in dataframe:
    if df_row.ortalama != '':
        KCETAS_ORTALAMA.append(df_row.ortalama)
df = pd.DataFrame(KCETAS_ORTALAMA)
df.to_csv('kilicaslan2_rev_ortalama.csv',index=False)

KCETAS_KESIM = []
for df_row in dataframe:
    if df_row.kesim != '':
        KCETAS_KESIM.append(df_row.kesim)
df = pd.DataFrame(KCETAS_KESIM)
df.to_csv('kilicaslan2_rev_kesim.csv',index=False)

KCETAS_first_col = []
for df_row in dataframe:
    KCETAS_first_col.append(df_row.adres)
KCETAS_ADRES_List = []
KCETAS_MAHALLE_Isim = []
KCETAS_SOKAK_Isim = []
KCETAS_BINA_NO = []
KCETAS_DAIRE_NO = []
KCETAS_ay = []
for patates in KCETAS_first_col:
    try:
        if 'SEMT: ' in patates:
            KCETAS_MAHALLE_Isim.append(patates)
        elif 'CADDESOKAK: ' in patates:
            KCETAS_SOKAK_Isim.append(patates)
        elif 'BINA: ' in patates:
            KCETAS_BINA_NO.append(patates)
        elif 'DAIRENO: ' in patates:
            KCETAS_DAIRE_NO.append(patates)
        elif patates in AY:
            KCETAS_ay.append(patates)
            KCETAS_ADRES_List.append([KCETAS_ay[-1],KCETAS_MAHALLE_Isim[-1], KCETAS_SOKAK_Isim[-1], KCETAS_BINA_NO[-1], KCETAS_DAIRE_NO[-1]])

    except:
        print('KCETAS adres bilgilerini kontrol et!')

concatADRES = ['ADRES']
for i in range(len(KCETAS_ADRES_List)):
    concatADRES.append(KCETAS_ADRES_List[i][1]+KCETAS_ADRES_List[i][2]+KCETAS_ADRES_List[i][3]+KCETAS_ADRES_List[i][4])
df = pd.DataFrame(concatADRES)
df.to_csv('kilicaslan2_rev_adres.csv',index = False)
df
