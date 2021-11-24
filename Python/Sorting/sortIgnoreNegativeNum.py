def sortList(lst):
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if lst[j] > lst[j+1] and lst[j+1] >= 0:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            elif j < len(lst)-2 and lst[j] > lst[j+2] and lst[j+2] >= 0:
                lst[j], lst[j+2] = lst[j+2], lst[j]
    return lst

inp = [int(e) for e in input('Enter Input : ').split()]
print(*sortList(inp))