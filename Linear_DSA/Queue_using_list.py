#Implementing Queue using list
class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items)==0
    
    def create_queue(self,data):
        if not data:
            return
        for val in data:
            self.enqueue(val)

    def enqueue(self,value):
        self.items.append(value)

    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("Queue underflow")
        
    def get_front(self):
        if not self.is_empty():
           return self.items[0]
        else:
            raise IndexError("Queue underflow")
        
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue underflow")
        
    def size(self):
        return len(self.items)

        
q1 = Queue()
try:
    print(q1.get_front())
except IndexError as e:
    print(e.args[0])
q1.create_queue([10,20,30,40])
print(q1.is_empty())
q1.enqueue(50)
try:
    q1.dequeue()
except IndexError as e:
    print(e.args[0])
print(q1.get_front())
print(q1.get_rear())
print(f"Number of items in queue is:{q1.size()}")