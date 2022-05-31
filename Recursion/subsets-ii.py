"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10

qustion link https://leetcode.com/problems/subsets-ii/
"""


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        def backtrack(i, sunset):
            if i == len(nums):
                res.append(sunset[::])
                return
            # All subsets that include nums[i]
            sunset.append(nums[i])
            backtrack(i+1,sunset)
            sunset.pop()
            #All subsets that don't include nums[i]
            while i +1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtrack(i +1,sunset)
        backtrack(0,[])
        return res
x = Solution()
print(x.subsetsWithDup([1,2,2]))
###out-put: [[1, 2, 2], [1, 2], [1], [2, 2], [2], []]
