from collections import Counter

inp = input('Enter number end with (-1) : ').split()
lst = []
for i in inp:
    if '-1' not in inp:
        print('Invalid INPUT !!!')
        quit()

for i in inp:
    if i != '-1':
        lst.append(i)
    elif i == '-1':
        break
if lst == set(lst) or lst == []:
    print('Not found')
else:
    #print(max(lst,key=lst.count))
    ans = Counter(lst).most_common(2)
    print(ans[0][0])
