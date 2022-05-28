"""
majority-element-ii
Given an integer array of size n, find all elements that appear more than [ n/3 ] times.

Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]

Example 3:
Input: nums = [1,2]
Output: [1,2]

Constraints:
1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109

qustion link https://leetcode.com/problems/majority-element-ii/
"""

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
        cand1, count1 = None,0
        cand2, count2 = None,0
        for num in nums:
            if cand1 == num:
                count1 +=1
            elif cand2 == num:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 +=1
            elif count2 == 0:
                cand2 = num
                count2+=1
            else:
                count1,count2 = count1-1,count2-1
        return [x for x in (cand1,cand2) if nums.count(x) > len(nums) //3]
x = Solution()
print(x.majorityElement([1,2]))
