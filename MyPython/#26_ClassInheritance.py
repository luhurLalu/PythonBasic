class kursi():
    def __init__(self, nama, jenis):
        self.namaKursi = nama
        self.jenisKursi = jenis
    
    def checkpoint(self):
        print('Nama kursi : ',self.namaKursi,'jenis kursi : ',self.jenisKursi)

class kursi2(kursi):
    def checkpoint(self):
        print('Ini adalah override method kursi')

a = kursi('bandidos','kayu')
a.checkpoint()

b = kursi2('broklyn','besi')
b.checkpoint()