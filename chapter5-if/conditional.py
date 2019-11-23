cars = ['mercedes','audi','bmw']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

if cars[2].upper() == 'BMW':
    print("eh")

ages = [1,2,18,45,46]

for age in ages:
    if age >10 and age < 30:
        print(age)
    elif age > 11 and age%2 != 0:
        print("mid: "+str(age))

if 'bmw' in cars:
    print("tem bmw")
else:
    print("nao tem bwm")
if 'ferrari' in cars:
    print("tem ferrari")
else:
    print("nao tem ferrari")

carro = "asd"

if carro not in cars:
    print("carro n ta")
    