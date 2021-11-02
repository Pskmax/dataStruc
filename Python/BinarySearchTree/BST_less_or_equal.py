class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def Insert(self, node):
        if self.root is None:
            self.root = node
        else:
            tNode = self.root
            while True:
                if node.data >= tNode.data:
                    if tNode.right is None:
                        tNode.right = node
                        break
                    tNode = tNode.right
                else:
                    if tNode.left is None:
                        tNode.left = node
                        break
                    tNode = tNode.left
        return self.root
    
    def PrintTree(self,node,level=0):
        if node != None:
            self.PrintTree(node.right, level + 1)
            print('     ' * level, node)
            self.PrintTree(node.left, level + 1)

# -------------------------------------------------

bst = BinarySearchTree()
s = BinarySearchTree()
inp = input('Enter Input : ').split('/')
inp[0] = inp[0].split()
k = inp[1]
num = 0
for i in inp[0]:
    root = bst.Insert(TreeNode(int(i)))


bst.PrintTree(root)
print('--------------------------------------------------')
for i in inp[0]:
    if int(i) <= int(k):
        num += 1
print(num)