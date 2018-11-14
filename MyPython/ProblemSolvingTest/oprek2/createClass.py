class mahasiswa():    
    jumlahMahasiswa = 0
    nilaiMahasiswa = 0    
    def __init__(self, nama, nim):    
        self.namaMahasiswa = nama
        self.nimMahasiswa = nim
    
        mahasiswa.jumlahMahasiswa +=1                
    def nilaiUas(self, nilai):
        self.nilaiMahasiswa += nilai / 2
    def nilaiUts(self, nilai):
        self.nilaiMahasiswa += nilai / 2
    
    def checkPoint(self):                
        if self.nilaiMahasiswa <= 50:
            print(self.namaMahasiswa,'Anda tidak lulus, nilai anda :', self.nilaiMahasiswa)
        else:
            print(self.namaMahasiswa,'Anda lulus, nilai anda :',self.nilaiMahasiswa)
        
