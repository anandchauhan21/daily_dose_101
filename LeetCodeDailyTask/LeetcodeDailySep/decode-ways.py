"""
decode-ways
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

Constraints:
1 <= s.length <= 100
s contains only digits and may contain leading zero(s).

Question link https://leetcode.com/problems/decode-ways/
"""

# Time Complexity: O(N)
# Space Complexity: O(N)
# This solution can be further space-optimized to be O(1). Let's think about it :D
class Solution:
    # number of ways to do something -> think about dp
    def numDecodings(self, s: str) -> int:
        # cannot map to any character due to the leading zero
        if s[0] == '0':
            return 0
        n = len(s)
        # dp[i]: number of ways of decoding the substring s[:i]
        dp = [0 for _ in range(n + 1)]
        # base case
        dp[0] = 1
        for i in range(1, n + 1):
            # check single digit decode
            # valid deocde is possible only when s[i - 1] is not zero
            # if so, take the previous state dp[i - 1]
            # e.g. AB - 1[2]
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            # check double digit decode
            # by looking at the previous two digits
            # if the substring belongs to the range [10 - 26]
            # then add the previous state dp[i - 2]
            # e.g. L - [12]
            if i >= 2:
                # or you can use `stoi(s.substr(i - 2, 2))`
                x = int(s[i - 2: i])
                # check the range
                if 10 <= x <= 26:
                    dp[i] += dp[i - 2]
        return dp[n]

x = Solution()
print(x.numDecodings("12"))
