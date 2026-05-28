from Singly_linked_list import *

class Stack:
    def __init__(self):
        self.stack = SLL()

    def is_empty(self):
        return self.stack.is_empty()
    
    def push(self,value):
        return self.stack.insert_at_start(value)
    
    def create_stack(self,data):
        if not data:
            return
        
        for val in data:
            self.stack.insert_at_start(val)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow") 
        return self.stack.delete_first()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        return self.stack.start.data
    
    def size(self):
        item_count = 0
        current = self.stack.start
        while current:
            item_count += 1
            current = current.next
        return(f"Number of element in stack is:{item_count}")

s1 = Stack()
s1.create_stack([40,30,20])
s1.push(10)
print(s1.is_empty())
s1.pop()
print(s1.peek())
print(s1.size())