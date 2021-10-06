print("*** Fun with Drawing ***")
inp = int(input('Enter input : '))
point = inp
plus = -1
floor = 1
for i in range(inp):
    point_mid = ((point)*2)-3
    for j in range(point-1):
        print('.',end='')
    print('*',end='')
    if i > 0:
        for j in range(plus):
            print('+',end='')
        if inp != 1:
            print('*',end='')
    for j in range(point_mid):
        print('.',end='')
    if floor != inp:
        print('*',end='')
    if i > 0:
        for j in range(plus):
            print('+',end='')
        if inp != 1:
            print('*',end='')
    for j in range(point-1):
        print('.',end='')

    plus += 2
    point -= 1
    floor += 1
    print()
plus = ((plus-2)*2) - 1
while plus >= -1:
    point += 1
    for i in range(point):
        print('.',end='')
    print('*',end='')
    for i in range(plus):
        print('+',end='')
    if plus != -1:
        print('*',end='')
    for i in range(point):
        print('.',end='')

    plus -= 2
    print()

    