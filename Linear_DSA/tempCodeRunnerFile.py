def push(self,value,priority):
        new_node = Node(value,priority)
        self.item_count += 1
        if self.is_empty():
            self.start = new_node
            return
        if self.start.priority > new_node.priority:
            new_node.next = self.start
            self.start = new_node
            return
        current = self.start
        while current.next:
            if current.next.priority == new_node.priority:
                while current.next and current.next.priority == new_node.priority:
                    current = current.next
                break
                 
            if current.next.priority > new_node.priority:
                break
            current = current.next
        new_node.next = current.next
        current.next = new_node