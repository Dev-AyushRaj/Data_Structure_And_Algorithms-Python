# Implementing Deque inherting list
class Deque(list):
    def is_empty(self):
        return len(self)==0
    
    def creat_Deque(self,data):
        if not data:
            return
        for val in data:
            self.insert_rear(val)

    def insert_front(self,value):
        self.insert(0,value)

    def insert_rear(self,value):
        self.append(value)
    
    def delete_front(self):
        if not self.is_empty():
            return self.pop(0)
        else:
            raise IndexError("Deque Underflow")
        
    def delete_rear(self):
        if not self.is_empty():
            return self.pop()
        else:
            raise IndexError("Deque Underflow")
        
    def get_front(self):
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError("Deque Underflow")
        
    def get_rear(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Deque Underflow")
        
    def size(self):
        return len(self)
    
d1 = Deque()
d1.creat_Deque([20,30,40,50])
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
print(d1.get_rear())
print(f"Number of element in Deque is:{d1.size()}")

