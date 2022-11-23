import csv
with open('data.csv',mode='a') as csv_file:
    keterangan=['NO','NAMA','TELEPON']
    input_data=csv.DictWriter(csv_file,fieldnames=keterangan)
    input_data.writerow({'NO':'3','NAMA':'Melky','TELEPON':'08123408787'})
    input_data.writerow({'NO':'4','NAMA':'Sarah','TELEPON':'08274848886'})
print('Input data ke file selesai...')