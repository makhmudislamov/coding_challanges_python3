"""
You're given an implementation for a Node and a Tree.
Implement the level-order, pre-order, in-order and post-order traversals for these trees. Return the data of each node in a list representing the requested order.


Given a tree that looks like this:
 
tree = Tree()
tree.root = Node(9)

tree.root.left = Node(5)
tree.root.right = Node(11)

tree.root.left.left = Node(3)
tree.root.left.right = Node(7)

Level Order
 
[9,5,11,3,7]

In-Order
 
[3,5,7,9,11]

Pre-Order
 
[9,5,3,7,11]

Post-Order
 
[3,7,5,11,9]
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def level_order_traversal(self):
        # return the tree as a list in a level-order sequence
        output_array = []
        if not self.root:
            return []
        
        queue = [self.root]
        while len(queue) > 0:
            cur_node = queue.pop(0)
            output_array.append(cur_node.data)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        return output_array


    def pre_order_traversal(self):
        # return the tree as a list in a pre-order sequence (dfs)
        output_arr = []
        def dfs(node):           
            if node:
                output_arr.append(node.data)
                dfs(node.left)
                dfs(node.right)
        dfs(self.root)
        return output_arr


    def in_order_traversal(self):
        # return the tree as a list in-order (dfs)
        output_arr = []

        def dfs(node):
            if node:
                dfs(node.left)
                output_arr.append(node.data)
                dfs(node.right)
        dfs(self.root)
        return output_arr

    def post_order_traversal(self):
        # return the tree as a list in a post-order sequence (dfs)
        output_arr = []

        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                output_arr.append(node.data)
        dfs(self.root)
        return output_arr


tree = Tree()
tree.root = Node(9)

tree.root.left = Node(5)
tree.root.right = Node(11)

tree.root.left.left = Node(3)
tree.root.left.right = Node(7)

print(tree.post_order_traversal())
