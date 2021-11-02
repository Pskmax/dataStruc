def checkMax(arr, maxNum = -99999999):
    if len(arr) == 0:
        return maxNum
    num = arr.pop()
    if maxNum < num:
        maxNum = num
    return checkMax(arr, maxNum)

if __name__ == '__main__':
    lst = list(map(int, input("Enter Input : ").split(' ')))
    print('Max :', checkMax(lst))