"""
best-sightseeing-pair
You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.
Return the maximum score of a pair of sightseeing spots.

Example 1:
Input: values = [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11

Example 2:
Input: values = [1,2]
Output: 2

Constraints:
2 <= values.length <= 5 * 104
1 <= values[i] <= 1000

Question link https://leetcode.com/problems/best-sightseeing-pair/
"""
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        l = len(values)
        i, j = 0, 0
        maxres = 0
        for x in range(l):
            res = values[x] + values[x + 1] - (i + j)
            maxres = max(res, maxres)
            j += 1


