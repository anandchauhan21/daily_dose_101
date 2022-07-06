"""
ransom-note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

Question link https://leetcode.com/problems/ransom-note/
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ra = sorted(ransomNote)
        ma = sorted(magazine)
        for char in ma:
            if ra and char == ra[0]:
                ra.pop(0)
        if ra:
            return False
        else:
            return True


x = Solution()
print(x.canConstruct("a", "b"))


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ma = list(magazine)
        for i in ransomNote:
            if i not in magazine:
                return False
            ma.remove(i)
        return True
