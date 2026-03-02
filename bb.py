class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # ---------------- Traversals ----------------

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end=" ")
        if self.right:
            self.right.inorder()

    def preorder(self):
        print(self.data, end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data, end=" ")

    # ---------------- Count Nodes ----------------

    def count_node(self):
        left = self.left.count_node() if self.left else 0
        right = self.right.count_node() if self.right else 0
        return 1 + left + right

    # ---------------- Sum Nodes ----------------

    def sum_nodes(self):
        left = self.left.sum_nodes() if self.left else 0
        right = self.right.sum_nodes() if self.right else 0
        return self.data + left + right

    # ---------------- Height ----------------

    def height(self):
        left = self.left.height() if self.left else 0
        right = self.right.height() if self.right else 0
        return 1 + max(left, right)

    # ---------------- Leaf Count ----------------

    def count_leaf_nodes(self):
        if self.left is None and self.right is None:
            return 1
        left = self.left.count_leaf_nodes() if self.left else 0
        right = self.right.count_leaf_nodes() if self.right else 0
        return left + right

    # ---------------- Max Node ----------------

    def max_node(self):
        left = self.left.max_node() if self.left else float('-inf')
        right = self.right.max_node() if self.right else float('-inf')
        return max(self.data, left, right)

    # ---------------- Balanced Check ----------------

    def is_balanced(self):
        def check(node):
            if node is None:
                return 0, True
            
            left_h, left_bal = check(node.left)
            right_h, right_bal = check(node.right)

            height = 1 + max(left_h, right_h)
            balanced = abs(left_h - right_h) <= 1 and left_bal and right_bal
            return height, balanced

        return check(self)[1]


# ---------------- Tree Creation ----------------

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# ---------------- Output ----------------

print("Inorder:")
root.inorder()

print("\nPreorder:")
root.preorder()

print("\nPostorder:")
root.postorder()

print("\nTotal Nodes:", root.count_node())
print("Sum of Nodes:", root.sum_nodes())
print("Height:", root.height())
print("Leaf Nodes:", root.count_leaf_nodes())
print("Max Value:", root.max_node())
print("Balanced?:", root.is_balanced())