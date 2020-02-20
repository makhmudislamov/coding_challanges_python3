"""
Given a Tree class, create a method called add that accepts a Node, and inserts it 
into a tree such that the tree continues to be a Binary Search Tree. 
The method should return nothing.

A Binary Search Tree is a tree where every node has values greater than its data on the right-hand side, and values less than its data on the left-hand side, 
and all of the sub-tree nodes follow suit.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def print_bfs(self):
        if not self.root:
            return

        queue = [self.root]

        while len(queue) > 0:
            current_node = queue.pop(0)
            print(current_node.data)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    def in_order_traversal(self):
        nodes = []

        def dfs(node):
            if node:

                dfs(node.left)
                nodes.append(node.data)
                dfs(node.right)

        dfs(self.root)
        return nodes

    def insert(self, root, node):

        if node.data < root.data:
            if root.left is None:
                node.left = node
            else:
                self.insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                self.insert(root.right, node)

    def add(self, node):
        if self.root is None:
            self.root = node
        else:
            root = self.root
            self.insert(root, node)


tree = Tree()
# tree.root = Node(9)

# tree.root.left = Node(5)
# tree.root.right = Node(11)

# tree.root.left.left = Node(3)
# tree.root.left.right = Node(7)

tree.add(Node(5))
tree.add(Node(25))
print(tree.in_order_traversal())
