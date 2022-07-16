"""
out-of-boundary-paths
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

Example 1:
Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6

Example 2:
Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12

Constraints:
1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n

Question link https://leetcode.com/problems/out-of-boundary-paths/
"""
from functools import lru_cache


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        @lru_cache(None)
        def moves(move, row, col):
            if row == m or row < 0 or col < 0 or col == n:
                return 1
            if move == 0:
                return 0
            move -= 1

            return (moves(move, row + 1, col) + moves(move, row, col + 1) + moves(move, row - 1, col) + moves(move, row, col - 1)) % ((10 ** 9) + 7)

        return moves(maxMove, startRow, startColumn)


x = Solution()
print(x.findPaths(2, 2, 2, 0, 0))
