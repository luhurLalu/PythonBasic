class pythonProgramming():    
    __value = 0 #Private attribute
    def __init__(self, name, nim):
        self.name = name #public attribute
        self.nim = nim
    def practice(self,practicalValue):
        self.__value += practicalValue
    def theory(self, theoryValue):
        self.__value += theoryValue
    def check(self):
        if self.__value <= 60:
            print('name: ',self.name,'nim :',self.nim,'sorry u failed, lets try hard','youre value :',self.__value )
        else:
            print('name: ',self.name,'nim :',self.nim,'Congrats ! U passed','youre value :',self.__value)


zilong = pythonProgramming('gde zilong', 1410530196)
fanny = pythonProgramming('fanny', 1410530199)

zilong.value = 70 #tidak berpengaruh karena value sudah menjadi private

zilong.practice(20)
zilong.theory(35)
zilong.check()

fanny.practice(40)
fanny.theory(50)
fanny.check()
    