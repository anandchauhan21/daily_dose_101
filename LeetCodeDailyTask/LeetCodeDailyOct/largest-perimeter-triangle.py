"""
largest-perimeter-triangle
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.



Example 1:

Input: nums = [2,1,2]
Output: 5
Example 2:

Input: nums = [1,2,1]
Output: 0


Constraints:

3 <= nums.length <= 104
1 <= nums[i] <= 106

Question link https://leetcode.com/problems/largest-perimeter-triangle/
"""
from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        A = sorted(nums)[::-1]
        for i in range(len(A) - 2):
            if A[i] < A[i + 1] + A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]
        return 0