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

# MODEL SOLUTION
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.left = None
#     self.right = None


# class Tree:
#   def __init__(self):
#     self.root = None

#   def level_order_traversal(self):
#     # return the tree as a list in a level-order sequence
#     traversed_list = []
#     if not self.root:
#       return []

#     queue = [self.root]

#     while len(queue) > 0:
#       current_node = queue.pop(0)
#       traversed_list.append(current_node.data)
#       if current_node.left:
#         queue.append(current_node.left)
#       if current_node.right:
#         queue.append(current_node.right)

#     return traversed_list

#   def pre_order_traversal(self):
#     # return the tree as a list in a pre-order sequence (dfs)
#     traversed_list = []

#     def dfs(node, traversed_list):
#       if node:
#         traversed_list.append(node.data)
#         dfs(node.left, traversed_list)
#         dfs(node.right, traversed_list)

#     dfs(self.root, traversed_list)
#     return traversed_list

#   def in_order_traversal(self):
#     # return the tree as a list in-order (dfs)
#     traversed_list = []

#     def dfs(node, traversed_list):
#       if node:
#         dfs(node.left, traversed_list)
#         traversed_list.append(node.data)
#         dfs(node.right, traversed_list)

#     dfs(self.root, traversed_list)
#     return traversed_list

#   def post_order_traversal(self):
#     # return the tree as a list in a post-order sequence (dfs)
#     traversed_list = []

#     def dfs(node, traversed_list):
#       if node:
#         dfs(node.left, traversed_list)
#         dfs(node.right, traversed_list)
#         traversed_list.append(node.data)

#     dfs(self.root, traversed_list)
#     return traversed_list
