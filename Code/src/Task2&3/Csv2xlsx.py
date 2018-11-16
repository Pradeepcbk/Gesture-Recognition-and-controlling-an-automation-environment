import csv
from openpyxl import Workbook

import os
import glob
import csv
from xlsxwriter.workbook import Workbook


def file_len(fname):
    with open(fname) as f:
         for i, l in enumerate(f):
             pass
    return i + 1

def convert_csv_to_xlsx(file_loc,i):
    for csvfile in glob.glob(file_loc):
        workbook = Workbook(csvfile[:-4] +'.xlsx')
        worksheet = workbook.add_worksheet()
        row_count = file_len(file_loc)
        with open(csvfile, 'rt') as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                 for c, col in enumerate(row):
                     if(r<(row_count-140)):
                         worksheet.write(r, c, col)
        workbook.close()
    return os.path.join('ACC_'+str(i)+'.xlsx')
