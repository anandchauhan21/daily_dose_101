"""
Search in a sorted 2D matrix
Given an m*n 2D matrix and an integer, write a program to find if the given integer exists in the matrix.

Given matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

qustion link https://leetcode.com/problems/search-a-2d-matrix/
"""
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROWS,COLS = len(matrix),len(matrix[0])
        top, bot = 0,ROWS-1
        while top<=bot:
            row = (top+bot)//2
            if target > matrix[row][-1]:
                top = row+1
            elif target < matrix[row][0]:
                bot = row-1
            else:
                break
            if not (top<=bot):
                return False
            row = (top+bot)//2
            l,r =0,COLS-1
            while l<=r:
                m = (l+r)//2
                if target > matrix[row][m]:
                    l = m+1
                elif target < matrix[row][m]:
                    r = m-1
                else:
                    return True
            return False
x = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(x.searchMatrix(matrix,target))


