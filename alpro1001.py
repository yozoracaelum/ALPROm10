'''
Python sudah memiliki fungsi bulit-in dalam operasi
file
open() digunakan untuk membuka suatu file
mode = 'r' -> mode read, membaca
readlines() akan meletakkan bacaan file ke dalam
list
'''
file_puisi=open("python.txt","r")
print(file_puisi.readlines())
file_puisi.close()