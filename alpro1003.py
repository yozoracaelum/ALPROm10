file_puisi=open('python.txt','r')
puisi=file_puisi.readlines()
for teks in puisi:
    print(teks)
file_puisi.close()