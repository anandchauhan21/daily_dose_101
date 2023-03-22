"""
number-of-zero-filled-subarrays
# Intuition
good
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
good
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: 0(n)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: 0(n)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
link https://leetcode.com/problems/number-of-zero-filled-subarrays/
"""
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        total = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                total +=1
            else:
                total = 0
            res += total
        return res


