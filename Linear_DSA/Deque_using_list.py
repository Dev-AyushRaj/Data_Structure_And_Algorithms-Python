# Implementing Deque using List
class Deque:
    def __init__(self):
        self.deque = []

    def is_empty(self):
        return len(self.deque)==0
    
    def create_deque(self,data):
        if not data:
            return
        for val in data:
            self.insert_rear(val)
    
    def insert_front(self,value):
        self.deque.insert(0,value)

    def insert_rear(self,value):
        self.deque.append(value)

    def delete_front(self):
        if not self.is_empty():
            return self.deque.pop(0)
        else:
            raise IndexError("Deque Underflow")
        
    def delete_rear(self):
        if not self.is_empty():
            return self.deque.pop()
        else:
            raise IndexError("Deque Underflow")
        
    def get_front(self):
        if not self.is_empty():
            return self.deque[0]
        else:
            raise IndexError("Deque Underflow")
        
    def get_rear(self):
        if not self.is_empty():
            return self.deque[-1]
        else:
            raise IndexError("Deque Underflow")
        
    def size(self):
        return len(self.deque)
    

d1 = Deque()
d1.create_deque([10,20,30,40])
d1.insert_front(5)
d1.insert_rear(50)
try:
    d1.delete_front()
except IndexError as e:
    print(e.args[0])
d1.delete_rear()
try:
    print(d1.get_front())
except IndexError as e:
    print(e.args[0])
print(d1.get_rear())
print(d1.size())