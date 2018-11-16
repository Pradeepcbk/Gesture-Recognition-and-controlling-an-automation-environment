import csv

import csv
with open('first.csv', 'rb') as inp, open('first_edit.csv', 'wb') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
	writer.writerow(row)
