rokok = ['sampoerna', 'surya','dunhill', 'class mild']
cari = input('Masukkan nama rokok : ')

if cari in rokok:
    print(cari, 'ditemukan di list rokok yang ke -',rokok.index(cari)+1)
else:
    print(cari, 'tidak ditemukan di list rokok')





