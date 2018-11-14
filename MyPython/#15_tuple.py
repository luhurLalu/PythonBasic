# perbandingan tuple dengan list
# mengetahui ukuran
import sys
# mengetahui waktu proses
import timeit

identitas = [1,2]
identitas2 = (1,2)
# ukuran data list dan tuple
list = sys.getsizeof(identitas)
tuple = sys.getsizeof(identitas2)
# print(dir(tuple))#mengetahui apa saja assignment(perintah) didalam tipe data tuple

print('Ukuran data list :',list)
print('ukuran data tuple :',tuple)

print(100*'#')

data_list = timeit.timeit(stmt = '[1,2,3,4,5,6]',number = 12345)
data_tuple = timeit.timeit(stmt = '(1,2,3,4,5,6)',number = 12345)

print('waktu proses list :',data_list)
print('waktu proses tuple :',data_tuple)