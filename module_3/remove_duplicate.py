def removeDuplicates(nums) -> int:
    prev = 0
    next_el = prev + 1

    while next_el < len(nums):
        if nums[prev] == nums[next_el]:
            del nums[next_el]
            prev += 1
    return len(nums)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums))
