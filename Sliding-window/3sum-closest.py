"""
3sum-closest
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
 

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0

 
Constraints:

    3 <= nums.length <= 1000
    -1000 <= nums[i] <= 1000
    -104 <= target <= 104

Question link https://leetcode.com/problems/3sum-closest/
"""
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums) - 2):
            s = i + 1
            e = len(nums) - 1
            while s < e:
                sumhere = nums[i] + nums[s] + nums[e]
                if abs(sumhere - target) < abs(res - target):
                    res = sumhere
                if sumhere < target:
                    s += 1
                else:
                    e -= 1
        return res
x = Solution()
print(x.threeSumClosest([-1,2,1,-4], 1))


