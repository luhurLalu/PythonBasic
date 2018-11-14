# Daftar yg sudah dipakai : List, Dictionary, if_else, input,import,package,function,while,for
# mengambil data - data apotek dari package 'dataApotek' yg sudah dibuat
from dataApotek import * 
# import method/fungsi yang akan digunakan dalam menghitung total transaksi
from fungsi import *

# iterasi pertama untuk menampung nilai/jumlah perulangan
z = 0
# variable untuk embuat syntax looping
i = 'y'
# memulai looping while dengan kode 'i.upper()' yaitu untuk inputan y kapital/tidak
while i.upper() == 'Y':   
    #  variable inputan 1 untuk menentukan tujuan customer(pelanggan)
    pilihan = input(str('Apakah menggunakan resep atau tidak Y/N : '))    
    # kondisi awal if_else, dimana proses yg akan di eksekusi tergantung kepada inputan 1
    if pilihan.upper() == 'Y':
        # syntax pertama yg dieksekusi apabila inputan memenuhi syarat (inputan nama resep)
        resep = input(str('masukkan nama resep : '))
        # variable untuk menampung index obat didalam list obat
        x = 0
        # kondisi jika inputan 'resep' berada didalam list obat
        if resep in obat:
            # proses looping for untuk mencari inputan resep satu per satu didalam list obat
            ''' variable i sebagai penampung sementara data pencarian pada list '''
            ''' looping for ini berfungsi hanya untuk menentukan index list obat '''
            for i in obat:
                # jika perulangan sudah menemukan data list sesuai dengan 'resep'
                if i == resep:
                    # tambah nilai 1 pada variable x setiap kali perulangan 
                    x += 1
                    # syntax yang akan berjalan ketika data list ditemukan
                    print('Obat {} tersedia ditempat kami pada kotak no : {} \n dengan harga Rp.{} :'.format(resep,x,hargaObat[resep]))
                # tambah nilai 1 pada variable x setiap kali perulangan 
                x+=1
            tanya = input('Apakah anda ingin membeli obat {} ? Y/N : '.format(resep))                 
            # kondisi apabila variable 'tanya'/inputan = y
            if tanya.upper() == 'Y':
                # inputan jumlah obat yg akan dibeli
                jumlahBeli = int(input('Berapa yg ingin anda beli : '))
                # cetak inputan resep,jumlah pembelian,dan total pembayaran
                # (rumus ada didalam method yg diimport seblumnya)
                print('Anda mendapatkan obat {} sebanyak {} buah, dengan harga Rp.{}'
                .format(resep, jumlahBeli, totalBayar(jumlahBeli,hargaObat[resep])))
            # kondisi jika inputanselain 'y' (tidak membeli obat)
            elif tanya.upper() == 'N':
                print('Semoga anda sembuh tanpa obat :)')
        # kondisi apabila inputan resep tidak ada
        else:
            print('Maaf {} tidak tersedia di tempat kami, silahkan cari ditempat lain '.format(resep))
    # kondisi jika tidak menggunakan resep
    elif pilihan.upper() == 'N':
        keluhan = input(str('apa keluhan penyakit anda ? : '))          
        if keluhan in penyakit.keys():
            print('Obat yg anda butuhkan adalah {} dengan harga : Rp.{}/biji'.format(penyakit[keluhan],hargaObat[penyakit[keluhan]]))
            tanya = input('Apakah anda ingin membeli obat {} ? Y/N : ' 
            .format(penyakit[keluhan]))
            if tanya.upper() == 'Y':
                jumlahBeli = int(input('Berapa yg ingin anda beli : '))
                print('Anda mendapatkan obat {} sebanyak {} buah, dengan harga Rp.{}'
                .format(penyakit[keluhan], jumlahBeli, jumlahBeli*hargaObat[penyakit[keluhan]]))
            else:
                print('Semoga anda sembuh tanpa obat :)')
        else:
            print('maaf anda harus konsultasi ke dokter')
    # penambahan nilai 1 pd variable z setiap kali kondisi resep = Y/N(untuk menghitung jumlah transaksi)
    z += 1
    print('ini transaksi yang ke : ',z)
    # apabila mau melakukan transaksi lagi/tidak,apabila valuenya = Y maka akan kembali ke kondisi awal
    ''' yaitu dari inputan menggunakan resep atau tidak '''
    i = input('mau akses lagi ? Y/N : ')    
print('Alhamdulillah :)')