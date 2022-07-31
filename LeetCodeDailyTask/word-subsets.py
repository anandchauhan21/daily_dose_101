"""
word-subsets
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

    For example, "wrr" is a subset of "warrior" but is not a subset of "world".

A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

 

Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]

Example 2:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]

 

Constraints:

    1 <= words1.length, words2.length <= 104
    1 <= words1[i].length, words2[i].length <= 10
    words1[i] and words2[i] consist only of lowercase English letters.
    All the strings of words1 are unique.

Question link https://leetcode.com/problems/word-subsets/

"""

from typing import List
from collections import Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        totalword = {}
        for b in words2:
            tmp = Counter(b)
            for k,v in tmp.items():
                if k not in totalword:
                    totalword[k] = v
                else:
                    totalword[k] = max(v,totalword[k])
        output = []
        for a in words1:
            tmp = Counter(a)
            if all([k in tmp and v <= tmp[k] for k,v in totalword.items()]):
                output.append(a)
        return output

x = Solution()
print(x.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]))


