def reverseSort(lst):
    if not lst: 
        return lst
    return lst[-1:] + reverseSort(lst[:-1])

lst =  list(map(int,input('Enter Input : ').split(',')))
lst.sort()
print('List after Sorted :',reverseSort(lst))