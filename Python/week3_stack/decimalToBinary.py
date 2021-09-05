class Stack :
    n = []
    def decTobin(self, decnum):
        if decnum > 1:
            Stack().decTobin(decnum//2)
        print(decnum%2,end='')

print(" ***Decimal to Binary use Stack***")

token = int(input("Enter decimal number : "))

print("Binary number : ",end='')

Stack().decTobin(token)
