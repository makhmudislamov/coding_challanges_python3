"""
Reverse a singly linked list.
Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

### do not modify this class


class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None

### do not modify this class, or any of the methods in it, other than reverse()
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

  # used in test cases verify correct solutions
  # if you want to test your code without submitting, consider using this function
    def to_array(self):
        array = []
        curr = self.head
        while curr != None:
            array.append(curr.data)
            curr = curr.next
        return array

  # implement this method
    def reverse(self):
        # declared previous node starting with None
        # until head doesnt point to None
        # use temporary pointer starting with head
        # move head to next node
        # move temporary pointer to previous node
        # set previous node to temporary pointer
        # NOTE: this doesn't return 5->4->3->2->1->NULL
        # this returns NULL<-1<-2<-3<-4<-5 
        previous_node = None
        while self.head:            
            temporary_pointer = self.head
            self.head = self.head.next
            temporary_pointer.next = previous_node
            previous_node = temporary_pointer            
        return self



            

ll = LinkedList()
ll.extend([1, 2, 3, 4, 5, 6, 7, 8, 9])

ll.reverse()
print(ll.to_array())



