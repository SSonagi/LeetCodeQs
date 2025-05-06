#56. Merge Intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ret = []

        for interval in intervals:
            if not ret:
                ret.append(interval)
            elif ret[-1][1] >= interval[0]:
                if ret[-1][1] <= interval[1]:
                    ret[-1][1] = interval[1]
            else:
                ret.append(interval)
            
        return ret