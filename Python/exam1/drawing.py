inp = int(input('Input : '))
if inp <= 0:
    print('!!!Please enter number greater than zero!!!')
    quit()

print()
star = 1
mid = (2*inp) - 2
for i in range(inp-1):
    for j in range(star):
        print('*',end='')
    for j in range(mid):
        print(' ',end='')
    for j in range(star):
        print('*',end='')
    star +=1
    mid -=2
    print()

for i in range(2*inp):
    print('*',end='')
print()

star -= 1
mid += 2
for i in range(inp-1):
    for j in range(star):
        print('*',end='')
    for j in range(mid):
        print(' ',end='')
    for j in range(star):
        print('*',end='')
    star -=1
    mid +=2
    print()
