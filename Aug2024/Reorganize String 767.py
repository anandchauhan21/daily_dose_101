"""
767. Reorganize String
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.



Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""


Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.

link https://leetcode.com/problems/reorganize-string/description/
"""
import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt,char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)
        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            cnt,char = heapq.heappop(maxHeap)
            res+= char
            cnt += 1
            if prev:
                heapq.heappush(maxHeap)
                prev = None
            if cnt != 0:
                prev = [cnt,char]
            return res