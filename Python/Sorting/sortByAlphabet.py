def checkAlphabet(inp):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in inp:
        if i in alphabet:
            return i

def sortAlphabet(inp):
    for i in range(len(inp)):
        for j in range(len(inp)-i-1):
            if checkAlphabet(inp[j]) > checkAlphabet(inp[j+1]):
                inp[j], inp[j+1] = inp[j+1], inp[j]
inp = input('Enter Input : ').split()
sortAlphabet(inp)
print(*inp)
