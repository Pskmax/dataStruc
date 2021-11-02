class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def inorder(self, root): 
        if root is not None: 
            self.inorder(root.left) 
            print(root.data),
            self.inorder(root.right) 

    def insert(self, node):
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

    def delete(self, root, data):
        if root is None:
            return print('Error! Not Found DATA')
        if data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            if root.left is None and root.right is None:
                self.root = None
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.minValueNode(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        return root
        
        
    
    def minValueNode(self,node):
        current = node
        while(current.left is not None):
            current = current.left
        return current

    def PrintTree(self,node,level=0):
        if node != None:
            self.PrintTree(node.right, level + 1)
            print('     ' * level, node)
            self.PrintTree(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
root = None
for i in data:
    i = i.split()
    if i[0] == 'i':
        root = tree.insert(Node(int(i[1])))
        print('insert',i[1])
    elif i[0] == 'd':
        print('delete',i[1])
        root = tree.delete(root,int(i[1]))
    tree.PrintTree(root)