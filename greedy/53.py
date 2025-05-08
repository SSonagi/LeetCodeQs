"""
LeetCode 53: Maximum Subarray

Description:
Given an integer array `nums`, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        ret = float("-inf")
        for num in nums:
            total += num
            ret = max(ret, total)
            if total < 0:
                total = 0
        
        return ret
