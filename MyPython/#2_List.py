
angka = [1, 3, 9, 11, 13, 15]

# Mengakses list
subangka1 = angka[-2]
subangka2 = angka[3]
# memotong list
subangka3 = angka[:4]
subangka4 = angka[2:4]

angka2 = [2, 4, 6, 8, 10, 12 ]
# Menambah list
angka3 = angka + angka2
# mengubah list
angka2 [2] = 3
# mengkopy isi list ke variable baru
a = angka2[:] # a akan mengkopy semua data angka2 tanpa ada perubahan pd angka2
a [2] = 3
# mengubah isi list dengan metode slicing
angka2 [2:5] = [9, 7, 5]

# List didalam List
x = [angka, angka2]
# mengakses list dlm multidimensial list
b = x[1][5]
# menggunakan method List
angka2.append(13)
# menggunakan function
y = len(angka2)
