class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.start = None
    
    def is_empty(self):
        if not self.start:
            print("List is empty")
            return True
        return False


    def Create_list(self,data):
        if not data:
            return
        self.start= Node(data[0])
        
        current = self.start
        for val in data[1:]:
            new_node = Node(val)
            current.next = new_node
            new_node.prev = current
            current = new_node

    def show_list(self):
        if not self.start:
            print("List is empty")
            return
        
        current = self.start
        while current:
            print(current.data, end="<->")
            current = current.next
        print("None")

    def insert_at_first(self,value):
        new_node = Node(value)
        if not self.start:
            self.start = new_node
            return
        
        self.start.prev = new_node
        new_node.next = self.start
        self.start = new_node

    def insert_at_last(self,value):
        new_node = Node(value)
        if not self.start:
            self.start = new_node
            return
        
        current = self.start
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current


    def search(self,value):
        if not self.start:
            return
        
        node_no = 1
        current = self.start
        while current:
            if current.data == value:
                print(f"{value} found at node no:{node_no}")
                return
            current = current.next
            node_no += 1
        print("Node not found")

    def insert_after(self,Node_val,value):
        new_node = Node(value)
        current = self.start
        while current:
            if current.data == Node_val:
                    new_node.next = current.next
                    new_node.prev = current
                    if current.next:
                        current.next.prev = new_node
                    current.next = new_node                    
                    return
            current = current.next

    def delete_first(self):
        if not self.start:
            return
        
        current = self.start
        if current.next is None:
            self.start = None
            return
        
        self.start = current.next
        current.next.prev = None

    def delete_last(self):
        if not self.start:
            return
        
        current = self.start
        if not current.next:
            self.start = None
            return
        
        while current.next.next:
            current= current.next
        current.next = None

    def delete_item(self,value):
        if not self.start:
            return
        
        current = self.start
        while current:
            if current.data == value:
                if current.prev is None:
                    self.start = current.next
                    current.next.prev = None
                    return
            
                current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next
    
    def __iter__(self):
        return DLLIterator(self.start)
    
class DLLIterator:
    def __init__(self, start):
        self.current = start
            
    def __iter__(self):
        return self
        
    def __next__(self):
        if not self.current:
            raise StopIteration
        
        data = self.current.data
        self.current = self.current.next
        return data
        

l1 = DLL()
l1.Create_list([10,20,20,40,50,60,70])
l1.insert_at_first(5)
l1.insert_at_last(80)
l1.insert_after(50,55)
l1.delete_first()
l1.delete_last()
l1.delete_item(55)
l1.show_list()
l1.search(50)
for val in l1:
    print(val,end=" ")