# Teknik looping
heroML = ['zilong','fanny','balmond','zhask']
tipe = ['fighter/assasin','assasin','tank/fighter','mage']
rank = {'warrior','elite','master','grandmaster','epic','legend','mythic'}
lengkap = {
    'zilong' : 'fighter/assasin',
    'fanny' : 'assasin',
    'zhask' : 'mage'
}
# membuat index sederhana
i = 1
for hero in heroML:
    print(i,':',hero)
    i += 1
# teknik index
print(100*'=')
for index,hero in enumerate(heroML):
    print(index,':',hero)
# zip(menggabungkan)
print(100*'=')
for hero, tipe in zip(heroML,tipe):
    print(hero,'adalah jenis hero :',tipe)
# Mengurutkan berdasarkan abjad
print(100*'=')
for ranked in sorted(rank):
    print(ranked)
# dictionary
print(100*'=')
for i in lengkap.keys():#lengkap.keys,values,items
    print(i)