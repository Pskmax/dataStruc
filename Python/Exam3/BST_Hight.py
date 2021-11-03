class Node:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def create(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            current = self.root
            while True:
                if current.data < data:
                    if current.right is None:
                        current.right = Node(data)
                        break
                    current = current.right
                else:
                    if current.left is None:
                        current.left = Node(data)
                        break
                    current = current.left
        return self.root

    def printTree(self,node,level = 0):
        if node is not None:
            self.printTree(node.right, level + 1)
def height(obj):
    if obj is None:
        return -1
    leftHight = height(obj.left)
    rightHeight = height(obj.right)
    if leftHight > rightHeight:
        return leftHight + 1
    else:
        return rightHeight + 1
    

print(" *** Binary Search Tree Height ***")
tree = BinarySearchTree()
arr = list(map(int, input("Enter Input : ").split()))

for e in arr:
    tree.create(e)
print("Height = ",height(tree.root),end="\n\n")