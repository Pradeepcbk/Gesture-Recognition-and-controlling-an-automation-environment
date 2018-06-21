import csv
from openpyxl import Workbook

def file_len(fname):
    with open(fname) as f:
	for i, l in enumerate(f):
	    pass
    return i + 1

def convert_csv_to_xlsx(file_loc, i):
    wb = Workbook()
    sheet = wb.active
    CSV_SEPARATOR = ";"
    row_count = file_len(file_loc)
    with open(file_loc, 'r') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                for idx, val in enumerate(col.split(CSV_SEPARATOR)):
			    if(r<(row_count-140)):
				    cell = sheet.cell(row=r+1, column=idx+1)
				    cell.value = val
    wb.save("ACC_" + str(i) + ".xlsx")
    return '/home/pradeep/Documents/Project_Smart_Lab/Gesture-Recognition-and-controlling-an-automation-environment-master/Code/src/Task2/ACC_' + str(i) + '.xlsx'

