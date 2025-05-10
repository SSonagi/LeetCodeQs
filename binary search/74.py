"""
LeetCode 74: Search a 2D Matrix

Description:
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
1. Integers in each row are sorted from left to right.
2. The first integer of each row is greater than the last integer of the previous row.

You are given a matrix of integers and a target value. Your task is to determine if the target value exists in the matrix.

Parameters:
- matrix (List[List[int]]): A 2D list of integers representing the matrix.
- target (int): The integer value to search for in the matrix.

Returns:
- bool: True if the target value exists in the matrix, otherwise False.
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        low = 0
        high = rows * columns - 1

        while low <= high:
            mid_i = low + (high - low) // 2
            mid = matrix[mid_i // columns][mid_i % columns]
            if mid < target:
                low = mid_i + 1
            elif mid > target:
                high = mid_i - 1
            else:
                return True
        
        return False