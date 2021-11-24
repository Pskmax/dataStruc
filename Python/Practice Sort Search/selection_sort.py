def selectionSort(lst):
    n = len(lst)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i],lst[min_index] = lst[min_index],lst[i]

if __name__ == '__main__':
    inp = list(map(int,input('Enter input: ').split()))
    selectionSort(inp)
    print(inp)
