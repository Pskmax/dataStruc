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
        else :
            return 0
    def __str__(self):
        x = self
        s = ""
        for i in range(x.size()):
            s+=x.items[i] 
        return s
        
   
d = Stack()
ss = input('Enter expresion : ')
s = ""
for i in ss:
    if i in '({[)}]':
        s+=str(i)

v = {
    ')':'(',
    '}':'{',
    ']':'['
}
u,o,c =0,0,0

for i in s:
    if d.size()==0 or i in '([{':
        d.push(i)
    elif v[i] == d.top():
        d.pop()
    else :
        if d.top() in '([{' and d.top() != i:
            u+=1
        d.push(i)
        
        
for i in d.items:
    if i in '({[':
        o+=1
    if i in ')}]':
        c+=1
    
print(ss,end=' ')
if u!=0:
    print('Unmatch open-close')
elif o>c:
    print('open paren excess   ' + str(o) + ' : ' + ''.join([e for e in d.items]))
elif c>o:
    print('close paren excess')
else:
    print('MATCH')