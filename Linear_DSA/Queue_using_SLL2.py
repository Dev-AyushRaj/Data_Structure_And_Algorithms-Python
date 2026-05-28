# Implement Queue using Singly linked list
from Singly_linked_list2 import*

class Queue:
    def __init__(self):

        self.items = SLL()
        self.item_count = 0

    def is_empty(self):
        return self.items.is_empty()
    
    def enqueue(self,value):
        self.items.insert_at_last(value)
        self.item_count += 1

    def create_queue(self,data):
        if not data:
            return
        for val in data:
            self.enqueue(val)

    def dequeue(self):
        if not self.is_empty():
            self.items.delete_first()
            self.item_count -= 1
        else:
            raise IndexError("Queue underflow")
        
    def get_front(self):
        if not self.is_empty():
            return self.items.start.data
        else:
            raise IndexError("Queue underflow")
        
    def get_rear(self):
        if not self.is_empty():
            return self.items.last.data
        else:
            raise IndexError("Queue underflow")

    def size(self):
        return self.item_count
    

q1 = Queue()
q1.create_queue([10,20,30,40])
q1.enqueue(50)
print(q1.is_empty())
q1.dequeue()
print(q1.get_front())
print(q1.get_rear())
print(f"Number of element in Queue is:{q1.size()}")
    