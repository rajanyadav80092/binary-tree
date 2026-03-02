from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def inorder(self):
        if Node is None:
            return ""
        if self.left:
            self.left.inorder()
        print(self.data,end=" ")
        if self.right:
            self.right.inorder()
    
    def preorder(self):
        if Node is None:
            return ""
        print(self.data,end=" ")
        if self.left:
            self.left.preorder()
        if self.right: 
            self.right.preorder()
    
    def postorder(self):
        if Node is None:
            return " "
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data,end=" ")
    
    def count_node(self):
        if Node is None:
            return " "
        left_count = self.left.count_node() if self.left else 0
        right_count = self.right.count_node() if self.right else 0
        return 1+left_count+right_count
    
    def sum_nodes(self):
        if root is None:
            return 0
        left_sum=self.left.count_node() if self.left else 0
        right_sum=self.right.count_node() if self.right else 0
        return root.data + left_sum+right_sum
    
    
    def is_balanced(self):
        def check(node):
            if node is None:
                return 0, True

            left_height, is_left_bal = check(node.left)
            right_height, is_right_bal = check(node.right)

            height = 1 + max(left_height, right_height)

            is_bal = (
                is_left_bal and
                is_right_bal and
                abs(left_height - right_height) <= 1
            )

            return height, is_bal

        return check(self)[1]
    
    # def max_node(self):
    #     if Node is None:
    #         return float('-inf')
    #     return max(self.data, root.left.max_node(),root.right.max_node())
    
    def max_node(self):

        left_max = self.left.max_node() if self.left else float('-inf')
        right_max = self.right.max_node() if self.right else float('-inf')

        return max(self.data, left_max, right_max)
    
    def count_leaf_nodes(self):
        if Node is None:
            return 0
    
        if self.left is None and self.right is None:
            return 1
        return self.left.count_leaf_nodes() + self.right.count_leaf_nodes()
    
    def height(self):
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0

        return 1 + max(left_height, right_height)
    
    def mirror(self):
        if self is None:
            return
        
        self.left, self.right = self.right, self.left

        if self.left:
            self.left.mirror()
        if self.right:
            self.right.mirror()
    
    
    def left_view(self, root):
        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                # First node of level
                if i == 0:
                    result.append(node.data)

                if self.node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

    
    
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.inorder()
print()
root.preorder()
print()
root.postorder()
print()
print(root.count_node())
print()
print(root.sum_nodes())
print("Height:", root.height())
print("Leaf Nodes:", root.count_leaf_nodes())
print("Max Value:", root.max_node())
print("Balanced?:", root.is_balanced())
print()
root.left_view(1)