"""N-Queens
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints:
1 <= n <= 9

qustion link https://leetcode.com/problems/n-queens/
"""

from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDig = set() #(r+c)
        negDig = set() #(r-c)

        res = []
        board = [["."]* n for i in range(n)]
        def backtrack(r):
            if r ==n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r+c) in posDig or (r-c) in negDig:
                    continue
                col.add(c)
                posDig.add(r+c)
                negDig.add(r-c)
                board[r][c]= "q"
                backtrack(r+1)
                col.remove(c)
                posDig.remove(r+c)
                negDig.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res

x = Solution()
print(x.solveNQueens(4))

###out-put: [['.q..', '...q', 'q...', '..q.'], ['..q.', 'q...', '...q', '.q..']]
