import csv
kontak=[]
'''
Tipe data dictionary
dictionary:
-immutable (tidak diubah elemennya)
- memiliki dua elemen, yaitu key dan value
dict = {KEY1: VALUE1, KEY2: VALUE2}
tampil = dict{KEY1}
print(tampil) // VALUE1
'''
with open('kontak.csv') as csv_file:
    baca_data=csv.DictReader(csv_file)
    for row in baca_data:
        kontak.append(row)
print(kontak)