"""
move-zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

Question link https://leetcode.com/problems/move-zeroes/
"""

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l +=1
        return nums

x = Solution()
nums = [0,1,0,3,12]
print(x.moveZeroes(nums))
###out-put: [1, 3, 12, 0, 0]
