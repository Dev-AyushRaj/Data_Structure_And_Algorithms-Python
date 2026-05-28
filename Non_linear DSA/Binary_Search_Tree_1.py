class Node:
    def __init__(self, item =None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return
        current = self.root
        while True:
            if new_node.item > current.item:
                if current.right == None:
                    current.right = new_node
                    return
                current = current.right
            
            if new_node.item < current.item:
                if current.left == None:
                    current.left = new_node
                    return
                current = current.left




    #define a search method to find the given item in binary search and return the node reference, return None if search failed

    def search(self,value):
        if not self.root:
            return None
        current = self.root
        while current:
            if current.item == value:
                return current
            if value > current.item:
                current = current.right
            else:
                current = current.left 
        return None
    
    def inorder(self, node=None):
        if node is None:
            node = self.root

        if node is None:
            return 
        
        if node.left:
            self.inorder(node.left)

        print(node.item, end=" ")

        if node.right:
            self.inorder(node.right)

    def preorder(self, node= None):
        if node is None:
            node = self.root

        if node is None:
            return
        
        print(node.item, end=" ")
        if node.left:
            self.preorder(node.left)

        if node.right:
            self.preorder(node.right)

    def postorder(self, node= None):
        if node is None:
            node = self.root

        if node is None:
            return
        
        if node.left:
            self.postorder(node.left)

        if node.right:
            self.postorder(node.right)
        print(node.item, end=" ")

 #Define a method to find the minimum value in BST

    def min_value(self):
        if not self.root:
            return
        current = self.root
        while current.left:
            current = current.left
        return current.item
    
    def max_value(self):
        if not self.root:
            return
        current = self.root
        while current.right:
            current = current.right
        return current.item
    
    def deletion(self,node_val):
        current = self.root
        par_ptr = None
        while current:
            if current.item == node_val:

                if current.left is None and current.right is None:
                    if current == self.root:
                        self.root = None
                        return
                    elif par_ptr.right == current:
                        par_ptr.right = None
                        return
                    else:
                        par_ptr.left = None
                        return
                
                
                if (current.left is not None)^(current.right is not None):
                    child = current.left or current.right
                    if current == self.root:
                        self.root = child
                        return
                    
                    elif par_ptr.right == current:
                           par_ptr.right = child
                           return
                    else:
                           par_ptr.left = child
                           return
                        
                        
                if current.left and current.right:
                    parent = current
                    predessor = parent.left
                    while predessor.right:
                        parent = predessor
                        predessor = predessor.right
                    if predessor.left:
                        parent.right = predessor.left
                    else:
                        parent.right = None
                    current.item = predessor.item
                    return
                
                
                
            par_ptr = current 
            if node_val > current.item:
                current = current.right
            else:
                current = current.left 
        return 


bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(80)
bst.insert(10)
bst.insert(40)
bst.insert(70)
bst.insert(100)
bst.insert(60)
bst.insert(55)
bst.insert(90)
bst.deletion(10)
bst.deletion(40)
bst.deletion(80)
print(bst.search(10))
print(bst.search(40))
print(bst.search(80))
bst.inorder()
print()
bst.preorder()
print()
bst.postorder()
print()
print(bst.min_value())
print(bst.max_value())