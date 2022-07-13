"""
n-th-tribonacci-numbern-th-tribonacci-number
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537


Constraints:
0 <= n <= 37

question link https://leetcode.com/problems/n-th-tribonacci-number/
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        pr1, pr2, pr3 = 1, 1, 0
        if n == 0: return pr3
        if n == 1: return pr2
        if n == 2: return pr1

        output = 0
        for _ in range(3, n + 1):
            output = pr1 + pr2 + pr3
            pr3 = pr2
            pr2 = pr1
            pr1 = output
        return output
x =Solution()
print(x.tribonacci(25))


class Solution:
    def tribonacci(self, n: int) -> int:
        dp = []
        dp.append(0)
        dp.append(1)
        dp.append(1)

        for i in range(3, n + 1):
            dp.append(dp[i - 2] + dp[i - 1] + dp[i - 3])
        return dp[n]