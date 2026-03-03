from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # -------- Traversals --------

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

    # -------- Basic Utilities --------

    def count_nodes(self):
        left = self.left.count_nodes() if self.left else 0
        right = self.right.count_nodes() if self.right else 0
        return 1 + left + right

    def sum_nodes(self):
        left = self.left.sum_nodes() if self.left else 0
        right = self.right.sum_nodes() if self.right else 0
        return self.data + left + right

    def height(self):
        left = self.left.height() if self.left else 0
        right = self.right.height() if self.right else 0
        return 1 + max(left, right)

    def count_leaf_nodes(self):
        if self.left is None and self.right is None:
            return 1
        left = self.left.count_leaf_nodes() if self.left else 0
        right = self.right.count_leaf_nodes() if self.right else 0
        return left + right

    def max_node(self):
        left = self.left.max_node() if self.left else float('-inf')
        right = self.right.max_node() if self.right else float('-inf')
        return max(self.data, left, right)

    def mirror(self):
        self.left, self.right = self.right, self.left
        if self.left:
            self.left.mirror()
        if self.right:
            self.right.mirror()

    # -------- Level Order Based --------

    def left_view(self):
        result = []
        queue = deque([self])

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == 0:
                    result.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

    def right_view(self):
        result = []
        queue = deque([self])

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == size - 1:
                    result.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

    def zigzag_traversal(self):
        result = []
        queue = deque([self])
        left_to_right = True

        while queue:
            size = len(queue)
            level = []

            for _ in range(size):
                node = queue.popleft()
                level.append(node.data)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if not left_to_right:
                level.reverse()

            result.extend(level)
            left_to_right = not left_to_right

        return result

    def reverse_level_order(self):
        queue = deque([self])
        stack = []

        while queue:
            node = queue.popleft()
            stack.append(node.data)

            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        return stack[::-1]

    # -------- Diameter & Longest Path --------

    def diameter(self):
        def helper(node):
            if node is None:
                return 0, 0  # height, diameter

            lh, ld = helper(node.left)
            rh, rd = helper(node.right)

            height = 1 + max(lh, rh)
            dia = max(lh + rh + 1, ld, rd)

            return height, dia

        return helper(self)[1]

    def longest_path(self):
        path = []
        
        def dfs(node,current):
            nonlocal path
            if not node:
                return 
            current.append(node.data)
            if not node.left and not node.right:
                if len(current)>len(path):
                    path=current[:]
            
            dfs(node.left,current)
            dfs(node.right,current)
            current.pop()
        
        dfs(self,[])
        return path
           
    def max_width(self):

        queue = deque([self])
        max_w = 0

        while queue:
            max_w = max(max_w, len(queue))

            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return max_w
    
    def top_view(self):

        hd_map = {}
        queue = deque([(self, 0)])

        while queue:
            node, hd = queue.popleft()

            if hd not in hd_map:
                hd_map[hd] = node.data

            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))

        return [hd_map[x] for x in sorted(hd_map)]
    
    def boundary_traversal(self):

        result = [self.data]

        def left_boundary(node):
            while node:
                if node.left or node.right:
                    result.append(node.data)
                node = node.left if node.left else node.right

        def leaves(node):
            if not node:
                return
            if not node.left and not node.right:
                result.append(node.data)
            leaves(node.left)
            leaves(node.right)

        def right_boundary(node):
            stack = []
            while node:
                if node.left or node.right:
                    stack.append(node.data)
                node = node.right if node.right else node.left
            while stack:
                result.append(stack.pop())

        left_boundary(self.left)
        leaves(self.left)
        leaves(self.right)
        right_boundary(self.right)

        return result
    
    @staticmethod
    def build_from_in_post(inorder, postorder):
        if not inorder:
            return None

        root_val = postorder.pop()
        root = Node(root_val)

        idx = inorder.index(root_val)

        root.right = Node.build_from_in_post(inorder[idx+1:], postorder)
        root.left = Node.build_from_in_post(inorder[:idx], postorder)

        return root
    
    @staticmethod
    def build_from_in_pre(inorder, preorder):
        if not inorder:
            return None

        root_val = preorder.pop(0)
        root = Node(root_val)

        idx = inorder.index(root_val)

        root.left = Node.build_from_in_pre(inorder[:idx], preorder)
        root.right = Node.build_from_in_pre(inorder[idx+1:], preorder)

        return root
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

print("Inorder:")
root.inorder()
print("\nPreorder:")
root.preorder()
print("\nPostorder:")
root.postorder()
print("\nCount Nodes:", root.count_nodes())
print("Sum Nodes:", root.sum_nodes())
print("Height:", root.height())
print("Leaf Nodes:", root.count_leaf_nodes())
print("Left View:", root.left_view())
print("Right View:", root.right_view())
print("Count Nodes:", root.count_nodes())
print("Sum Nodes:", root.sum_nodes())
print("Height:", root.height())
print("Leaf Nodes:", root.count_leaf_nodes())
print("Max Value:", root.max_node())
print("Zigzag:", root.zigzag_traversal())
print("Reverse Level Order:", root.reverse_level_order())
print("Diameter:", root.diameter())
print("Longest Path:", root.longest_path())