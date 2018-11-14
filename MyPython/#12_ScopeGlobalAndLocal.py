# scope variable : local
namaAyam = 'betet' #iterasi 1
def gantiNamaAyam(gantiNama): #Fungsi ganti nama    
    namaAyam = gantiNama #copy argumen 
    print('nama baru ayam :',namaAyam)
gantiNamaAyam('bangkok')
print('nama ayam adalah :',namaAyam)

print(100*'#')

# scope variable : global
namaAyam1 = 'betet' #iterasi 1
makananAyam1 = 'nasi'
def gantiNamaAyam1(gantiNama,makanan): #Fungsi ganti nama
    global namaAyam1,makananAyam1 #definisikan scope variable global
    makananAyam1 = makanan
    namaAyam1 = gantiNama #mengganti isi argumen
    print('nama baru ayam :',namaAyam1)
    print('Makanan baru ayam :',makananAyam1)

gantiNamaAyam1('bangkok','butiran')
print('nama ayam adalah :',namaAyam1, 'makanannya : ',makananAyam1)
print(100*'#')

