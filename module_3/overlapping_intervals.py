"""
Given a collection of intervals, merge all overlapping intervals.

For example:
Given [1,3],[2,6],[8,10],[15,18],

return [1,6],[8,10],[15,18].

Make sure the returned intervals are sorted.
"""

def merge_overlapping_intervals(intervals):
    # if the input is empty
    # return the input
  for interval in intervals:
    #   check if the last item of an array is greater or equal to the first item of next array
    #   if so pop those items and merge the arrays
    #   return the array
    # else return the input itself
    pass


intervals = [1, 3], [2, 6], [8, 10], [15, 18]
merge_overlapping_intervals(intervals)
