class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items)==0:
            print("List is empty")
            return True
        return False
    
    def create_stack(self,values):
        if not values:
            return
        
        for val in values:
            self.items.append(val)

    def push(self,value):
        self.items.append(value)
        return
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    

    def peek(self):
        if not self.items:
            return
        print(f"Element at peek is:{self.items[-1]}")

    def stack_size(self):
        if not self.items:
            return
        print(f"Number of item in stack is:{len(self.items)}")

sl = Stack()
sl.is_empty()
sl.create_stack([50,40,30,20])
sl.push(10)
print(sl.pop())
sl.peek()
sl.stack_size()