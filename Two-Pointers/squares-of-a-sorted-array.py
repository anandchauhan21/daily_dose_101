"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

Question Link https://leetcode.com/problems/squares-of-a-sorted-array/
"""

from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l ,r = 0, len(nums)-1
        res = []
        while(l<=r):
            if nums[l]*nums[l] > nums[r]*nums[r]:
                res.append(nums[l]*nums[l])
                l += 1
            else:
                res.append(nums[r]*nums[r])
                r -= 1
        return res[::-1]
x =Solution()
print(x.sortedSquares([-4,-1,0,3,10]))
###out-put: [0, 1, 9, 16, 100]
