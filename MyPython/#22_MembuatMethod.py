class snake(): #class harus diatas karena python merupakan interpreted leanguage(bahasa berurutan)
    name = 'cobra'

    def waterSnakes(self):
        print(self.name,'Is a water snake !')
    
    def landSnakes(self,argumen):
        print(self.name,'Is a land snake !',argumen)
# main program
# Deklarasi objek terhadap class
animal1 = snake()
animal2 = snake()
animal3 = snake()
# deklarasi nilai objek
animal1.name = 'anaconda'
animal2.name = 'sea snake'
animal3.name = 'black mamba'
# deklarasi objek ke method
animal1.waterSnakes()
animal3.landSnakes('and one of 10 most dangerous snakes')
