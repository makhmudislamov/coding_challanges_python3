"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
Do not return anything, modify the input array in-place instead.
"""


def rotate_array(input_array, k):
    # PSEUDOCODE:
    # for k times:
    # take end of the list item
    # put it to the beginning

    # SOLUTION 1:
    # for t in range(1, k + 1):
    #     # getting last element
    #     end_element = input_array[-1]
    #     # inserting the last elemnt to the start of the array
    #     input_array.insert(0, end_element)
    #     # deleting the lat element
    #     input_array.pop()

    # SOLUTION 2:
    # slice the array from last to k index
    # cut it and past to the beginning of the array

    prepend_elements = input_array[-k:]
    input_array = prepend_elements + input_array
    # deleting last k elements
    del input_array[-k:]

    return input_array


input_array = [1, 2, 3, 4, 5, 6, 7]
print(rotate_array(input_array, 1))

