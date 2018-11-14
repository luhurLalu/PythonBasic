# tujuan dari function adalah untuk membuat algoritma yg bisa dipanggil berulang kali
harga = 100000
beli = 3
def laptop():
    print('ini Laptop')
def hitung(x,y):
    hasil=x*y
    print(hasil)
def beliLaptop():
    laptop()
    hitung(harga, beli)    
beliLaptop()