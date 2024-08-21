with open ('out.txt', 'r') as file:
    lines = file.read().split()
    print(lines)
    for i in lines:
        print(chr(int(i)), end="")
