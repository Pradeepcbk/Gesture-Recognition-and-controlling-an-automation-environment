import csv
import xlrd
import numpy as np
from openpyxl import Workbook
import subprocess
import os

def meanForPosition(file_loc1):
    def convertCsv2Xlsx(file_loc):
        wb = Workbook()

        sheet = wb.active
        CSV_SEPARATOR = " "
        with open(file_loc, 'r') as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    for idx, val in enumerate(col.split(CSV_SEPARATOR)):
                        cell = sheet.cell(row=r + 1, column=idx + 1)
                        cell.value = val
        wb.save("position.xlsx")
        return "position.xlsx"


    def getColumninExcel(columnNumber):
        excelData = []
        for value in sheet.col_values(columnNumber):
            excelData.append(value[:-2])
            newData = np.array(excelData[1:]).astype(np.float)
        return newData
    def getColumninExcelString(columnNumber):
        excelData = []
        for value in sheet.col_values(columnNumber):
            excelData.append(value[:-2])
            newData = np.array(excelData[1:]).astype(np.string_)
        return newData


    file_location = file_loc1
    excelFile = convertCsv2Xlsx(file_location)
    workbook = xlrd.open_workbook(excelFile)
    sheet = workbook.sheet_by_index(0)
    L = sheet.nrows

    X_Data = getColumninExcel(33)
    Y_Data = getColumninExcel(35)
    Z_Data = getColumninExcel(37)
    color_data = getColumninExcelString(41)

    X = []
    Y = []
    color_arr = ""

    for data1 in X_Data:
        if (data1 != 0):
            X.append(data1)

    for data2 in Y_Data:
        if (data2 != 0):
            Y.append(data2)

    for color in color_data:
        if (color == "true"):
            color_arr = "true"

    data = np.zeros((3, 2), dtype=float)

    meanValueX = np.mean(X)
    meanValueY = np.mean(Y)
    meanValue = [meanValueX,meanValueY,color_arr]

    print('Min =',min(Y))
    print('Max =', max(Y))
    print(meanValueY)


if __name__ == "__main__":
    meanForPosition("C:/Users/hp/Desktop/positional data/zone3.1_blue.csv")







