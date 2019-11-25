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