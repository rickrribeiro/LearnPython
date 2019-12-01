users = []
new_user={}
def create_user():
    new_user['name'] = input("What is your name: ")
    new_user['age'] = input("What is your age: ")
choose = 1
while choose!= 0:
    choose= int(input("1.New user\n2.List of users\n0.Quit\nOption: "))
    if choose == 1:
        create_user()
        users.append(new_user)
    elif choose == 2:
        print(users)

def pritar(message):
    print(message)

pritar("oi")

def agrs(arg1,arg2, default='luz'):
    print(arg1+" "+arg2+" "+default)

agrs(arg2='asd', arg1='abc')
agrs('bbb','aaa')
agrs('bbb','aaa','ccc')

#mid is an optional argument
def title(name,surname,midname=''):
    return name.title()+" "+surname.title()

print(title('ricardo','ribeiro'))

#Passar por valor
def nao_mod(lista):
    lista[1]='dd'


liste = ['a','b','c']
nao_mod(liste[:])
print(liste)
nao_mod(liste)
print(liste)
