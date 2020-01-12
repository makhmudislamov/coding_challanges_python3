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
    
#    BRUTEFORCE

    # nums1_index = len(nums1) - 1
    # nums2_index = len(nums2) - 1

    # while nums2_index >= 0:
    #     nums1[nums1_index] = nums2[nums2_index]
    #     nums1_index -= 1
    #     nums2_index -= 1

    # print("nums1 after replace", nums1)

    # index = 0
    # while index < len(nums1) - 1:
    #     if nums1[index] > nums1[index + 1]:
        
    #         nums1[index], nums1[index + 1] = nums1[index + 1], nums1[index]
    #     index += 1

    # return nums1

    # SUBLINEAR APPROACH
    nums1_indx = 0
    nums2_indx = 0

    while nums1_indx < len(nums2):
        if nums2[nums2_indx] >= nums1[nums1_indx] or nums1[nums1_indx] == 0:
            # insert nums2[nums2_indx] at nums1[nums1_indx]
            # delete the last element in nums1
            nums2_indx += 1
        else:
            nums1_indx += 1


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
print(merge_sorted_lists(nums1, nums2))
