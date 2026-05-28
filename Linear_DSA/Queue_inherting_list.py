# Implemention of Queue inherting list
class Queue(list):
    def is_empty(self):
        return len(self) == 0
    
    def create_queue(self,data):
        if not data:
            return
        for val in data:
            self.append(val)

    def enqueue(self,value):
        self.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.pop(0)
        else:
            raise IndexError("Queue underflow")
        
    def get_front(self):
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError("Queue underflow")
        
    def get_rear(self):
        if not self.is_empty():
            return self[len(self)-1]
        else:
            raise IndexError("Queue underflow")
        
    def size(self):
        return len(self)
    
    def insert(self, index, object):
        raise AttributeError("No attribute insert in Queue class")
    
q1 = Queue()
q1.create_queue([10,20,30,40])
q1.enqueue(50)
q1.dequeue()
print(q1.is_empty())
print(q1.get_front())
print(q1.get_rear())
print(f"Number of element in Queue:{q1.size()}")