class Dog():
    def __init__(self,name,age):
        self.name= name
        self.age=age

    def info(self):
        print(self.name+" "+str(self.age))
    def latir(self):
        print("au")
#inheritance
class security_dog(Dog):
    def __init__(self,name,age):
        super().__init__(name,age)
    def latir(self): #override
        print("au au")

class canil():
    def __init__(self,name):
        self.name = name
        self.dogs=[]
    def addDog(self,dog):
        self.dogs.append(dog)
    def printDog(self):
        for dog in self.dogs:
            print(dog.name)