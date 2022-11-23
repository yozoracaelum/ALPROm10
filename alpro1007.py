import csv
kontak=[]
print(kontak)
with open('kontak.csv') as csv_file:
    baca_csv=csv.reader(csv_file,delimiter=',',quotechar="|")
    for row in baca_csv:
        kontak.append(row)
print(kontak)