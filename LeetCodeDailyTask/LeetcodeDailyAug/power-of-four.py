'''
power-of-four
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.



Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true


Constraints:

-231 <= n <= 231 - 1

Question link https://leetcode.com/problems/power-of-four/
'''
from math import log


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        res = log(n) / log(4)
        return res.is_integer()


x = Solution()
print(x.isPowerOfFour(16))
