alien = {'color':'green', 'points':6}
print(alien['points'])
alien['points'] +=1
print(alien['points'])
del alien['color']
alien['ads'] = 'addd'

for key,value in alien.items():
    print("Key: "+str(key)+" value: "+str(value))
for key in alien.keys():
    print(key)
for value in alien.values():
    print(value)

lista = []

for number in range(30):
    new_alien = {'tipo':'alien','number':number}
    lista.append(new_alien)
for alie in lista[:5]:
    print(alie)

receita = {'sabores':['peperoni','calabesa'],'local':'cork', 'endereco':{'rua':'oliver plunket','num':23}}
for key,value in receita.items():
    print(key+" "+str(value))
