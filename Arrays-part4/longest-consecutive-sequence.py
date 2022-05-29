"""
longest-consecutive-sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109

qustion link https://leetcode.com/problems/longest-consecutive-sequence/
"""
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        Longest = 0
        for n in nums:
            """check if it's the start of the sequence"""
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length+=1
                Longest = max(length,Longest)
        return Longest
x = Solution()
print(x.longestConsecutive([100,4,200,1,3,2]))
