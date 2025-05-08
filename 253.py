"""
Title: Meeting Rooms II
Description: Given an array of meeting time intervals consisting of start and end times 
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

You may assume that no two meetings can take place at the same time in the same room, 
and a meeting can only end before another one starts in the same room.

Parameters:
    intervals (List[List[int]]): A list of meeting time intervals where each interval 
    is represented as a list [start, end].

Returns:
    int: The minimum number of conference rooms required to accommodate all meetings.
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        # the min_heap keeps track of the end time of the meetings in each room
        min_heap = []

        # at each loop, we check if the next meeting can be scheduled in the room that ends the earliest
        for interval in intervals:
            # if yes, we pop the room from the heap and push the end time of the next meeting into the heap
            # if no, we need to create a new room, so we push the end time of the next meeting into the heap
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)

        # the size of the heap at the end is the number of rooms we need
        return len(min_heap)

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # We use a list to store the start and end times of all meetings
        time = []
        for i in intervals:
            time.append((i.start, 1))
            time.append((i.end, -1))
        
        # Sort the time list. If two times are the same, we want to end the meeting first, this is for the case when a meeting ends at the same time another starts
        time.sort(key=lambda x: (x[0], x[1]))
        
        # We use a counter to keep track of the number of meetings at the same time
        # The maximum value of the counter at any time is the number of rooms we need
        res = count = 0
        for t in time:
            count += t[1]
            res = max(res, count)
        return res