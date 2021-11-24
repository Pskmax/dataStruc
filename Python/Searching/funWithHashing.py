class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class Hash:
    def __init__(self,size,maxCollision):
        self.size = size
        self.maxCollision = maxCollision
        self.table = [None]*size

    def getIndex(self,key):
        index = 0
        for i in key:
            index += ord(i)
        return index % self.size

    def isFull(self):
        sum = 0
        for i in range(len(self.table)):
            if self.table[i] is not None:
                sum += 1
        return sum == self.size
    
    def insert(self,data):
        if self.isFull():
            print('This table is full !!!!!!')
            quit()
        key, value = data.key, data.value
        count = 0
        hash_index = self.getIndex(key)
        while count < self.maxCollision:
            index = (hash_index + (count ** 2)) % self.size
            if self.table[index] is None:
                self.table[index] = data
                return
            count += 1
            print('collision number',count,'at',index)
        print('Max of collisionChain')
    
    def __str__(self):
        string = ''
        for i in range(self.size):
            string += '#'+str(i+1)+'\t'+str(self.table[i])+'\n'
        string += '---------------------------'
        return string
    
# 3 2/1+1 I,OnE Love,abcde I,#$ew2 KMITL,kk KMITL,z Love
print(' ***** Fun with hashing *****')
inp = input('Enter Input : ').split('/')
inpL = list(map(int,inp[0].split()))
inpR = inp[1].split(',')
lst = []

for i in inpR:
    key,value = i.split()
    lst.append(Data(key,value))

h = Hash(inpL[0],inpL[1])
for i in lst:
    h.insert(i)
    print(h)
