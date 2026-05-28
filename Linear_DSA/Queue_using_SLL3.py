# Queue inheriting Single linked list
from Singly_linked_list2 import *

class Queue(SLL):
    def __init__(self):
        super().__init__()
        self.item_count = 0

    def is_empty(self):
        return super().is_empty()
    
    def enqueue(self,value):
        self.insert_at_last(value)
        self.item_count += 1

    def create_queue(self,data):
        if not data:
            return
        for val in data:
            self.enqueue(val)

    def dequeue(self):
        if not self.is_empty():
            self.delete_first()
            self.item_count -= 1
        else:
            raise IndexError("Queue underflow")
    
    def get_front(self):
        if not self.is_empty():
            return self.start.data
        else:
            raise IndexError("Queue underflow")
        
    def get_rear(self):
        if not self.is_empty():
            return self.last.data
        else:
            raise IndexError("Queue underflow")
        
    def size(self):
        return self.item_count
    
    def insert_at_start(self, data):
        raise AttributeError("No attribute insert_at_start in class Queue")
    
    def insert_after(self, data):
        raise AttributeError("No attribute insert_after in class Queue")
    
    def delete_last(self, data):
        raise AttributeError("No attribute delete_last in class Queue")
    
    def delete_item(self, data):
        raise AttributeError("No attribute delete_item in class Queue")
    
    def __iter__(self, data):
        raise AttributeError("Iteration not allowed in Queue class")
    
q1 = Queue()
q1.create_queue([10,20,30,40])
q1.enqueue(50)
print(q1.is_empty())
q1.dequeue()
print(q1.get_front())
print(q1.get_rear())
print(q1.size())
