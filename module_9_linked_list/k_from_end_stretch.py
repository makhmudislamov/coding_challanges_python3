"""
Write a function that, when given a Singly
Linked List and an integer k, will return the kth element from the end of the list.
"""
### do not modify this class


class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None

### do not modify this class, or any of the methods in it, other than kth_from_the_end()
### you may insert new methods if you like


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head == None

    def append(self, data):
        if self.empty():
            self.head = LinkedNode(data)
            self.tail = self.head
        else:
            new_node = LinkedNode(data)
            self.tail.next = new_node
            self.tail = new_node

    def extend(self, array):
        for element in array:
            self.append(element)

  # implement this method
    def kth_from_the_end(self, k):
        # iterate over the LL
        # BRUTE FORCE
        # curr_node = self.head
        # node_position = 0
        # while curr_node.next != None:
        #     curr_node = curr_node.next
        #     node_position += 1

        # curr_node = self.head
        # for _ in range(node_position - k):
        #     curr_node = curr_node.next

        # return curr_node.data  

        # TWO POINTERS METHOD
        # have two pointers
        # one moves k times
        # second one moves one step until k reaches None
        # return data at second pointer node
        # use two loops 
        # k_times_mover = 0
        every_kth_node = self.head
        while every_kth_node.next != None:
            every_kth_node = every_kth_node.next
            # k_times_mover += k
            print(every_kth_node.data)
        
        kth_element = 0
        curr_node = self.head
        for _ in range(k_times_mover):
            # kth_element += 1
            curr_node = curr_node.next
            print(curr_node.data)
        # return curr_node.data
        pass     


ll = LinkedList()
ll.extend(['A', 'B', 'C', 'D', 'E', 'F', 'M'])

print(ll.kth_from_the_end(2))

# MODEL SOLUTION
# borrowed from previous problem solution
#   def length(self):
#     curr = self.head
#     count = 0
#     while not (curr is None):
#       curr = curr.next
#       count += 1
#     return count

#   # borrowed from previous problem
#   def get(self, index):
#     curr = self.head
#     count = index
#     while count > 0:
#       curr = curr.next
#       count -= 1
#     return curr.data

#   # implement this method
#   def kth_from_the_end(self, k):
#     return self.get(self.length() - k - 1)
