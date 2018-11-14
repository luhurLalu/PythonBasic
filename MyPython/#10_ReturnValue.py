# fungsi dengan return value
def kubus(panjang, lebar):
    hasil = panjang * lebar
    return hasil
a = kubus(3,2)
print('luas kubus : ',a)

# return value dengan multiple argumen
def segitiga(alas,tinggi):
    total = 1/2 * alas * tinggi
    return total
b = segitiga(a,5)
print(b)

