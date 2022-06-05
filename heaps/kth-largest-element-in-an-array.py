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

