elektronik = ['kipas','laptop','tv','hp','lcd']
# cetak isi list beserta index
# for index,value in enumerate(elektronik):
#     print(index+1,':',value)

# cari key dan value list berdasarkan keywords

ulang = 'y'
while ulang.upper() == 'Y':    
    keywords = input(str('masukkan pencarian : '))    
    x = 0
    if keywords in elektronik:
        for i in elektronik:    
            if i == keywords:
                x += 1
                print(keywords,' ditemukan pada perulangan ke : ',x)
                continue            
            x += 1
            # print('ini adalah {} pada perulangan ke : {}'.format(i,x))                    
    else:
        print('maaf {} tidak termasuk kedalam elektronik'.format(keywords))
    ulang = input('apakah ingin hitung ? y/n : ')
