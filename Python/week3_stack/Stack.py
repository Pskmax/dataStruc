class Stack:
    def __init__(self):
        self.items = []
    def push(self, i):
        return self.items.append(i)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return (len(self.items)==0)
    def size(self):
        return len(self.items)
    def top(self):
        if self.size()!=0:
            return self.items[-1]
    def __str__(self):
        return str(self.items)


s = input('Enter Input : ')
stack=Stack()
s=s.split(',')
for i in s:
    if i[0] == 'P':
        if stack.size() == 0:
            print('-1')
        else:
            temp = stack.pop()
            print('Pop =',temp ,'and Index =', str(stack.size()))
    else:
        if i[0] == 'A':
            i = i.split()
            stack.push(int(i[1]))
            print('Add =',stack.top() ,'and Size =', str(stack.size()))
         
if(stack.size()==0):
    print('Value in Stack = Empty ')
else:
    print('Value in Stack =' , *[str(e) for e in stack.items])