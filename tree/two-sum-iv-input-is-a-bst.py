"""
two-sum-iv-input-is-a-bst
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.


Example 1:
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105

Question link https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l = set()
        def dfs(node):
            if not node:return False
            y = k -node.val
            if y in l:
                return True
            else:
                l.add(node.val)
            return dfs(node.left) or dfs(node.right)
        return dfs(root)


from collections import deque
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        queue, seen = deque([root]),set()
        while queue:
            cur = queue.popleft()
            if cur.val in seen:
                return True
            else:
                seen.add(k-cur.val)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
        return False