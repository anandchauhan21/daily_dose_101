"""
maximum-length-of-repeated-subarray
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.



Example 1:

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
Example 2:

Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5

Question link https://leetcode.com/problems/maximum-length-of-repeated-subarray/
"""
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        N,M = len(nums1), len(nums2)
        dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
        output = 0
        for i in range(1, N+1):
            for j in range(1, M+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                output = max(output,dp[i][j])
        return output

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        nums2_str = "".join([chr(x) for x in nums2])
        max_str = ""
        res = 0
        for i in nums1:
            max_str += chr(i)
            if max_str in nums2_str:
                res = max(res, len(max_str))
            else:
                max_str = max_str[1:]
        return res

x = Solution()
print(x.findLength(nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]))

