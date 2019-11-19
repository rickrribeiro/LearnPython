names = ['ricardo', 'arbiola', 'xhoerta']
print(names)
names[1]='arba'
print(names)
names.append('NomeNovo')
names.insert(0, 'rick')
print(names)
del names[1]
print(names)
print(names[1].title())
print(names[-1]) #printa last item
poped = names.pop()
print("retirado: "+poped)
print(names)
names.insert(6, 'asd')#vai pro final pq n tem até la e vira o 4º
print(names.pop(-1))
print(names)
names.append('lol')
names.append('lol')
names.append('lol')
print(names)
names.remove('lol') #remove só o primeiro
names.sort()
print(names)
names.sort(reverse=True)
print(sorted(names)) #só printa em ordem mas n muda
print(names)
names.reverse()
print(names)
len(names)