rokok = set()

rokok.add('surya')
rokok.add('dunhill')
rokok.add('sampoerna')
rokok.add('calss mild')

print(rokok)

genap = {2,4,6,8}
ganjil = {1,3,5,7}
prima = {2,3,5,7}

print(ganjil | genap)#Union(persatuan)
print(ganjil.union(genap))#cara ke 2

print(ganjil & prima)#intersection(angka yg sama)
