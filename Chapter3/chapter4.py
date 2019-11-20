names = ['ricardo','arba','xhoerta']
for name in names:
    print(name)
    print("e")
print("acabou a identação")

numbers = list(range(1,5))
for value in numbers:
    print(value)
square = list(range(1,7,2))
print(square)
numeros = [1,2,3,4,5,6,7,8,9]
print(max(numeros))
print(min(numeros))
print(sum(numeros))
print(numeros[0:3])
print(numeros[:4])
copy = numeros[:]#se nao botar p dar slice ele só passa a referencia
print(copy)

