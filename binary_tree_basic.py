class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
    def inorder(self):
        if Node is None:
           return
        if self.left:
            self.left.inorder()
        print(self.data, end=" ")
        if self.right:
            self.right.inorder()
    
    def preorder(self):
        if Node is None:
            return 
        print(self.data,end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    
    def postorder(self):
        if Node is None:
            return 
        if self.left :
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data,end=" ")
        
        
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.right.left=Node(6)
root.left.left=Node(4)
root.left.right=Node(5)
root.inorder()
print()
root.preorder()
print()
root.postorder()