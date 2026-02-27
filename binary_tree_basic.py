class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
    def inorder(node):
        if node is None:
           return
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)
        
        
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.inorder()