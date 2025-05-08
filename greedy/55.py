"""
LeetCode 55: Jump Game

Description:
You are given an integer array `nums`. You are initially positioned at the first index, and each element in the array represents your maximum jump length at that position.

Return `true` if you can reach the last index, or `false` otherwise.

Example:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_travel = 0
        for num in nums[:-1]:
            max_travel -= 1
            max_travel = max(max_travel, num)
            
            if max_travel <= 0:
                return False
        
        return True