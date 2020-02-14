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
        curr_node = self.head
        
        while curr_node != None:
            curr_node = curr_node.next
            print(curr_node.data)


ll = LinkedList()
ll.extend([1, 2, 3, 4, 5])

ll.kth_from_the_end(1)