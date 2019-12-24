"""
Given an array of integers, sort the array into a wave like array and return it, 
In other words, arrange the elements into a sequence such that a[1] >= a[2] <= a[3] >= a[4] <= a[5] ...

Example
Given [1, 2, 3, 4]

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]
"""
import random

def wave_array(integers):
    # iterate throught the array
    # shuffle every other elements
    for index in range(len(integers) - 1):
        integers[index], integers[index + 1] = integers[index + 1], integers[index]
    return integers


integers = [1, 2, 3, 4]
print(wave_array(integers))
