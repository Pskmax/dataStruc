class Node:
    def __init__(self, data, next = None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
    # insert in front of head
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    # insert after head
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return 
        current = self.head
        while(current.next):
            current = current.next
        current.next = new_node
        new_node.next=None
    def insert_after_node(self, previous_node, new_data):
        if previous_node is None:
            print("The given previous node must in LinkedList.")
            return
        new_node = Node(new_data)
        new_node.next = previous_node.next
        previous_node.next = new_node
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