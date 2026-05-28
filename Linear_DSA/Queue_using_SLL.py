# Queue using Singly linked list concept
class Node:
    def __init__(self,items = None,next = None):
        self.items = items
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):
        return self.front == None
    
    def create_queue(self,data):
        if not data:
            return
        for val in data:
            self.enqueue(val)
    
    def enqueue(self,value):
        new_node = Node(value)
        self.item_count += 1
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow")
        value = self.front.items
        self.front = self.front.next
        self.item_count -= 1
        if self.front == None:
            self.rear = None
        return value
    
    def get_front(self):
        if not self.is_empty():
            return self.front.items
        else:
            raise IndexError("Queue Underflow")
        
    def get_rear(self):
        if not self.is_empty():
            return self.rear.items
        else:
            raise IndexError("Queue Underflow")
        
    def size(self):
        return self.item_count

q1 = Queue()
print(q1.is_empty())
try:
    print(q1.get_front())
except IndexError as e:
    print(e.args[0])
q1.create_queue([10,20,30,40])
q1.enqueue(50)
try:
    print(q1.dequeue())
except IndexError as e:
    print(e.args[0])
try:
    print(q1.get_front())
except IndexError as e:
    print(e.args[0])
try:
    print(q1.get_rear())
except IndexError as e:
    print(e.args[0])
print(q1.size())