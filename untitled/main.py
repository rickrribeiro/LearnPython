i=0
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

#r - read, w - write, a - append (write without delete), r+ - read and write
with open('numbers','a') as file:
    file.write('teste')