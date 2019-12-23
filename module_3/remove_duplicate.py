"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""

def removeDuplicates(nums) -> int:

    print(f"initial list {nums}")
    for _, item in enumerate(nums):
        if nums.count(item) > 1:
            nums.remove(item)
    print(f"modified list {nums}")
    return len(nums)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums))
