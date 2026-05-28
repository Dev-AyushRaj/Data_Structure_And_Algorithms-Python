# Implementation of priority queue using list
class Priority_queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def create_priority_queue(self,data):
        if not data:
            return
        for val in data:
            self.push(val)

    def push(self,value):
        priority_no = value[1]
        for index, val in enumerate(self.items):
            if val[1] == priority_no:
                self.items.insert(index+1,value)
                return
            if val[1] > priority_no:
                self.items.insert(index,value)
                return
        self.items.append(value)

    def show_priority_queue(self):
        return self.items

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Priority queue Underflow")
        
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Priority queue Underflow")
        
    def size(self):
        return len(self.items)
        
pq = Priority_queue()
pq.create_priority_queue([("A",4),("B",3),("C",1)])
pq.push(("D",2))
pq.push(("E",2))
pq.push(("I",2))
pq.pop()
print(pq.peek())
print(pq.size())
print(pq.show_priority_queue())
    