import csv
kontak = []
with open('kontak.csv') as csv_file:
    baca_data = csv.reader(csv_file, delimiter=",")
    for row in baca_data:
        kontak.append(row)
'''
pop(a) digunakan untuk mengambil sebuah elemen indeks a dari suatu list
'''
labels = kontak.pop(2)
print(f'{labels[0]} \t {labels[1]} \t\t {labels[2]}')
print("----------------------------------")
for data in kontak:
    print(f'{data[0]} \t {data[1]} \t\t {data[2]}')