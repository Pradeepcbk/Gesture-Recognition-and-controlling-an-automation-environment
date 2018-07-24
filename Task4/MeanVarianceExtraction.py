import csv
import xlrd
import numpy as np
from openpyxl import Workbook
import os
import glob

def convertCsv2Xlsx(file_loc):
    wb = Workbook()
    sheet = wb.active
    CSV_SEPARATOR = " "
    with open(file_loc, 'r') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                for idx, val in enumerate(col.split(CSV_SEPARATOR)):
                    cell = sheet.cell(row=r+1, column=idx+1)
                    cell.value = val
    wb.save("position.xlsx")
    return "position.xlsx"

def getColumninExcel(columnNumber):
    excelData = []
    for value in sheet.col_values(columnNumber):
        excelData.append(value[:-2])
        newData = np.array(excelData[1:]).astype(np.float)
    return newData


file_location = "C:/Users/Happy/PycharmProjects/HMM_DataExtraction/position.csv"
excelFile = convertCsv2Xlsx(file_location)
workbook = xlrd.open_workbook(excelFile)
sheet = workbook.sheet_by_index(0)
L = sheet.nrows

X_Data = getColumninExcel(33)
Y_Data = getColumninExcel(35)
Z_Data = getColumninExcel(37)

data = np.zeros((3,2),dtype=float)

data = [[np.mean(X_Data),np.var(X_Data)],[np.mean(Y_Data),np.var(Y_Data)],[np.mean(Z_Data),np.var(Z_Data)]]

print(data)
