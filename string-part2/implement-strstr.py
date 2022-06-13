"""
implement-strstr

Implement strStr().
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

Question link https://leetcode.com/problems/implement-strstr/
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle =="":
            return 0
        for i in range(len(haystack) +1 - len(needle)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
x = Solution()
print(x.strStr("hello","ll"))

###out-put: 2
