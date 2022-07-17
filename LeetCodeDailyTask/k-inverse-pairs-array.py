"""
k-inverse-pairs-array
For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.

Example 1:
Input: n = 3, k = 0
Output: 1
Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.

Example 2:
Input: n = 3, k = 1
Output: 2
Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.

Constraints:
1 <= n <= 1000
0 <= k <= 1000

https://leetcode.com/problems/k-inverse-pairs-array/
"""


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        if k == 0: return 1
        memo = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            memo[i][0] = 1
        if n < 2:
            return memo[n][k]
        memo[2][1] = 1

        for i in range(3, n + 1):
            mx = min(k, (n * (n - 1)) // 2)
            for j in range(1, mx + 1):
                memo[i][j] = memo[i - 1][j] + memo[i][j - 1]

                if j >= i:
                    memo[i][j] -= memo[i - 1][j - i]
        return memo[n][k] % mod


x = Solution()
print("ans:", x.kInversePairs(3, 1))


class Solution:
    # A very good description of the dp solution is at
    # https://leetcode.com/problems/k-inverse-pairs-array/solution/
    # The code below uses two 1D arrays--dp and tmp--instead if a
    # 2D array. tmp replaces dp after each i-iteration.
    def kInversePairs(self, n: int, k: int) -> int:
        dp, mod = [1] + [0] * k, 1000000007

        for i in range(n):
            tmp, sm = [], 0
            for j in range(k + 1):
                sm += dp[j]
                if j - i >= 1: sm -= dp[j - i - 1]
                sm %= mod
                tmp.append(sm)
            dp = tmp
            # print(dp)       # <-- uncomment this line to get a sense of dp from the print output
            #     try n = 6, k = 4; your answer should be 49.
        return dp[k]