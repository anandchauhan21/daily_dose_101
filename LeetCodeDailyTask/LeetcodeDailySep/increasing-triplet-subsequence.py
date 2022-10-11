"""
increasing-triplet-subsequence
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.



Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.


Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1

question link https://leetcode.com/problems/increasing-triplet-subsequence/
"""
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf') # Initialize two variables to infinite
        for n in nums: # Loop through all numbers
            if n <= first: # If it is less then infinite you know you got the first triplet
                first = n
            elif n <= second: # If it is less then infinite you know you got the second triplet
                second = n
            else: # If its not less then the first and second then you know its the last value your looking for.
                return True
        return False