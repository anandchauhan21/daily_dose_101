"""
median-of-two-sorted-arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

Question link https://leetcode.com/problems/median-of-two-sorted-arrays/
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(b) < len(a):
            a, b = b, a
        l, r = 0, len(a) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2
            aleft = a[i] if i >= 0 else float("-infinity")
            aright = a[i + 1] if (i + 1) < len(a) else float("infinity")
            bleft = b[j] if j >= 0 else float("-infinity")
            bright = b[j + 1] if (j + 1) < len(b) else float("infinity")

            if aleft <= bright and bleft <= aright:
                if total % 2:
                    return min(aright, bright)
                return (max(aleft, bleft) + min(aright, bright)) / 2
            elif aleft > bright:
                r = i - 1
            else:
                l = i + 1


x = Solution()
print(x.findMedianSortedArrays([1, 3], [2]))
