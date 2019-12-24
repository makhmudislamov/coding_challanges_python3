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
    if len(intervals) == 0:
        return intervals

    index = 0
    while index < len(intervals) - 1:
    #   check if the last item of an array is greater or equal to the first item of next array
        if intervals[index][1] > intervals[index + 1][0]:
            del intervals[index][1]
            del intervals[index + 1][0]
            intervals[index].extend(intervals[index + 1])
            del intervals[index + 1]
        # else:
        #     return intervals
        return intervals
    # else return the input itself
    # pass


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_overlapping_intervals(intervals))
