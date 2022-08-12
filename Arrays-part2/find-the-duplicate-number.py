"""
find-the-duplicate-number
Given an array of N + 1 size, where each element is between 1 and N. Assuming there is only one duplicate number,
your task is to find the duplicate number.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Constraints:
1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.

Question link https://leetcode.com/problems/find-the-duplicate-number/
"""

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
x = Solution()
print(x.findDuplicate([1,3,4,2,2]))


