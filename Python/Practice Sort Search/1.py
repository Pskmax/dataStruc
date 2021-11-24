# tree AVL

# sort
# bubble
# insertion
# selection

# search
# binary search
# hash
def bubble_sort(lst):
    n = len(lst)
    step = 0
    move = 0
    for i in range(n-1,0,-1):
        step += 1
        check = False
        for j in range(i):
            if lst[j] > lst[j+1]:
                move = lst[j]
                lst[j],lst[j+1] = lst[j+1],lst[j]
                check = True
        if not check:
            print(f"last step : {lst} move[None]")
            break
        elif step == n-1:
            print(f"last step : {lst} move[{move}]")
            break
        else:
            print(f"{step} step : {lst} move[{move}]")

if __name__ == '__main__':
    inp = list(map(int,input('Enter Input: ').split()))
    bubble_sort(inp)