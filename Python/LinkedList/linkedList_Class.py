class Node:
    def __init__(self,data):
        self.data=data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def push_front(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def push_tail(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return 
        current = self.head
        while(current.next):
            current = current.next
        current.next = new_node
        new_node.next = None
    def del_front(self):
        self.head = self.head.next
    def del_tail(self):
        new_node = self
        if self.head is None:
            self.head = new_node
            return 
        current = self.head
        while(current.next.next):
            current = current.next
        current.next = None
    def size(self):
        current = self.head
        n = 0
        while(current != None):
            n+=1
            current = current.next
        return n
    def isEmpty(self):
        return self.head == None
    def __str__(self):
        current = self.head
        s = ''
        while(current!=None):
            s+=str(current.data)+' '
            current = current.next
        return s
    def is_x_in(self,x):
        current = self.head
        while(current!=None):
            if current==x:
                return True
            current = current.next
        return False