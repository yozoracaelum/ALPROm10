'''
format string, digunakan untuk mengubah tipe data apapun
menjadi string
Diletakkan di dalam sebuah string
{}.format()
fungsi write() digunakan untuk menulis ke dalam file
'''
print ('Biodata')
print ('=======')
nama = input("Nama: ")
umur = input("Umur: ")
alamat = input("Alamat: ")
teks = "\nNama: {}\nUmur: {}\nAlamat: {} \n------".format(nama, umur, alamat)
file_bio = open("biodata.txt", "w")
file_bio.write(teks)
file_bio.close()