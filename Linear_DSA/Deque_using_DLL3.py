# Implementing Deque inherting Doubly Linked list
from Doubly_linked_list2 import*
class Deque(DLL):
    def __init__(self):
        super().__init__()
        self.item_count = 0

    def is_empty(self):
        return super().is_empty()
    
    def create_Deque(self,data):
        if not data:
            return
        for val in data:
            self.insert_rear(val)
    
    def insert_front(self,value):
        self.insert_at_first(value)
        self.item_count += 1

    def insert_rear(self,value):
        self.insert_at_last(value)
        self.item_count += 1

    def delete_front(self):
        if not self.is_empty():
            self.delete_first()
            self.item_count -= 1
        else:
            raise IndexError("Deque Underflow")
        
    def delete_rear(self):
        if not self.is_empty():
            self.delete_last()
            self.item_count -= 1
        else:
            raise IndexError("Deque Underflow")
        
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("Deque Underflow")
        
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError("Deque Underflow")
        
    def size(self):
        return self.item_count
     
    def insert_after(self, node_val, data):
        raise AttributeError("No attribute insert_after in Deque class")
    
    def delete_item(self, node_val):
        raise AttributeError("No attribute delete_item in Deque class")
    
    def __iter__(self):
        raise AttributeError("No attribute iter in Deque class")
    

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
