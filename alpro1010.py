import csv
with open('kontak.csv',mode='a') as csv_file:
    input_data=csv.writer(csv_file,delimiter=',',quotechar='|')
    input_data.writerow(['5','Dian','021100022129'])
    input_data.writerow(['6','Meli','021444443234'])
print("Input data ke file selesai...")