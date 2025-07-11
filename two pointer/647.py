"""
### LeetCode 647: Palindromic Substrings

#### Description:
Given a string `s`, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward. A substring is a contiguous sequence of characters within the string.

#### Example:
Input: s = "abc"
Output: 3
Explanation: Three palindromic substrings are "a", "b", "c".

Input: s = "aaa"
Output: 6
Explanation: Six palindromic substrings are "a", "a", "a", "aa", "aa", "aaa".

#### Constraints:
- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters only.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i + 1)
        return res

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res