"""
first-unique-character-in-a-string
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
1 <= s.length <= 105
s consists of only lowercase English letters.

Question link https://leetcode.com/problems/first-unique-character-in-a-string/
"""
from collections import Counter
class Solution:
    def firstUniqChar(self,s: str) -> int:
        counter = Counter(list(s))
        for i in range(len(s)):
            if counter.get(s[i]) == 1:
                return i
        return -1

x = Solution()
print(x.firstUniqChar("leetcode"))


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            d[s[i]] = d.get(s[i],0) + 1
        for i in d:
            if d[i] == 1:
                return s.find(i)
        return -1