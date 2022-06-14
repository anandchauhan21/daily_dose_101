"""
maximum-product-subarray

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
Accepted
766,358
Submissions
2,212,548

Question link https://leetcode.com/problems/maximum-product-subarray/
"""
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1,1

        for n in nums:
            tmp = curMax*n
            curMax = max(n*curMax,n*curMin,n)
            curMin = min(n * curMax, n * curMin, n)
            res = max(res,curMax)
        return res
x = Solution()
print(x.maxProduct([2,3,-2,4]))

###out-put: 6