"""
Title: Decode Ways
Description: A message containing letters from A-Z can be encoded into numbers using the mapping 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. 
Given a string s containing only digits, return the total number of ways to decode it. 
An empty string or a string starting with '0' has no valid decodings. 
The input string is guaranteed to contain only digits and may not contain leading zeros.

Args:
    s (str): A string containing only digits representing the encoded message.

Returns:
    int: The total number of ways to decode the given string.
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[-1] = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and int(s[i:i+2] < 27):
                dp[i] += dp[i + 2]
        
        return dp[0]