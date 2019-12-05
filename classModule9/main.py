import dog
#from dog import Canil, dog
#i can import a module inside another module
my_dog = dog.Dog('Kiara',3)
my_dog.info()
print(my_dog.name)

security = dog.security_dog('rotweiller',12)

print(security.name)
select=1
canil = dog.canil("Canils")
while select != 0:
    select = int(input("1.Add\n2.List\n0.Exit\n"))
    if select == 1:
        canil.addDog(dog.Dog(input("Name: "),int(input("Age: "))))
    elif select == 2:
        canil.printDog()

print(security.name)