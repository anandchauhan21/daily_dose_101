"""
number-of-submatrices-that-sum-to-target
Given a matrix and a target, return the number of non-empty submatrices that sum to target.
A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

Example 1:
Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.

Example 2:
Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

Example 3:
Input: matrix = [[904]], target = 0
Output: 0

Constraints:
1 <= matrix.length <= 100
1 <= matrix[0].length <= 100
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8

Question link https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
"""
from collections import defaultdict
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        N, M = len(matrix[0]), len(matrix)
        output = 0
        for r in matrix:
            for i in range(1, len(r)):
                r[i] += r[i - 1]
        for start in range(N):
            for end in range(start, N):
                lookup = defaultdict(int)
                cumsum = 0
                lookup[0] = 1
                for k in range(M):
                    cumsum += matrix[k][end] - (matrix[k][start - 1] if start != 0 else 0)
                    if cumsum - target in lookup:
                        output += lookup[cumsum - target]
                    lookup[cumsum] += 1
        return output


x = Solution()
print(x.numSubmatrixSumTarget([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0))
