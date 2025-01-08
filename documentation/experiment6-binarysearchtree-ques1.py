class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert a new element
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert(current.left, data)
        else:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert(current.right, data)

    # Determine the height of the tree
    def height(self, node):
        if not node:
            return -1  # Height of an empty tree is -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    # Delete a node
    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if not node:
            return node
        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            # Node with one or no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            # Node with two children: Get inorder successor
            temp = self._min_value_node(node.right)
            node.data = temp.data
            node.right = self._delete(node.right, temp.data)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Check if the tree is balanced
    def is_balanced(self, node):
        if not node:
            return True
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        if abs(left_height - right_height) > 1:
            return False
        return self.is_balanced(node.left) and self.is_balanced(node.right)

    # In-order traversal (helper to visualize the tree)
    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.data, end=" ")
            self.in_order(node.right)


# Example usage
bst = BST()

# Construct BST with given values
values = [12, 35, 14, 97, 36, 65, 89]
for value in values:
    bst.insert(value)

# 1. Insert new element
roll_number_last_two_digits = 12  # Replace with your own roll number's last two digits
bst.insert(roll_number_last_two_digits)

# 2. Determine height
tree_height = bst.height(bst.root)
print(f"Height of the BST: {tree_height}")

# 3. Delete an element
bst.delete(14)  # Example: Deleting 14
print("In-order traversal after deletion:")
bst.in_order(bst.root)

# 4. Check if the tree is balanced
is_bal = bst.is_balanced(bst.root)
print(f"\nIs the BST balanced? {'Yes' if is_bal else 'No'}")
