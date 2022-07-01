"""
rotate-array

Given an array, rotate the array to the right by k steps,
where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

Question link https://leetcode.com/problems/rotate-array/
"""

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l,r = 0, len(nums) -1
        k = k % len(nums)
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l,r = l+1, r -1
        l,r = 0, k-1
        while l < r:
            nums[l], nums[r] = nums[r],nums[l]
            l,r = l+1 ,r-1
        l,r = k, len(nums) -1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

x = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
x.rotate(nums,k)
print(nums)
###out-put: [5, 6, 7, 1, 2, 3, 4]

