"""
Given an integer numRows, return the first numRows of Pascal's triangle.

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

qustion link https://leetcode.com/problems/pascals-triangle
"""

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []
        for row in range(numRows):
            add = []
            for i in range(row+1):
                if row == i or 0 == i:
                    add.append(1)
                else:
                    add.append(triangle[row-1][i-1] + triangle[row-1][i])
            triangle.append(add)
        return triangle
x = Solution()
print(x.generate(5))


