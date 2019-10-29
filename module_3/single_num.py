"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


Example 1:
Input: [2,2,1]
Output: 1

"""


def single_number(integers):
# INPUT >>> non-emtpy array. OUTPUT >>> int

# PSEUDOCODE - brute force
# iterate over the integers arr
# use .count to check if the element appears only once


    # for integer in integers:
    #     if integers.count(integer) == 1:
    #         return integer

# ANOTHER SOLUTION
# create set 
# add array elements to set only if it is not in the set already


    int_set = set()

    for integer in integers:

        if not integer in int_set:
            int_set.add(integer)
        elif integer in int_set:
            int_set.remove(integer)
    
    return int_set.pop()
   
        
       







 




integers = [2, 3, 3, 2, 5, 6, 6]

print(single_number(integers))


