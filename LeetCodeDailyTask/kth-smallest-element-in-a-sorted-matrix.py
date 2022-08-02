"""
kth-smallest-element-in-a-sorted-matrix
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).



Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5


Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2

Question link https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
"""
from bisect import bisect_right
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l, r, N = matrix[0][0], matrix[-1][-1], len(matrix)

        def helper(m):
            cnt = 0
            for i in range(N):
                x = bisect_right(matrix[i], m)
                cnt += x
            return cnt

        while l < r:
            mid = (l + r) // 2
            if helper(mid) < k:
                l = mid + 1
            else:
                r = mid
        return l


x = Solution()
print(x.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
