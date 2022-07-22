"""
kth-smallest-element-in-a-bst
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104

Question link https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        n = 0
        stack = []
        cur = root

        while cur and stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right
'''
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.cou = 1
        self.ksmall = None
        def inorder(node):
            if not node or self.ksmall:
                return
            inorder(node.left)
            if self.cou == k:
                self.ksmall = node.val
            self.cou += 1
            inorder(node.right)
        inorder(root)
        return self.ksmall