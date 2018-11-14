# fungsi dengan argumen sederhana
def handphone(hp):
    print('merk hp adalah', hp)
handphone('oppo')
# fungsi dengan keywords argumen 
def laptop(merk,proseccor):
    print('merk laptop:',merk)
    print('proseccor:',proseccor)
laptop(merk='Asus',proseccor='AMD')
# fungsi dengan argumen default
def spesifikasi(merk='Asus',proseccor='AMD',ram='1 GB'):
    print('merk : ',merk)
    print('proseccor : ',proseccor)
    print('RAM : ',ram)
spesifikasi(ram='3 GB', proseccor='Intel Core i7')