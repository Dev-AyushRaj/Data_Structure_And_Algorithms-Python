# Programme to creat linked list
class Node:
    def __init__(self,Data):
        self.data = Data
        self.next = None

# Creating nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

#Connecting nodes to form linked list
node1.next = node2
node2.next = node3
node3.next = node4

#Printing the linked list
connect = node1
while connect is not None:
    print(connect.data,end="->")
    connect = connect.next
print("None")