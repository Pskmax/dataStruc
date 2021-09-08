class Queue:
    def __init__(self) -> None:
        self.data = []
    def __str__(self) -> str:
        x = ''
        if not self.is_empty():
            for i in self.data:
                x += str(i) + ', '
            return x
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

x = input('Enter Input : ').split('/')
q = Queue()
book = x[0].split()
dORe = x[1].split(',')

for i in book:
    q.enqueue(i)

for j in dORe:
    if j[0] == 'D':
        if not q.is_empty():
            q.dequeue()
    elif j[0] == 'E':
        temp = j.split()
        y = temp[1]
        q.enqueue(y)

book_list = []
while not q.is_empty():
    book_list.append(q.dequeue())

checkDuplicate = set(book_list)
if len(checkDuplicate) != len(book_list):
    print('Duplicate')
else:
    print('NO Duplicate')