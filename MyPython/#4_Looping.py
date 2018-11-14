# Iterable menggunakan list
motor = ['mio', 'supra', 'jupyter']
rokok = ['sampoerna', 'surya','dunhill', 'class mild']
hp = ['samsung', 'nokia', 'oppo']
# iterable menggunakan string
laptop = 'asus'

merk = [motor, rokok,hp]
# nested for
for i in merk:
    print (i)
    for x in i:
        print(x)
        for y in x:
            print(y)
