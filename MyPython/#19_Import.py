# import moduleDictionary #cara 1
# for i,x in moduleDictionary.biodata.items(): #Menampilkan item dr dictionary
#     print('ini adalah key : ',i,'& ini adalah value :',x)

# import moduleDictionary as a #menyederhanakan nama
# print(a.biodata)

# from moduleDictionary import biodata,nim #Lebih spesifik
# print(biodata)

# from moduleDictionary import biodata as bio #Mengganti nama fungsi
# print(bio)

from moduleDictionary import * #mengambil semua tanpa terkecuali
print(nim)
