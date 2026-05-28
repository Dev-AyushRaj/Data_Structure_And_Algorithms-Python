class Node:
    def __init__(self,item = None, next =None):
        self.item = item
        self.next = next

class CLL:
    def __init__(self):
        self.last = None
    
    def is_empty(self):
        if not self.last:
            print("List is empty")
            return True
        return False
    
        
    def create_list(self,data):
        if not data:
            return

        first_node = Node(data[0])
        self.last = first_node

        for val in data[1:]:
            new_node = Node(val)
            self.last.next = new_node
            self.last = new_node

        self.last.next = first_node



    def Show_list(self):
        if not self.last:
            print("list is empty")
            return

        current = self.last.next
        while True:
            print(current.item,end="->")
            current = current.next
            if current == self.last.next:
                print("Back to start")
                return
            
    def insert_at_first(self,data):
        new_node = Node(data)
        if not self.last:
            self.last = new_node
            self.last.next = new_node
            return
        
        new_node.next = self.last.next
        self.last.next = new_node

    def insert_at_last(self,data):
        new_node = Node(data)
        if not self.last:
            self.last = new_node
            self.last.next = new_node
            return

        new_node.next = self.last.next
        self.last.next = new_node
        self.last = new_node     

    def search(self,node_val):
        if not self.last:
            print("list is empty")
            return

        node_no = 1
        current = self.last.next
        while True:
            if current.item == node_val:
                print(f"{node_val} found at node no:{node_no}")
                return
            current = current.next
            node_no += 1

            if current == self.last.next:
                print("Node not found")
                return
            
    def insert_after(self,node_val,data):
        if not self.last:
            return

        current = self.last.next 
        while True:
            if current.item == node_val:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                if current == self.last:
                    self.last = new_node
                return
            current = current.next

            if current == self.last.next:
                print("Node not found for insert after")
                return
            
    def delete_first(self):
        if not self.last:
            return
        if self.last.next == self.last:
            self.last = None
            
        self.last.next = self.last.next.next
                
    def delete_last(self):
        if not self.last:
            return
        
        if self.last.next == self.last:
            self.last = None

        current = self.last.next
        while current.next != self.last:
            current = current.next
        current.next = self.last.next
        self.last = current

    def delete_item(self,node_val):
        if not self.last:
            return
        
        if self.last.next == self.last and self.last.item == node_val:
            self.last = None
            return
        

        current = self.last.next
        while True:
            if current.next.item == node_val:
                if current.next == self.last:
                    current.next = self.last.next
                    self.last = current
                    return
                current.next = current.next.next
                return
            
            current = current.next
            if current == self.last.next:
                print("Node not found for deletion")
                return
            
    def __iter__(self):
        return CLLiterator(self.last.next)
    

class CLLiterator:
    def __init__(self,start):
        self.current = start
        self.start = start
        self.count = 0
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current == None:
            raise StopIteration
        if self.current == self.start and self.count > 0:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        self.count += 1
        return data
    
  
cll = CLL()
cll.create_list([10,20,30,40,50,60,70])
cll.insert_at_first(0)
cll.insert_at_last(80)
cll.insert_after(80,90)
cll.delete_first()
cll.delete_last()
cll.delete_item(80)
cll.Show_list()
cll.search(50)
for val in cll:
    print(val,end=" ")
