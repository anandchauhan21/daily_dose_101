"""
search-insert-position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

Question link https://leetcode.com/problems/search-insert-position/

"""

from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l ,r = 0,len(nums) -1
        while (l<=r):
            mid = (l+r) //2
            #print(nums[mid])
            if target == nums[mid]:
                return mid
            if nums[mid] > target:
                r = mid - 1
            else:
                 l = mid + 1
        return l

x =Solution()
print(x.searchInsert([1,2,3,4,5,6,7,8,9,10], 6))