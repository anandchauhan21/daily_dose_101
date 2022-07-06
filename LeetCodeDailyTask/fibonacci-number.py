"""
fibonacci-number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Constraints:
0 <= n <= 30

Question link https://leetcode.com/problems/fibonacci-number/
"""


# Easy solution
class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        prev1, prev2 = 1, 0
        output = 0
        for i in range(2, n + 1):
            output = prev1 + prev2
            prev2 = prev1
            prev1 = output
        return output

x = Solution()
print(x.fib(6))


############################################################################
# Efficient Solution
class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        l = [0, 1]
        for i in range(n - 1):
            l.append(l[len(l) - 1] + l[len(l) - 2])
        return l[-1]
