i=0
try:
    with open('numbers') as file:
        fil = file
        content = fil.read()
        lines = fil.readlines()
        print(content.rstrip()) #rstrip is used to remove whitespaces from the right side of a string
        if str(1) in content:
          print("tem")

        print(lines)
        for line in lines:
           print(line)
except FileNotFoundError:
    print("arquivo n enontrado")
except ZeroDivisionError:
    pass
#r - read, w - write, a - append (write without delete), r+ - read and write
with open('numbers','a') as file:
    file.write('teste')
