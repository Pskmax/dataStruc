def checkMin(arr, min = 999999):
    if len(arr) == 0:
        return min
    num = arr.pop()
    if min > num:
        min = num
    return checkMin(arr,min)

inp = list(map(int,input('Enter Input : ').split()))
print('Min :',checkMin(inp))
