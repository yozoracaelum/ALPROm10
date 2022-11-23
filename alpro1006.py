'''
perlu library csv untuk mengoperasikan file
ekstensi .csv (comma separated values)
delimiter yaitu pemisah setiap elemen
quotechar yaitu pengapit setiap elemen
reader() untuk membaca file .csv
'''
import csv
with open('address.csv') as csv_file:
    baca_csv=csv.reader(csv_file,delimiter=',',quotechar="'")
    ''' print(csv_file)
    print(id(csv_file))
    print(id(baca_csv))
    print(baca_csv)'''
    for row in baca_csv:
        print(row)