"""
reshape-the-matrix
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.
You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.
The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:
Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 100
-1000 <= mat[i][j] <= 1000
1 <= r, c <= 300

Question link https://leetcode.com/problems/reshape-the-matrix/
"""

from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        N, M = len(mat[0]), len(mat)
        T = r * c
        if N * M != T: return mat
        output = [[0 for _ in range(c)] for _ in range(r)]
        k = 0
        for i in range(M):
            for j in range(N):
                output[k // c][k % c] = mat[i][j]
                k += 1
        return output


x = Solution()
print(x.matrixReshape([[1, 2], [3, 4]], 1, 4))
###out-put: [[1, 2, 3, 4]]
