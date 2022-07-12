"""
bulls-and-cows
The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.



Example 1:

Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"
Example 2:

Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.


Constraints:

1 <= secret.length, guess.length <= 1000
secret.length == guess.length
secret and guess consist of digits only.

Question link https://leetcode.com/problems/bulls-and-cows/
"""
from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull, cow = 0, 0
        s = list(secret)
        g = list(guess)

        i, j = 0, 0
        while i < len(secret):
            if s[j] == g[j]:
                bull += 1
                s.pop(j)
                g.pop(j)
            else:
                j += 1
            i += 1
        count = Counter(s)
        for l in g:
            if l in count and count[l] > 0:
                cow += 1
                count[l] -= 1
        return "{}A{}B".format(bull, cow)


x = Solution()
print(x.getHint("1807", "7810"))
