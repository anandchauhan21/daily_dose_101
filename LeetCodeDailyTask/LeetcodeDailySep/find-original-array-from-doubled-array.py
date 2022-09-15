"""
find-original-array-from-doubled-array
An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.

Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.

Example 1:
Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].

Example 2:
Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.

Example 3:
Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.

Constraints:
1 <= changed.length <= 105
0 <= changed[i] <= 105

Question link https://leetcode.com/problems/find-original-array-from-doubled-array/
"""
from collections import Counter

changed = [1,3,4,2,6,8]
output = [1,3,4]
class Solution:
    def findOriginalArray(self, changed):
        c = Counter(changed)
        # int = [0,0,0,0]
        if c[0]%2:
            return []
        for x in sorted(c): # c = [1:1,2:1,3:1,4:1,6:1,8:1]
            if c[x] > c[2*x]: # [6,3,4,1] = c [1:1,3:1,4:1,6:1]
                return []
            c[2*x] -=c[x] if x else c[x]//2
        return list(c.elements())

x = Solution()
print(x.findOriginalArray([1, 3, 4, 2, 6, 8]))


