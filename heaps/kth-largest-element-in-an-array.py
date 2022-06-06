"""
kth-largest-element-in-an-array

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104

qustion link https://leetcode.com/problems/kth-largest-element-in-an-array/
"""

from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) -k
        def quickSelect(l,r):
            pivot, p = nums[r],l
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p],nums[i] = nums[i],nums[p]
                    p+=1
            nums[p],nums[r] = nums[r],nums[p]
            if p > k:   return quickSelect(l,p-1)
            elif p < k: return quickSelect(p+1,r)
            else:       return nums[p]
        return quickSelect(0,len(nums)-1)
x = Solution()
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(x.findKthLargest(nums,k))

###out-put: 4
