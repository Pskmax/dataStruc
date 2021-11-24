def bi_search(l, r, arr, x):
    if l > r:
        return False
    mid = (l+r)//2
    if arr[mid] == x:
        return True
    else:
        if arr[mid] < x:
            return bi_search(mid+1,r,arr,x)
        else:
            return bi_search(l,mid-1,arr,x)

inp = input('Enter Input : ').split('/')
arr = list(map(int,inp[0].split()))
arr = sorted(arr)
x = list(map(int,inp[1].split()))
for i in x:
    i+=1
    while not bi_search(0,len(arr)-1,arr,i) and i < max(arr):
        i+=1
    if i>max(arr):
        print('No First Greater Value')
    else:
        print(i)
