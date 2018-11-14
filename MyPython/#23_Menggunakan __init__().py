class snakes():
    # this is a special method, because it will call every class is using
    def __init__(self,nameSnakes,ageSnakes): #auto call when running program
        self.name = nameSnakes
        self.age = ageSnakes

    #Method
    def waterSnakes(self): 
        print(self.name,'Is a water snake and the age is :',self.age)

    def landSnakes(self):
        print(self.name,'Is a land snake and the age is :',self.age)

animal1 = snakes('anaconda','3 years')

animal1.landSnakes()
