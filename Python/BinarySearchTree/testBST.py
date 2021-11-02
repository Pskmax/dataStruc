class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self,node):
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
    
    def printTree(self,node,level=0):
        if node is not None:
            self.printTree(node.right,level + 1)
            print('     ' * level,node)
            self.printTree(node.left,level + 1)

if __name__ == '__main__':
    bst = BST()
    inp = input('Enter Input : ').split()
    for i in inp:
        root = bst.insert(Node(int(i)))
    bst.printTree(root)
