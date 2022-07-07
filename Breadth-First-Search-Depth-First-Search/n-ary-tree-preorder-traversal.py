"""
n-ary-tree-preorder-traversal
"""
from collections import deque
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output = []
        def dfs(node):
            if not node: return
            output.append(node.val)
            for c in node.children:
                dfs(c)
        dfs(root)
        return output

###solution 2
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        q = deque([root])
        output = []
        while q:
            cand = q.popleft()
            output.append(cand.val)
            for c in reversed(cand.children):
                q.appendleft(c)
        return output