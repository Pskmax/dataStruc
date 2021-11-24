def bubbleSort(lst):
    n = len(lst)
    for i in range(n-1):
        move = ''
        for j in range(0,n-i-1):
            if lst[j] > lst[j+1]:
                move = str(lst[j])
                lst[j], lst[j+1] = lst[j+1], lst[j]
        if move == '':
            print('last step :',lst,'move[None]')
            break
        elif i == n-2:
            print('last step :',lst,'move['+move+']')
            break
        else:
            print(i+1,'step :',lst,'move['+move+']')

inp = list(map(int,input('Enter Input : ').split()))
bubbleSort(inp)

'''
----------Input----------
Enter Input : 4 3 2 1
----------Output----------
1 step : [3, 2, 1, 4] move[4]
2 step : [2, 1, 3, 4] move[3]
last step : [1, 2, 3, 4] move[2]
'''