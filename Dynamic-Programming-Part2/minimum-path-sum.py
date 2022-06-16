"""
minimum-path-sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100

Question link https://leetcode.com/problems/minimum-path-sum/
"""

from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid),len(grid[0])

        res = [[float("inf")]*(COLS+1) for r in range(ROWS+1)]
        res[ROWS-1][COLS] = 0
        for r in range(ROWS -1,-1,-1):
            for c in range(COLS-1,-1,-1):
                res[r][c] = grid[r][c]+min(res[r+1][c],res[r][c+1])
        return res[0][0]
x = Solution()
print(x.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
###out-put: 7

