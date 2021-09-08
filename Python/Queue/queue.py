class Queue:
    def __init__(self) -> None:
        self.data = []
    def __str__(self) -> str:
        x = ''
        if not self.is_empty():
            for i in self.data:
                x += str(i)
            return ', '.join(x)
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
# test input E 1,E 2,E 3,D,D,E 4
x = input('Enter Input : ').split(',')
q = Queue()
ans = []
for i in x:
    if i[0] == 'D':
        if not q.is_empty():
            temp1 = q.dequeue()
            ans += temp1
            print(temp1, '<-', q)
        else:
            print("Empty")     
    elif i[0] == 'E':
        temp2 = i.split()
        y = temp2[1]
        q.enqueue(y)
        print(q)
if len(ans) == 0:
    print('Empty',end='')
print(', '.join(ans),':', q)