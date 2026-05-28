class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item = item
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        return self.front == None
    
    def Create_DLL(self,data):
        if not data:
            return 
        self.front = Node(data[0])
        current = self.front
        for val in data[1:]:
            new_node = Node(val)
            new_node.prev = current
            current.next = new_node
            current = current.next
        self.rear = current

    def show_list(self):
        if not self.front:
            print("List is empty")
            return
        
        current = self.front
        while current:
            print(current.item, end="<->")
            current = current.next
        print("None")


    def insert_at_first(self,value):
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
            return
        new_node.next = self.front
        self.front.prev = new_node
        self.front = new_node
        return
    
    def insert_at_last(self,value):
        new_node = Node(value)
        if self.is_empty():
            self.front= new_node
            self.rear = new_node
            return
        new_node.prev = self.rear
        self.rear.next = new_node
        self.rear = new_node

    def search(self,data):
        current = self.front
        node_no = 0
        while current:
            if current.item==data:
                print(f"{data} found at Node no:{node_no}")
                return
            current = current.next
            node_no += 1
        print("Node not found")
    
    def insert_after(self,node_val,data):
        current = self.front
        while current:
            if current.item == node_val:
                new_node = Node(data)
                new_node.prev = current
                new_node.next = current.next
                if current.next:
                    current.next.prev = new_node
                else:
                    self.rear = new_node
                current.next = new_node
            current = current.next


    def delete_first(self):
        if not self.front:
            return
        
        if not self.front.next:
            self.front = None
            return
        self.front.next.prev = None
        self.front = self.front.next

    def delete_last(self):
        if not self.front:
            return
        
        if  not self.rear.prev:
            self.rear = None
            self.front = None
            return
        self.rear.prev.next = None
        self.rear = self.rear.prev
    
    def delete_item(self,node_val):
        if not self.front:
            return 
        current = self.front
        while current:
            if current.item == node_val:
                if current.prev == None:
                    self.front = current.next
                    if self.front:
                        self.front.prev = None
                    else:
                        self.rear = None
                        return
                    
                if current.next == None:
                    self.rear = current.prev
                    self.rear.next = None
                    return
                current.next.prev = current.prev
                current.prev.next = current.next
            current = current.next

    def __iter__(self):
        return DLLiterator(self.front)
    
class DLLiterator:
    def __init__(self,start):
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        
        data = self.current.item
        self.current = self.current.next
        return data


# l1 = DLL()
# l1.Create_DLL([10,20,20,40,50,60,70])
# l1.insert_at_first(5)
# l1.insert_at_last(80)
# l1.insert_after(50,55)
# l1.delete_first()
# l1.delete_last()
# l1.delete_item(55)
# l1.show_list()
# l1.search(50)
# for val in l1:
#     print(val,end=" ")                     
        
