def bubbleSort(lst):
    n = len(lst)
    step = 0
    for i in range(n-1,0,-1):
        #รอบ
        step += 1
        change = False
        for j in range(i):
            #เรียง
            if lst[j] > lst[j+1]:
                move = lst[j]
                lst[j],lst[j+1] = lst[j+1],lst[j]
                change = True
        if change == False:
            print(f"last step : {lst} move [None]")
            break
        elif step == n-1:
            print(f"last step : {lst} move [{move}]")
            break
        else:
            print(f"{step} step : {lst} move [{move}]")

inp = input('Enter Input : ').split()
bubbleSort(inp)