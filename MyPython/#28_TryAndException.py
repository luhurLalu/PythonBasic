
while True:
    try:
        angka1 = int(input('masukkan angka pembilang : '))
        angka2 = int(input('Masukkan angka penyebut : '))
        hasil = angka1/angka2
        break
    except ValueError:
        print('Anda tidak menginputkan angka, silahkan ulangi !')
    except ZeroDivisionError:
        print('Angka tidak bisa dibagi dengan 0, silahkan ulangi !')
    except Exception as err:
        print(err)
    except KeyboardInterrupt:
        print('proses masih berjalan')
print('hasil pembagian adalah :',hasil)
'''
    Type exception error :
    1.IOError = error saat buka file
    2.ImportError = package yg diimport tidak ditemukan
    3.ValueError = contoh harus inputkan angka tetapi inputan string
    4.Division By Zero = pembagi dengan angka 0
    5.KeyboardInterupted = agar tdk menghentikan proses program yg masih berjalan
    6.EOFError
'''

