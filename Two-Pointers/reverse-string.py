"""
reverse-string
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:
1 <= s.length <= 105
s[i] is a printable ascii character.

Question link https://leetcode.com/problems/reverse-string/
"""

from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        l,r = 0,len(s)-1
        while l<r:
            tmp = s[l]
            s[l] = s[r]
            s[r] = tmp
            r -= 1
            l +=1
x =Solution()
s = ["h","e","l","l","o"]
x.reverseString(s)
print(s)
### out-put: ['o', 'l', 'l', 'e', 'h']