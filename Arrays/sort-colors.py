"""
Given an array consisting of only 0s, 1s and 2s. Write a program to in-place sort the array without using inbuilt sort functions.
( Expected: Single pass-O(N) and constant space)

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.

qustion link https://leetcode.com/problems/sort-colors/
"""
class Solution:
    def sortColors(self, nums:list[int]) -> None:
        l,r = 0, len(nums)-1
        i = 0
        def swap(i ,j):
            tem = nums[i]
            nums[i] = nums[j]
            nums[j] = tem
        while i <= r:
            if nums[i] == 0:
                swap(l,i)
                l+=1
            elif nums[i] == 2:
                swap(i,r)
                r-=1
                i-=1
            i +=1


nums = [2,0,2,1,1,0]
x = Solution()
x.sortColors(nums)
print(nums)
