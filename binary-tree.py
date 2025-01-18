class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # Insert data into the binary tree
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

    # In-order Traversal: Left -> Root -> Right
    def in_order(self, node):
        if node is not None:
            self.in_order(node.left)
            print(node.data, end=" ")
            self.in_order(node.right)

    # Pre-order Traversal: Root -> Left -> Right
    def pre_order(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    # Post-order Traversal: Left -> Right -> Root
    def post_order(self, node):
        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.data, end=" ")

    # Level-order Traversal: Level by Level
    def level_order(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print(current.data, end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    # Branch-wise Traversal: List nodes from root to leaves
    def branch_order(self, node, path=[]):
        if node is not None:
            path.append(node.data)  # Add current node to path
            if not node.left and not node.right:
                print(" -> ".join(map(str, path)))  # Print the branch
            else:
                self.branch_order(node.left, path[:])  # Traverse left
                self.branch_order(node.right, path[:])  # Traverse right

# Example usage:
bt = BinaryTree()
bt.insert(10)
bt.insert(8)
bt.insert(4)
bt.insert(9)
bt.insert(21)
bt.insert(19)
bt.insert(11)
bt.insert(20)
bt.insert(31)
bt.insert(28)




print("In-order Traversal:")
bt.in_order(bt.root)
print("\nPre-order Traversal:")
bt.pre_order(bt.root)
print("\nPost-order Traversal:")
bt.post_order(bt.root)
print("\nLevel-order Traversal:")
bt.level_order()
print("\nBranch-wise Traversal:")
bt.branch_order(bt.root)
