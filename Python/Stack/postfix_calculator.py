class postFixeval:
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

print(" ***Postfix expression calcuation***")
token = list(input("Enter Postfix expression : ").split())
stack = postFixeval()
for i in token:
    if i not in '+-*/':
        y = stack.push(int(i))
    if i == '+':
        y = stack.pop()
        x = stack.pop()
        stack.push(x+y)
    elif i=='-':
        y = stack.pop()
        x = stack.pop()
        stack.push(x-y)
    elif i=='*':
        y = stack.pop()
        x = stack.pop()
        stack.push(x*y)
    elif i=='/':
        y = stack.pop()
        x = stack.pop()
        stack.push(x/y)
ans = stack.items[0]
print('Answer :  {:.2f}'.format(ans))