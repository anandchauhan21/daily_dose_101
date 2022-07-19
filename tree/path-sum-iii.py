"""
path-sum-iii
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

Constraints:
The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000

Question link https://leetcode.com/problems/path-sum-iii/
"""


# Definition for a binary tree node.
from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.total =0
        self.lookup = defaultdict(int)
        self.lookup[targetSum] = 1
        def dfs(node,root_sum):
            if not node:
                return
            root_sum += node.val
            self.total += self.lookup[root_sum]
            self.lookup[root_sum+targetSum] +=1
            dfs(node.left, root_sum)
            dfs(node.right,root_sum)
            self.lookup[root_sum+targetSum] -= 1
        dfs(root,0)
        return self.total


