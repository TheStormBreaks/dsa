class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1  # Height of the node


class AVLTree:
    def __init__(self):
        self.root = None

    # Get the height of a node
    def _height(self, node):
        return node.height if node else 0

    # Get the balance factor of a node
    def _get_balance(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    # Right rotate
    def _right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        # Return new root
        return y

    # Left rotate
    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        # Return new root
        return y

    # Insert a node
    def insert(self, root, data):
        if not root:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        else:
            return root  # Duplicate keys not allowed

        # Update height of this node
        root.height = 1 + max(self._height(root.left), self._height(root.right))

        # Get balance factor to check if the node is unbalanced
        balance = self._get_balance(root)

        # Balance the node using rotations
        # Case 1: Left Left
        if balance > 1 and data < root.left.data:
            return self._right_rotate(root)

        # Case 2: Right Right
        if balance < -1 and data > root.right.data:
            return self._left_rotate(root)

        # Case 3: Left Right
        if balance > 1 and data > root.left.data:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)

        # Case 4: Right Left
        if balance < -1 and data < root.right.data:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    # In-order traversal
    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.data, end=" ")
            self.in_order(root.right)

# Example usage
if __name__ == "__main__":
    elements = ["Z", "I", "J", "F", "A", "E", "C", "P", "B", "D", "H", "N"]
    elements.sort()  # Sort elements in ascending order

    avl = AVLTree()
    root = None

    # Insert elements into the AVL tree
    for element in elements:
        root = avl.insert(root, element)

    print("In-order traversal of the AVL tree:")
    avl.in_order(root)
