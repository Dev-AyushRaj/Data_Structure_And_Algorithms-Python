# Implementing Deque using Doubly Linked list concept
class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item = item
        self.prev = prev
        self.next = next

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):
        return self.front == None
    
    def create_Deque(self,data):
        if not data:
            return
        for val in data:
            self.insert_rear(val)
    
    def insert_front(self,value):
        new_node = Node(value)
        self.item_count += 1
        if not self.front:
            self.front = new_node
            self.rear = new_node 
            return
        new_node.next = self.front
        self.front.prev = new_node
        self.front = new_node

    def insert_rear(self,value):
        new_node = Node(value)
        self.item_count += 1
        if not self.front:
            self.front = new_node
            self.rear = new_node
            return
        new_node.prev = self.rear
        self.rear.next = new_node
        self.rear = new_node

    def delete_front(self):
        if not self.front:
            raise IndexError("Deque underflow")
        self.item_count -= 1
        if not self.front.next:
            self.front = None
            self.rear = None
            return
        self.front = self.front.next
        self.front.prev = None

    def delete_rear(self):
        if not self.front:
            raise IndexError("Deque underflow")
        self.item_count -= 1
        if not self.front.next:
            self.front = None
            self.rear = None
            return
        self.rear = self.rear.prev
        self.rear.next = None

    def get_front(self):
        if not self.front:
            raise IndexError("Deque Underflow")
        else:
            return self.front.item
        
    def get_rear(self):
        if not self.front:
            raise IndexError("Deque Underflow")
        else:
            return self.rear.item
    
    def size(self):
        return self.item_count
    
d1 = Deque()
d1.create_Deque([20,30,40,50])
d1.insert_front(10)
d1.insert_rear(60)
try:
    d1.delete_rear()
except IndexError as e:
    print(e.args[0])
try:
    d1.delete_front()
except IndexError as e:
    print(e.args[0])
try:
    print(d1.get_front())
except IndexError as e:
    print(e.args[0])
try:
    print(d1.get_rear())
except IndexError as e:
    print(e.args[0])
print(f"Number of element in Deque is:{d1.size()}")
