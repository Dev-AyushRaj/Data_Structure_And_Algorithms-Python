class Node:
    def __init__(self,item = None, prev= None, next = None ):
        self.item = item
        self.prev = prev
        self.next = next


class CDLL:
    def __init__(self):
        self.start = None

    def is_empty(self):
        if not self.start:
            print("List is empty")
            return True
        return False
    
    def create_list(self,node_val):
        if not node_val:
            return

        self.start = Node(node_val[0])
        
        current = self.start
        for val in node_val[1:]:
            new_node = Node(val)
            new_node.prev= current
            current.next = new_node
            current = new_node
        current.next = self.start
        self.start.prev = current
            
    def show_list(self):
        if not self.start:
            print("List is empty")
            return
        
        current = self.start
        while True:
            print(current.item,end="<->")
            current = current.next
            if current==self.start:
                print("Back to start")
                return
                       
    def insert_at_first(self,node_val):
        new_node = Node(node_val)
        if not self.start:
            self.start = new_node
            new_node.prev = new_node
            new_node.next = new_node
            return
        
        new_node.prev = self.start.prev
        new_node.next = self.start
        self.start.prev.next = new_node
        self.start.prev= new_node
        self.start = new_node
        return
    
    def insert_at_last(self,node_val):
        new_node = Node(node_val)
        if not self.start:
            self.start = new_node
            new_node.prev = new_node
            new_node.next = new_node
            return
        
        new_node.prev = self.start.prev
        new_node.next = self.start
        self.start.prev.next = new_node
        self.start.prev = new_node
        return
    
    def search(self,node_val):
        if not self.start:
            print("List is empty")
            return
        
        node_no = 1
        current = self.start
        while True:
            if current.item == node_val:
                print(f"{node_val} found at node no:{node_no}")
                return
            node_no += 1
            current = current.next

            if current == self.start:
                print("Node not found")
                return
            
    def insert_after(self,node_val,data):
        if not self.start:
            return
        
        current = self.start
        while True:
            if current.item == node_val:
                new_node = Node(data)
                new_node.prev = current
                new_node.next = current.next
                current.next.prev = new_node
                current.next = new_node
                if current == self.start.prev:
                    self.start.prev = new_node
                    current.next = new_node
                return
                    
            current = current.next
            if current == self.start:
                print("Node not found for insert after")
                return
            
    def delete_first(self):
        if not self.start:
            return
        
        if self.start == self.start.prev:
            self.start = None
            return
        
        self.start.prev.next = self.start.next
        self.start.next.prev = self.start.prev
        self.start = self.start.next
        return
    
    def delete_last(self):
        if not self.start:
            return
        
        if self.start == self.start.prev:
            self.start = None
            return
        
        self.start.prev.prev.next = self.start
        self.start.prev = self.start.prev.prev
    
    def delete_item(self,node_val):
        if not self.start:
            return
        
        current = self.start
        if current.item == node_val and self.start == self.start.prev:
            self.start = None
            return
        

        while True:
            if current.item == node_val:
                current.prev.next = current.next
                current.next.prev = current.prev
                if current == self.start:
                    self.start  = self.start.next
                return
            current = current.next

            if current == self.start:
                print("Node not found for deletion")
                return
            
    def __iter__(self):
        return CDLLITERATOR(self.start)


class CDLLITERATOR:
    def __init__(self,start):
        self.current = start
        self.start = start
        self.count = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current == None:
            raise StopIteration
        
        if self.current == self.start and self.count>1:
            raise StopIteration
        
        data = self.current.item 
        self.current = self.current.next
        self.count += 1
        return data



cdll = CDLL()
cdll.create_list([10,20,30,40,50,60,70])
cdll.insert_at_first(0)
cdll.insert_at_last(80)
cdll.insert_after(50,55)
cdll.delete_first()
cdll.delete_last()
cdll.delete_item(55)
cdll.show_list()
cdll.search(50)
for val in cdll:
    print(val,end=" ")