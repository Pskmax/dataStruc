class Queue:
    def __init__(self) -> None:
        self.data = []
    def __str__(self) -> str:
        return str(self.data)
    def is_empty(self):
        return len(self.data) == 0
    def is_full(self):
        return len(self.data) >= 5
    def __len__(self):
        return len(self.data)
    def enqueue(self, new_data):
        return self.data.append(new_data)
    def dequeue(self):
        if self.is_empty():
            return
        return self.data.pop(0)
    def size(self):
        return len(self.data)

inp = input('Enter people and time : ').split()
q = Queue()
c1 = Queue()
c2 = Queue()
people = inp[0]
time = int(inp[1])
start = False
count = 0
number = 0
for i in people:
    q.enqueue(i)
#check list q
#print(q,c1,c2)

for j in range(0,time):
    number += 1
    print(number,end=' ')
    if j % 3 == 0:
        c1.dequeue()
    if start:
        count += 1
        if count % 2 == 0:
            c2.dequeue()
    if not c1.is_full():
        if not q.is_empty():
            c1.enqueue(q.dequeue())
        print(q,c1,c2)
    else:
        if not c2.is_full():
            if not q.is_empty():
                c2.enqueue(q.dequeue())
            print(q,c1,c2)
            start = True