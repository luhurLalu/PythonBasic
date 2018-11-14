# while dengan integer
number = 0
while number < 7:
    print('angka ini =',number)    
    number += 1
print('number ! < 7 ')

# while menggunakan boolean
numb = 0
start = True
while start:
    print('inside while')
    if numb is 10:
        start = False
        print('dibawah 10')
    numb += 1
# pass, continue, break didalam while
number = 0
while number <7:
    print ('angka :',number)
    if number is 5:
        break
        continue
        pass
    number += 1
    
else:
    print('angka dibawah 7')
