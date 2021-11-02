a = []
b = []
c = []

def hanoiList(start, dest):
    global a
    global b
    global c
    if start == 'A':
        x = a.pop(0)
    elif start == 'B':
        x = b.pop(0)
    else:
        x = c.pop(0)
    if dest == 'A':
        a.insert(0,x)
    elif dest == 'B':
        b.insert(0,x)
    else:
        c.insert(0,x)

def draw_tower(n, row):
    global a
    global b
    global c
    s1 = a[::-1]
    s2 = b[::-1]
    s3 = c[::-1]
    if row == 0:
        return
    if row == n:
        print('|  |  |')
    if len(a) >= row:
        print(s1[row-1],end='  ')
    else:
        print('| ',end=' ')
    if len(b) >= row:
        print(s2[row-1],end='  ')
    else:
        print('| ',end=' ')
    if len(c) >= row:
        print(s3[row-1],end='  ')
    else:
        print('| ',end=' ')
    if row != 0:
        print()
    draw_tower(n,row-1)


def move(n , start, aux, dest, n2):
    if n == 1:
        print ("move 1 from ",start,"to",dest)
        hanoiList(start, dest)
        draw_tower(n2,n2)
        return
    move(n-1, start, dest, aux, n2)
    print ("move",n,"from ",start,"to",dest)
    hanoiList(start, dest)
    draw_tower(n2,n2)
    move(n-1, aux, start, dest, n2)

def init_a(num, target):
    global a
    if num <= target:
        a.append(num)
        init_a(num+1,target)

n = int(input("Enter Input : "))
init_a(1, n)
draw_tower(n, n)
move(n,'A','B','C',n) 