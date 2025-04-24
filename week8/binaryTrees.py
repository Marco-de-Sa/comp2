class TreeNode:
    def __init__(self, value, left = None, right = None):
        # Left and Right are optional parameters
        # If they are not specified, their value is None
        self.value = value
        self.left = left
        self.right = right

    def add_left(self, left): # Left needs to be a TreeNode
        if isinstance(left, TreeNode): # True if left is a TreeNode
            self.left = left

    def add_right(self, right): # Right needs to be a TreeNode
        self.right = right

    def traversal(self):
        # Traverse the left subtree if it exists
        if self.left is not None:
            self.left.traversal()
        # Print the current value
        print(self.value)
        # Traverse the right subtree if it exists
        if self.right is not None:
            self.right.traversal()

    def height(self):
        # Base case
        if self.left is None and self.right is None:
            # We are at a leaf
            return 1
        # Recursive case 1: There is only a left subtree
        elif self.left is not None and self.right is None:
            return self.left.height() + 1
        # Recursive case 2: There is only a right subtree
        elif self.left is None and self.right is not None:
            return self.right.height() + 1
        # Last Recursive case: there is both
        else:
            return max(self.left.height(), self.right.height()) + 1

# Nodes
node_5 = TreeNode(5)
node_3 = TreeNode(3)
node_8 = TreeNode(8)
node_1 = TreeNode(1)
node_6 = TreeNode(6)
node_9 = TreeNode(9)

# Connections (remember we use the nodes because they are TreeNode)
node_5.add_left(node_3)
node_5.add_right(node_8)
node_3.add_left(node_1)
node_8.add_left(node_6)
node_8.add_right(node_9)


node_5.traversal()
print(node_5.height())