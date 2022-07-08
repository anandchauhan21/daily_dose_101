"""
01-matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.

Question link https://leetcode.com/problems/01-matrix/
"""
import sys
from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        queue = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ans = [[0] * n for _ in range(m)]
        visited = set()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        dist = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if mat[i][j] == 1:
                    ans[i][j] = dist
                for d in directions:
                    ni = i + d[0]
                    nj = j + d[1]

                    if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                        queue.append((ni, nj))
                        visited.add((ni, nj))
            dist += 1
        return ans


x = Solution()
print(x.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        ans = [[sys.maxsize] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                else:
                    left = ans[i][j - 1] if j > 0 else sys.maxsize
                    up = ans[i - 1][j] if i > 0 else sys.maxsize
                    ans[i][j] = min(left, up) + 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                else:
                    right = ans[i][j + 1] if j < n - 1 else sys.maxsize
                    down = ans[i + 1][j] if i < m - 1 else sys.maxsize
                    ans[i][j] = min(ans[i][j], min(right, down) + 1)
        return ans
