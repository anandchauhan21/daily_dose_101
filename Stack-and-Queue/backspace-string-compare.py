"""
backspace-string-compare
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.



Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.

Question link https://leetcode.com/problems/backspace-string-compare/
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_out, t_out = [], []
        for char in s:
            if char == "#":
                if s_out: s_out.pop()
            else:
                s_out.append(char)
        for char in t:
            if char == "#":
                if t_out: t_out.pop()
            else:
                t_out.append(char)
        if s_out == t_out:
            return True
        else:
            return False
x =Solution()
print(x.backspaceCompare("ab##","c#d#"))