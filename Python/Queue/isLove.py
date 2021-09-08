class Queue:
    def __init__(self) -> None:
        self.data = []
    def __str__(self) -> str:
        x = ''
        if not self.is_empty():
            for i in self.data:
                x += str(i) + ' '
            return ', '.join(x.split())
        return 'Empty'
    def is_empty(self):
        return len(self.data) == 0
    def __len__(self):
        return len(self.data)
    def enqueue(self, new_data):
        return self.data.append(new_data)
    def dequeue(self):
        if self.is_empty():
            return 'Empty'
        return self.data.pop(0)
    def size(self):
        return len(self.data)

dictQ = {
    '0:0' : 'Eat:Res.',
    '0:1' : 'Eat:ClassR.',
    '0:2' : 'Eat:SuperM.',
    '0:3' : 'Eat:Home',
    '1:0' : 'Game:Res.',
    '1:1' : 'Game:ClassR.',
    '1:2' : 'Game:SuperM.',
    '1:3' : 'Game:Home',
    '2:0' : 'Learn:Res.',
    '2:1' : 'Learn:ClassR.',
    '2:2' : 'Learn:SuperM.',
    '2:3' : 'Learn:Home',
    '3:0' : 'Movie:Res.',
    '3:1' : 'Movie:ClassR.',
    '3:2' : 'Movie:SuperM.',
    '3:3' : 'Movie:Home'
}

# test input 0:0 2:0,1:3 3:3,2:1 2:1
inp = input('Enter Input : ').split(',')
myQ = Queue()
yourQ = Queue()
temp = []
for i in inp:
    i = i.split()
    myQ.enqueue(i[0])
    yourQ.enqueue(i[1])
# check myQ and yourQ
print('My   Queue =',myQ)
print('Your Queue =',yourQ)
# dict myQ and yourQ
print('My   Activity:Location =',', '.join([dictQ[e] for e in myQ.data]))
print('Your Activity:Location =',', '.join([dictQ[e] for e in yourQ.data]))

mylist = []
for j in myQ.data:
    j = j.split(':')
    mylist.append(j)
yourList = []
for j in yourQ.data:
    j = j.split(':')
    yourList.append(j)

point = 0
for i in range(len(mylist)):
    if mylist[i][0] == yourList[i][0] and mylist[i][1] != yourList[i][1]:
        point += 1
    elif mylist[i][0] != yourList[i][0] and mylist[i][1] == yourList[i][1]:
        point += 2
    elif mylist[i][0] == yourList[i][0] and mylist[i][1] == yourList[i][1]:
        point += 4
    else:
        point -= 5

if point >= 7:
    print('Yes! You\'re my love! : Score is',point,end='.')
elif point > 0:
    print('Umm.. It\'s complicated relationship! : Score is',point,end='.')
else:
    print('No! We\'re just friends. : Score is',point,end='.')

    