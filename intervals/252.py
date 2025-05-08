"""
LeetCode 252: Meeting Rooms

Description:
Given an array of meeting time intervals where intervals[i] = [start_i, end_i], 
determine if a person could attend all meetings. A person can attend a meeting 
if and only if the meeting intervals do not overlap.

Example:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: False

Input: intervals = [[7,10],[2,4]]
Output: True

Constraints:
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= start_i < end_i <= 10^6
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda interval: interval.start)
        
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
            
        return True