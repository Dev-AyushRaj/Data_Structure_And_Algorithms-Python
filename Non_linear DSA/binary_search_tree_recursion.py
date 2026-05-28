class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insertion(self,value):
        self.root = self.rinsert(self.root,value)

    def rinsert(self,root,value):
        if root is None:
            return Node(value)
            

        if value < root.item:
            root.left = self.rinsert(root.left,value)

        elif value > root.item:
            root.right = self.rinsert(root.right,value)

        return root

    #define a search method to find the given item in binary search and return the node reference, return None if search failed

    def search(self,value):
       return self.rsearch(self.root, value)
    
    def rsearch(self,root,value):
        if root is None or root.item == value:
            return root
        
        
        if value < root.item:
            return self.rsearch(root.left,value)
        
        elif value > root.item:
            return self.rsearch(root.right,value) 
           
     
    #Inorder Traversal(left->Root->right)
    def inorder(self,node= None):
        if node is None:
            node = self.root

        if node is None:
            return
        
        if node.left:
            self.inorder(node.left)

        print(node.item, end=" ")

        if node.right:
            self.inorder(node.right)

    #Preorder(root->left->right)
    def preorder(self,node=None):
        if node is None:
            node = self.root

        if node is None:
            return
        
        print(node.item, end= " ")
        if node.left:
            self.preorder(node.left)

        if node.right:
            self.preorder(node.right)


    #Postorder(Left->Right->Root)--- SIR VERSION----
    def postorder(self):
        list = []
        self.rpostorder(self.root,list)
        return list
    def rpostorder(self,root,list):
        if root:
            self.rpostorder(root.left,list)
            self.rpostorder(root.right,list)
            list.append(root.item)
        

    def min_val(self,node = None):
        if node is None:
            node = self.root
        if node is None:
            return
        if node.left:
            return self.min_val(node.left)
        return node.item
    
    def max_val(self,node = None):
        if node is None:
            node = self.root

        if node is None:
            return
        
        if node.right:
            return self.max_val(node.right)
        return node.item 
    
    def size(self):
        return self.rsize(self.root)
    def rsize(self,root):
        if root:
            return 1 + self.rsize(root.left) + self.rsize(root.right)
        else:
            return 0    
        

    def deletion(self,value):
       self.root = self.rdelete(self.root,value)
    
    def rdelete(self,root,value):
        if root is None:
            return root
        
        if root.item == value:
            if root.left is None and root.right is None:
                return None
            elif (root.left is None)^(root.right is None):
                child = root.left or root.right
                return child
            elif root.left and root.right:
                predecessor = root.left
                while predecessor.right:
                    predecessor = predecessor.right
                root.item = predecessor.item
                root.left = self.rdelete(root.left, predecessor.item)
                return root
        
        elif value > root.item:
           root.right = self.rdelete(root.right,value)

        else:
            root.left = self.rdelete(root.left,value)
        return root
        
                      
                
bst = BST()
bst.insertion(50)
bst.insertion(30)
bst.insertion(10)
bst.insertion(40)
bst.insertion(80)
bst.insertion(60)
bst.insertion(100)
bst.insertion(75)
bst.deletion(40)
bst.deletion(75)
print(bst.search(40))
bst.inorder()
print()
bst.preorder()
print()
print(bst.postorder())
print()
print(bst.min_val())
print(bst.max_val())
print(bst.size())