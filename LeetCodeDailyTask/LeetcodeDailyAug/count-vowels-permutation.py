"""
count-vowels-permutation
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3:

Input: n = 5
Output: 68


Constraints:

1 <= n <= 2 * 10^4

Question link https://leetcode.com/problems/count-vowels-permutation/
"""


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[], [1, 1, 1, 1, 1]]
        a, e, i, o, u = 0, 1, 2, 3, 4
        mod = 10 ** 9 + 7
        for j in range(2, n + 1):
            dp.append([0, 0, 0, 0, 0])
            dp[j][a] = (dp[j - 1][e] + dp[j - 1][i] + dp[j - 1][u])
            dp[j][e] = (dp[j - 1][a] + dp[j - 1][i]) % mod
            dp[j][i] = (dp[j - 1][e] + dp[j - 1][o]) % mod
            dp[j][o] = dp[j - 1][i]
            dp[j][u] = dp[j - 1][i] + dp[j - 1][o]
        return sum(dp[n]) % mod

x = Solution()
print(x.countVowelPermutation(5))
