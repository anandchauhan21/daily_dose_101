from contextlib import redirect_stderr
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if not root: return res
        stack = [[root, [root.val]]]
        while len(stack) > 0:
            node, path = stack.pop()
            if not node.left and not node.right and sum(path) == targetSum:
                res.append(path)
            if node.righ:
                stack.append([node.right,path+[node.right.val]])
            if node.left:
                stack.append([node.left,path+[node.left.val]])

        return res