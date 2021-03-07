import pandas as pd
import numpy as np
import xlrd
import matplotlib.pyplot as plt

excel_file_1 = 'a.xlsx'

df_first_shift = pd.read_excel(excel_file_1, sheet_name='first', engine = 'openpyxl')
df_second_shift = pd.read_excel(excel_file_1, sheet_name='second', engine = 'openpyxl')

print(df_first_shift)

