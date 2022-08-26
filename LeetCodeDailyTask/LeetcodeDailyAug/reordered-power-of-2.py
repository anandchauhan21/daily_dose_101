"""
reordered-power-of-2
You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.



Example 1:

Input: n = 1
Output: true
Example 2:

Input: n = 10
Output: false


Constraints:
1 <= n <= 109

Question link https://leetcode.com/problems/reordered-power-of-2/
"""


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        nums = [str(i) for i in str(n)]
        nums.sort()
        nums = "".join(nums)
        for i in range(31):
            curr = "".join(sorted(str((1 << i))))
            if curr == nums:
                return True
        return False
