"""
letter-case-permutation
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create. Return the output in any order.

Example 1:
Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:
Input: s = "3z4"
Output: ["3z4","3Z4"]

Constraints
1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.

Question link https://leetcode.com/problems/letter-case-permutation/
"""
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output = [""]
        for c in s:
            tmp = []
            if c.isalpha():
                for o in output:
                    tmp.append(o+c.lower())
                    tmp.append(o+c.upper())
            else:
                for o in output:
                    tmp.append(o+c)
            output =tmp
        return output
x =Solution()
print(x.letterCasePermutation("a1b2"))
