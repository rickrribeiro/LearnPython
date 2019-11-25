text = "Hello\nWhat is your name?\n"
name = input(text)
print("hello, "+name)
current_number = 1

while current_number <= 5:
    print(current_number)
    current_number+=1

message = ""
while message != "quit":
     message = input("If u want to quit, write quit: ")

for i in range(5):
    if i == 2:
        break
    else:
        print(i)

pets = ['dog','cat', 'dog','cat','fish']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)