"""
Given this implementation of a Binary Tree, write a function to balance the 
binary tree to reduce the height as much as possible.

For example, given a tree where the nodes have been added in an order 
such that the height is higher than it could be:

Nodes have been added in this order:
tree = Tree()

tree.add(Node(6))
tree.add(Node(27))
tree.add(Node(15))
tree.add(Node(10))
tree.add(Node(13))
tree.add(Node(8))

Hint:
Make sure to use the add() method in your balancing- you may have to traverse the whole tree, 
and re-add all nodes to the tree in a particular order. 
If so, you've probably seen this ordering somewhere before... 
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        ## INSTEAD, non binary
        self.children = []

        self.parent = None


class Tree:
    def __init__(self):
        self.root = None

    def in_order_traversal(self):

        def dfs(node):
            if node:

                dfs(node.left)
                print(node.data)
                dfs(node.right)

        dfs(self.root)

    def level_order_traversal(self):
        if not self.root:
            return

        queue = [self.root]

        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node.left:
                queue.append(current_node.left)
            print(current_node.data)
            if current_node.right:
                queue.append(current_node.right)

    def add(self, node):
        if not self.root:
            self.root = node
            return

        def insert(root, node):

            if root.data > node.data:
                if root.left is None:
                    root.left = node
                else:
                    insert(root.left, node)
            else:

                if root.right is None:
                    root.right = node
                else:
                    insert(root.right, node)

        insert(self.root, node)

    def height(self):

        def get_height(node):

            if node is None:
                return 0
            else:
                left_height = get_height(node.left)
                right_height = get_height(node.right)

                if left_height > right_height:
                    return left_height + 1
                else:
                    return right_height + 1
            return get_height(self.root)

    def balance(self):
        # write a function to reduce the height of this tree as much as possible
        pass
