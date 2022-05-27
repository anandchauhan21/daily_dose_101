"""
majority-element
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

qustion link https://leetcode.com/problems/majority-element/
"""

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        res, count = 0,0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res

x = Solution()
print(x.majorityElement([2,2,1,1,1,2,2]))
