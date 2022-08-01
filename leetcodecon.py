"""
contest
"""
from collections import Counter
from typing import List

'''
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        w = 1

        while sum(nums):
            for j in range(len(nums)):
                if nums[j] == 0:
                    continue
                else:
                    nums[j] -= w
            w += 1
        return w


x = Solution()
'''


class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        res = 0
        l, r = 0, 0
        c = Counter(edges)
        s = sum(c)
        el = len(edges)
        if s == len(edges) + 1:
            return -1
        else:
            for i in range(len(edges)):
                if edges[l] == edges[r]:
                    edges[l] = edges[r]
                else:
                    res += 1
                r += 1
            return res + 1
# [2,-1,3,1]
#   edges = [2, 3, 4, 2, 3]
#  [3,3,4,2,3]
x = Solution()
print(x.longestCycle([3, 3, 4, 2, 3]))
