class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class SLL():
    def __init__(self):
        self.start = None
        self.last = None

    def is_empty(self):
        if self.start is None:
            return True
        return False
            
    def create_list(self,value):
        if not value:
            return
        new_node = Node(value[0])
        self.start = new_node

        current = self.start
        for val in value[1:]:
            new_node = Node(val)
            current.next = new_node
            current = new_node
        self.last = current

        
    def insert_at_start(self,data):
        new_node = Node(data)
        if not self.start:
            self.start = new_node
            return
        
        new_node.next = self.start
        self.start = new_node
    
    def insert_at_last(self,data):
        new_node = Node(data)
        if not self.start:
            self.start = new_node
            self.last = new_node
            return
        
        self.last.next = new_node
        self.last = new_node
        # current = self.start
        # while current.next:
        #     current = current.next
        # current.next = new_node
        # self.last =new_node
   
    def search(self,value):
        node_no = 1
        current = self.start
        while current:
            if(current.data == value):
                print(f"Node number {node_no} have the value {value}")
                return node_no
            node_no += 1      
            current = current.next
        print("Node not found")
        return -1

    def insert_after(self,node,value):
        current = self.start
        while current:
            if(current.data == node):
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print("Node not found")


    def delete_first(self):
        if self.start is None:
            print("List is empty")
        
        self.start = self.start.next


    def delete_last(self):
        if self.start is None:
            print("List is empty")

        if self.start.next is None:
            self.start = None
            return
        
        current = self.start
        while current.next.next:
            current = current.next
        current.next = None
        self.last = current

    def delete_item(self,item):
        if self.start is None:
            return
        
        if self.start.data == item:
            self.start = self.start.next
            return
        
        current = self.start
        while current.next:
            if current.next.data == item:
                current.next = current.next.next
                return
            current = current.next
  
    def show_list(self):
        current = self.start
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")
    
    def __iter__(self):
        return Slliterator(self.start)

# Making sll class iterable 

class Slliterator:
    def __init__(self,start):
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data


# sll =SLL()
# sll.create_list([20,30,40,50,60,70])
# sll.is_empty()
# sll.insert_at_start(10)
# sll.insert_at_last(80)
# sll.insert_after(50,55)
# sll.delete_last()
# sll.delete_item(55)
# sll.show_list()
# sll.search(50)
# for value in sll:
#     print(value,end=" ")