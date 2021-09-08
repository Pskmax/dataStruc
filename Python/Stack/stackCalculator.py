class Stack:
    def __init__(self):
        self.items = []
    def push(self, i):
        return self.items.append(i)
    def pop(self):
        if self.isEmpty():
            return 0
        return self.items.pop()
    def isEmpty(self):
        return (len(self.items)==0)
    def size(self):
        return len(self.items)
    def top(self):
        if self.size()!=0:
            return self.items[-1]
    def peek(self):
        return self.items[-1]
    def __str__(self):
        return str(self.items)

class StackCalc:
    def __init__(self, type=""):
        self.type = type
        self.i = 0
    def run(self, type):
        s = Stack()
        for i in type:
            if i in '+-*/':
                x = s.pop()
                y = s.pop()
                if i == '+':
                    s.push(x+y)
                elif i == '-':
                    s.push(x-y)
                elif i == '*':
                    s.push(x*y)
                else:
                    s.push(x/y)
            elif i == 'DUP':
                s.push(s.peek())
            elif i == 'POP':
                s.pop()
            elif i == 'PSH':
                s.push()
            else:
                try:
                    s.push(int(i))
                except:
                    print("Invalid instruction:", i)
                    quit()
        self.i = s.pop()
    def getValue(self):
        return self.i

print("* Stack Calculator *")
arg = input("Enter arguments : ").split()
machine = StackCalc()
machine.run(arg)
print(f'{machine.getValue():.0f}')