print("*** Fun with Drawing ***")
x = input("Enter input : ")
x = int(x)
x1 = x
for i in range(x):
    y = ((x - 1) * 2) - 1
    z = (((x1)-x)*2)-1
    for j in range(x-1):
        print(".",end = "")
    print("*",end = "")
    if z > 0:
        for l in range(z):
            print("+", end="")
        if x != 1:
            print("*", end="")
    for k in range(y):
        print(".",end = "")
    print("*", end="")
    if z > 0:
        for l in range(z):
            print("+", end="")
        print("*", end="")
    for j in range(x-1):
        print(".",end = "")
    print()
    x = x-1
z = ((z*2)+1)
while z >= 0:
    x = x+1
    z = z-2
    for j in range(x):
        print(".", end="")
    print("*", end="")
    if z > 0:
        for l in range(z):
            print("+", end="")
        print("*", end="")
    for j in range(x):
        print(".",end = "")
    print()