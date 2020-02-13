"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        return self.stack

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        return self.stack

    def top(self):
        """
        :rtype: int
        """
        top_element_inx = len(self.stack) - 1 
        return self.stack[top_element_inx]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# MODEL SOLUTION
# class MinStack(object):

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         # this should be the systems maximum size
#         self.currentMin = float("inf")
#         self.stack = []
    #     return

    # def push(self, numToPush):
    #     """
    #     :type numToPush: int
    #     :rtype: None
    #     """
    #     if numToPush <= self.currentMin:
    #     	self.stack.append(self.currentMin)
    #     	self.currentMin = numToPush
    #     self.stack.append(numToPush)

    # def pop(self):
    #     """
    #     :rtype: None
    #     """
    #     # NOTE: self.stack.pop() is NOT using the property
    #     # pop method we are currently defining.
    #     # Python has a built-n array pop method.
    #     # This is NOT recursion.
    #     if self.stack.pop() == self.currentMin:
    #     	self.currentMin = self.stack.pop()

    # def top(self):
    #     """
    #     :rtype: int
    #     """
    #     if (self.stack == []):
    #     	return None
    #     return self.stack[-1]

    # def getMin(self):
    #     """
    #     :rtype: int
    #     """
    #     return self.currentMin

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# NOTES ---
# So this solution is pretty clever and vastly reduces the
# amount of data that is stored to solve this problem.
# Common solutions include making another stack
# to keep track of minimums or using an array to
# to store two pieces of data at once.
#
# This solution uses the natural attributes of numbers to
# save space.
# Whenever a new minimum is encountered, push the old minimum
# and the new minimum, in that order.
# Then when you pop, if the number you pop is equal to the current minimum
# Set the currentMin to the item on the stack (by popping). Since we
# the previous minimum before storing the current minimum, we can safely
# use the current minimum as a flag to pop again for the next minimum.
