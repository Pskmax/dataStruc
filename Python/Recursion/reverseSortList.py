def reverseSort(lst):
    if not lst: 
        return lst
    return lst[-1:] + reverseSort(lst[:-1])

if __name__ == '__main__':
    lst =  list(map(int,input('Enter your List : ').split(',')))
    lst.sort()
    print('List after Sorted :', reverseSort(lst))