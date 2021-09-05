def odd_even(arr, s):
    if isinstance(arr,list):
        lst = [] #กรณีมีตัวเดียว
        for i in range(len(arr)):
            if(s == 'Even' and i % 2 != 0):
                lst.append(arr[i])
            elif(s == 'Odd' and i % 2 == 0):
                lst.append(arr[i])
    elif isinstance(arr,str):
        lst = ''
        for i in range(len(arr)):
            if(s == 'Even' and i % 2 != 0):
                lst += arr[i]
            elif(s == 'Odd' and i % 2 == 0):
                lst += arr[i]
    return lst    

print('*** Odd Even ***')
x,arr,s = input('Enter Input : ').split(',')
if x == 'S':
    arr = str(arr)
elif x == 'L':
    arr = arr.split(' ')
print(odd_even(arr,s))

