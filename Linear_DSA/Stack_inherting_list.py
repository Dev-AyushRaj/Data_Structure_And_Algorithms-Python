class Stack(list):
    def is_empty(self):
        return len(self)==0
    
    def create_stack(self,data):
        if not data:
            return
        
        for values in data:
            self.append(values)

    def push(self,item):
        return self.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return super().pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty") 
        return (f"Element at peek is:{self[-1]}")   
    
    def stack_size(self):
        return (f"No of element in stack is:{len(self)}")
    
    def insert(self, index, object):
        raise AttributeError("No attribute insert in Stack")
    
s1 = Stack()
s1.create_stack([10,20,30])
s1.push(40)
print(s1.pop())
print(s1.peek())
print(s1.stack_size())
s1.insert(2,0)
