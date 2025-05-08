"""
LeetCode 152: Maximum Product Subarray

Description:
Given an integer array `nums`, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated such that the answer will fit in a 32-bit integer.

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -10 <= nums[i] <= 10
- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tmp = curMax * n
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(tmp, curMin * n, n)
            res = max(res, curMax)

        return res