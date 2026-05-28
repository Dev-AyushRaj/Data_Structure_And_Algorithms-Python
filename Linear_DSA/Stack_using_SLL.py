class Node:
    def __init__(self,items=None,next=None):
        self.items = items
        self.next = next

class Stack:
    def __init__(self):
        self.start = None
        self.item_count = 0
    
    def is_empty(self):
        if not self.start:
            return True
        return False

    def push(self,data):
        new_node = Node(data,self.start)
        self.start = new_node
        self.item_count += 1
    
    def create_stack(self,data):
        if not data:
            return
        
        for val in data:
            self.push(val)
    
    def pop(self):
        if not self.start:
           raise IndexError("Stack is empty")
        data = self.start.items
        self.start = self.start.next
        self.item_count -= 1
        return data
        
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.start.items
    
    def size(self):
        print(f"No of element in stack is:{self.item_count}")

s1 = Stack()
s1.create_stack([40,30,20])
print(s1.peek())
s1.push(10)
s1.pop()
print(s1.peek())
s1.size()