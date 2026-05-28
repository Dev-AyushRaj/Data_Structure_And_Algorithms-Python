# Implementation of Priority queue using Singly linked list concept
class Node:
    def __init__(self,items=None,priority=None,next=None):
        self.items = items
        self.priority=priority
        self.next = next

class Priority_queue:
    def __init__(self):
        self.start = None
        self.item_count = 0

    def is_empty(self):
        return self.start == None
    
    def create_priority_queue(self,data):
        if not data:
            return
        for val in data:
            self.push(val[0],val[1])

    def push(self,value,priority):
        new_node = Node(value,priority)
        self.item_count += 1
        if self.start == None or self.start.priority > new_node.priority:
            new_node.next = self.start
            self.start = new_node
            return
        current = self.start
        while current.next and current.next.priority <= new_node.priority:
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Priority queue Underflow")
        else:
            data = (self.start.items,self.start.priority)
            self.start = self.start.next
            self.item_count -= 1
            return data
        
    def size(self):
        return self.item_count
    
    def peek(self):
        return (self.start.items,self.start.priority)
    
    def show_priority_queue(self):
        current = self.start
        while current:
            print((current.items,current.priority),end="->")
            current = current.next
        print("None")
        return
    
pq = Priority_queue()
pq.create_priority_queue([("A",7),("F",9),("C",4)])
pq.push("B",2)
pq.push("Z",2)
pq.push("H",9)
pq.push("Y",9)
try:
    print(pq.pop())
except IndexError as e:
    print(e.args[0])
print(pq.peek())
pq.show_priority_queue()
print(f"Number of element in Priority Queue:{pq.size()}")