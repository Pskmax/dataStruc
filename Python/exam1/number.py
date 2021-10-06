inp = input('Enter a positive number : ')
inp = int(inp)
mid = 0
if inp < 1:
    print(inp, 'is too low.')
    quit()
if inp > 15:
    print(inp, 'is too high.')
    quit()

dic16 = {
    1 : '1',
    2 : '2',
    3 : '3',
    4 : '4',
    5 : '5',
    6 : '6',
    7 : '7',
    8 : '8',
    9 : '9',
    10 : 'A',
    11 : 'B',
    12 : 'C',
    13 : 'D',
    14 : 'E',
    15 : 'F'
}

for i in range(1,inp+1):
    for j in range(1,inp+1):
        if i == 1:
            print(dic16[j],end=' ')
        elif i == inp+1:
            print(dic16[::-1])
    
    if i != 1 and i != inp:
        for j in range(mid):
            print(' ',end=' ') 

    if i >= 2 and i < inp:
        print(dic16[i-1],end=' ')
    
    if i >= inp:
        for j in range(1,inp):
            print(dic16[j],end=' ')

    if mid == 0:
        mid = inp - 2
    print()
    if i >= 1 and i < inp:
        print(dic16[i+1],end=' ')
    
