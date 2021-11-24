def insertion_sort(lst):
    n = len(lst)
    for i in range(1,n):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key

if __name__ == '__main__':
    inp = list(map(int,input('Enter input: ').split()))
    insertion_sort(inp)
    print(inp)