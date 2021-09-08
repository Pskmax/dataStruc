x = input("Enter Input : ")
x = int(x)
z = x
x = x+1
y = 1
round = 1
for i in range(x+1):

    for j in range(x):
        print(".",end = "")
    for k in range(y):
        print("#",end="")
    print("+", end="")
    if round==1 or round == (z+2):
        for l in range(z):
            print("+",end="")
    else:
        for l in range(z):
            print("#",end="")
    print("+", end="")
    x = x-1
    y = y+1
    round = round + 1
    print()
round2 = round - 1
for i in range(round-1):
    x = x+1
    y = y-1
    print("#", end="")
    if round == (y+1) or round == (z + 2 + round2):
        for l in range(z):
            print("#", end="")
    else:
        for l in range(z):
            print("+", end="")
    print("#", end="")
    for j in range(y):
        print("+",end = "")
    for k in range(x):
        print(".",end="")
    round = round+1
    print()