def binarySearch(left,right,lst,x):
    if left > right:
        return False
    mid = (left+right)//2
    if lst[mid] == x:
        return True
    else:
        if lst[mid] < x:
            return binarySearch(mid+1,right,lst,x)
        elif lst[mid] > x:
            return binarySearch(left,mid-1,lst,x)

if __name__ == '__main__':
    inp = list(map(int,input('Enter input: ').split()))
    binarySearch(inp)
    print(inp)