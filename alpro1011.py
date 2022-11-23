import csv
with open('data.csv',mode='w') as csv_file:
    keterangan=['NO','NAMA','TELEPON']
    input_data=csv.DictWriter(csv_file,fieldnames=keterangan)
    input_data.writeheader()
    input_data.writerow({'NO':'1','NAMA':'Rina Diana','TELEPON':'09123409999'})
    input_data.writerow({'NO':'2','NAMA':'Rafi','TELEPON':'086748488888'})
print('Input data ke file selesai...')