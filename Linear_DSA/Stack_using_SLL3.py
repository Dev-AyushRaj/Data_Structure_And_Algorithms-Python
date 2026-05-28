from singly_linked_list import*

class Stack(SLL):
    def is_empty(self):
        return super().is_empty()
    
    def create_stack(self,data):
        if not data:
            return
        
        for val in data:
            self.insert_at_start(val)
    
    def push(self,value):
        self.insert_at_start(value)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        return self.delete_first()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        return self.start.data
    
    def size(self):
        item_count = 0
        current = self.start
        while current:
            item_count += 1
            current = current.next
        return(f"Number of item in stack is:{item_count}")
    
    def insert_at_last(self, data):
        raise AttributeError("No attribute insert_at_last in Stack")
    
    def insert_after(self, node, value):
        raise AttributeError("No attribute inser_after in Stack ")
    
    def delete_last(self):
        raise AttributeError("No attribute delete_last in Stack")
    
    def delete_item(self, item):
        raise AttributeError("No attribute delete_item in Stack")

s1 = Stack()
s1.create_stack([40,30,20])
s1.push(10)
print(s1.is_empty())
s1.pop()
print(s1.peek())
print(s1.size())
s1.delete_item(5)