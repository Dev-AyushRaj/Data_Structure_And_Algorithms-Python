class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SLL:
    def __init__(self):
        self.start =None

    def is_empty(self):
        if not self.start:
            print("list is empty")
            return True
        return False
        
    def creat_list(self,data):
        if not data:
            return
        self.start = Node(data[0])
        
        current = self.start
        for val in data[1:]:
            new_node = Node(val)
            current.next = new_node
            current = new_node

    def show_list(self):
        if not self.start:
            print("List is empty")
            return
        
        current = self.start
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

    def insert_at_start(self,data):
        new_node = Node(data)
        if not self.start:
            self.start  = new_node
            return

        new_node.next = self.start
        self.start = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.start:
            self.start = new_node
            return
        
        current = self.start
        while current.next:
            current = current.next
        current.next = new_node

    def search(self,data):
        if not self.start:
            return
        
        node_no = 1
        current = self.start
        while current:
            if current.data == data:
                print(f"{data} found at node no:{node_no}")
                return
            node_no += 1
            current = current.next
        print("Not Found")
    

    def insert_after(self,node_value,data):
        if not self.start:
            return
        
        current = self.start
        while current:
            if current.data == node_value:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print("Node not found")


    def delete_first(self):
        if not self.start:
            return
        else:
            self.start = self.start.next
        
    def delete_last(self):
        if not self.start:
            return
        
        if not self.start.next:
            self.start = None
            return

        current = self.start
        while current.next.next:
            current = current.next
        current.next = None
        
    def delete_item(self,data):
        if not self.start:
            return
        
        if self.start.data == data:
            self.start = self.start.next

        current = self.start
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        print("Node not found")


l1 = SLL()
l1.is_empty()
l1.creat_list([10,20,30,40,50,60,70])
l1.insert_at_start(5)
l1.insert_at_end(80)
l1.insert_after(50,55)
l1.delete_first()
l1.delete_last()
l1.delete_item(55)
l1.show_list()
l1.search(40)
