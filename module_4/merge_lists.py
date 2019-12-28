"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.


Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

"""


def merge_sorted_lists(nums1, nums2):
    
    # merge two lists - nums1 + nums2
    # iterate over the list
    # if element is out of order swap the elements
    # return the modified list

    nums1.extend(nums2)
    print(nums1)
    index = 0
    while index < len(nums1) - 1:
        if nums1[index] > nums1[index + 1]:
            print(f"sorting {nums1}")
            nums1[index], nums1[index + 1] = nums1[index + 1], nums1[index]
        index += 1

    return nums1


nums1 = [1, 2, 3]
nums2 = [2, 5, 6]
print(merge_sorted_lists(nums1, nums2))
