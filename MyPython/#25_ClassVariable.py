class mahasiswa(): #Clasc mahasiswa
    jurusan ='jaringan' #variable class    
    jumlahMahasiswa = 0 #variableclass
    def __init__(self, input_nama, input_nim):#Argumen fungsi
        self.nama = input_nama #setiap ada self berarti menunjukkan bhwa variable itu dimiliki instances
        self.nim = input_nim #Setiap variable tanpa self didalam class brarti itu adalah variable class
        
        mahasiswa.jumlahMahasiswa += 1 #Menghitung jumlah instance
    

mhs1 = mahasiswa('dagul',1410530199) #Input data instance kedalam class(wajib mengisi argumen)
mhs2 = mahasiswa('muklis',1410530198)


mhs1.jurusan = 'multimedia' #variable instance/override variable class

print(mahasiswa.jurusan) #mengambil variable jurusan 
print(mhs1.jurusan) #mengambil variable jurusan dalam class mahasiswa
print(mhs2.jurusan)

print(mhs1.__dict__) #Melihat isi dari mhs1

print('jumlah mahasiswa :',mahasiswa.jumlahMahasiswa)#Mencetak jumlah instance