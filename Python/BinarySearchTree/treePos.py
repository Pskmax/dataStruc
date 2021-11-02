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
    
    def checkPos(self, data, node):
        if data == self.root.data:
            return print('Root')
        if node.data == data:
            if node.left is not None or node.right is not None:
                return print('Inner')
            else:
                return print('Leaf')
        elif node.data > data:
            if node.left is not None:
                self.checkPos(data,node.left)
            else:
                return print('Not exist')
        elif node.data <= data:
            if node.right is not None:
                self.checkPos(data,node.right)
            else:
                return print('Not exist')

# -------------------------------------------------

bst = BinarySearchTree()
inp = input('Enter Input : ').split()
for i in inp[1:]:
    root = bst.Insert(TreeNode(int(i)))
bst.PrintTree(root)
bst.checkPos(int(inp[0]),root)