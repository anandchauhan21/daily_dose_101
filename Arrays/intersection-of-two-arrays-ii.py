"""
intersection-of-two-arrays-ii

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

Question link https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""
from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums1)
        output = []
        for n in nums2:
            if c[n] > 0:
                output.append(n)
                c[n] -= 1
        return output


x = Solution()
print(x.intersect([1, 2, 2, 1], [2, 2]))

#####


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1, d2 = {}, {}
        for i in nums1:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1
        for i in nums2:
            if i not in d2:
                d2[i] = 1
            else:
                d2[i] += 1
        res = []
        # print(d1, d2)
        for i in d1:
            if i in d2:
                res += [i] * min(d2[i], d1[i])
        return res