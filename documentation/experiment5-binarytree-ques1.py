import random

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class FullBinaryTree:
    def __init__(self):
        self.root = None

    # Construct a full binary tree with random values
    def construct_full_binary_tree(self, n=10, min_value=1, max_value=100):
        """Constructs a full binary tree with n nodes."""
        if n <= 0:
            return
        values = [random.randint(min_value, max_value) for _ in range(n)]
        self.root = self._construct_tree(values, 0)

    def _construct_tree(self, values, index):
        """Helper function to recursively construct a full binary tree."""
        if index < len(values):
            node = Node(values[index])
            node.left = self._construct_tree(values, 2 * index + 1)
            node.right = self._construct_tree(values, 2 * index + 2)
            return node
        return None

    # Find the minimum value in the tree
    def find_min(self, node):
        if not node:
            return float('inf')
        return min(node.data, self.find_min(node.left), self.find_min(node.right))

    # Find the maximum value in the tree
    def find_max(self, node):
        if not node:
            return float('-inf')
        return max(node.data, self.find_max(node.left), self.find_max(node.right))

    # Calculate the sum of all elements in the tree
    def calculate_sum(self, node):
        if not node:
            return 0
        return node.data + self.calculate_sum(node.left) + self.calculate_sum(node.right)

    # Pre-order Traversal: Root -> Left -> Right
    def pre_order_traversal(self, node):
        stack = []
        current = node
        while stack or current:
            if current:
                print(current.data, end=" ")
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right

    # Post-order Traversal: Left -> Right -> Root
    def post_order_traversal(self, node):
        stack1 = []
        stack2 = []
        if node:
            stack1.append(node)
        while stack1:
            current = stack1.pop()
            stack2.append(current)
            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)
        while stack2:
            print(stack2.pop().data, end=" ")

    # In-order Traversal: Left -> Root -> Right
    def in_order_traversal(self, node):
        stack = []
        current = node
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                print(current.data, end=" ")
                current = current.right

# Example Usage
if __name__ == "__main__":
    # Create a FullBinaryTree instance
    fbt = FullBinaryTree()

    # Construct the tree with random values
    fbt.construct_full_binary_tree()

    # Perform operations
    print("In-order Traversal:")
    fbt.in_order_traversal(fbt.root)
    print("\nPre-order Traversal:")
    fbt.pre_order_traversal(fbt.root)
    print("\nPost-order Traversal:")
    fbt.post_order_traversal(fbt.root)
    print("\nMinimum Value:", fbt.find_min(fbt.root))
    print("Maximum Value:", fbt.find_max(fbt.root))
    print("Sum of All Values:", fbt.calculate_sum(fbt.root))
