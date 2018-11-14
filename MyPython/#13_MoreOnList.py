# tambahan method untuk mengakses List
merkHp = ['oppo', 'samsung', 'sony', 'asus']
# tambah isi list sesuai urutan
merkHp.append('apple')
print(merkHp)
# tambah isi list sesuai keinginan
merkHp.insert(2,'asus')
print(merkHp)
# menghitung jumlah isi list yang sama
hitung = merkHp.count('asus')
print(hitung)
# perpanjang output
merkHp.extend('mito')
print(merkHp)
# hapus isi list
merkHp.remove('oppo')
print(merkHp)
# cetak terbalik
merkHp.reverse()
print(merkHp)