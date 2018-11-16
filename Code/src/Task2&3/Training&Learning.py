import Feature_Extraction as code
import numpy as np
import xlrd
from sklearn import svm
X = np.empty([code.Total_data, 135], dtype=float)
data = np.empty([1,135], dtype='object')

book = xlrd.open_workbook('arrays.xlsx')
sheet = book.sheet_by_name('Sheet1')
for c in range(sheet.ncols):
    for r in range(sheet.nrows):
        X[c,r] = sheet.cell_value(r, c)

y = np.empty(code.Total_data, dtype='object')
classes = ["UP", "DOWN"]

for i in range(0,151):
	y[i] = classes[0]

for i in range(151,code.Total_data):
	y[i] = classes[1]

clf = svm.SVC(C=1, kernel = 'linear')
clf.fit(X, y)

data = code.Gesture()

Result = clf.predict(data)

print(Result)


