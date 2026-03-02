class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None
        
    def count_node(self,node):
        if node is None:
            return 0
        return 1+self.count_node(node.left)+self.count_node(node.right)
    
    def height(self,node):
        if node is None:
            return 0
        return 1+max(self.height(node.left),self.height(node.right))
    
    def mirror(self,node):
        if node is None:
            return 
        self.mirror(node.left)
        self.mirror(node.right)
        
        self.left,self.right=self.right,self.left
    
    def display(self):
        print(self.data,end=" ")
        if self.left:
            self.left.display()
        if self.right:
            self.right.display()
        
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)

print(tree.count_node(tree.root))
print(tree.height(tree.root))
tree.root.mirror(tree.root)
tree.display()