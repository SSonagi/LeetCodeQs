"""
Title: Non-overlapping Intervals
Description: Given an array of intervals `intervals` where intervals[i] = [start_i, end_i], 
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Parameters:
    intervals (List[List[int]]): A list of intervals where each interval is represented as a list of two integers [start, end].

Returns:
    int: The minimum number of intervals that need to be removed to make the rest of the intervals non-overlapping.

Constraints:
    - 1 <= intervals.length <= 10^5
    - intervals[i].length == 2
    - -5 * 10^4 <= start_i < end_i <= 5 * 10^4
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ret = 0
        lowest_high = intervals[0][1]
        for i in range(1, len(intervals)):
            if lowest_high > intervals[i][0]:
                ret += 1
                lowest_high = min(lowest_high, intervals[i][1])
            else:
                lowest_high = intervals[i][1]
        
        return ret