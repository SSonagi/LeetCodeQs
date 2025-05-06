"""
LeetCode 57: Insert Interval

Description:
You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start_i, end_i]` represent the start and the end of the ith interval and `intervals` is sorted in ascending order by `start_i`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `start_i` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return the resulting array of intervals.

Parameters:
- intervals (List[List[int]]): A list of non-overlapping intervals sorted by their start times.
- newInterval (List[int]): A new interval to be inserted into the list of intervals.

Returns:
- List[List[int]]: The updated list of intervals after inserting and merging the new interval.
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        added = False

        for interval in intervals:
            if interval[1] >= newInterval[0] and interval[0] <= newInterval[1]:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
            elif interval[0] > newInterval[1] and not added:
                ret.append(newInterval)
                ret.append(interval)
                added = True
            else:
                ret.append(interval)
        
        if not added:
            ret.append(newInterval)
        
        return ret