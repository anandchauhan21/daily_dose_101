"""
unique-paths
Given a matrix m X n, count paths from left-top to the right bottom of a matrix with the constraints that from each cell
you can either only move to the rightward direction or the downward direction.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:
1 <= m, n <= 100

qustion link https://leetcode.com/problems/unique-paths/
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row= [1]*n
        for i in range(m-1):
            newRow =[1]*n
            for j in range(n-2,-1,-1):
                newRow[j]=newRow[j+1]+row[j]
            row=newRow
        return  row[0]
x =Solution()
print(x.uniquePaths(3,2))
