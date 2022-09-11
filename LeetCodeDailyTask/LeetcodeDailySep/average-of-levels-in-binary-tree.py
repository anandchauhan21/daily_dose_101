"""
average-of-levels-in-binary-tree
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:


Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1

Question link https://leetcode.com/problems/average-of-levels-in-binary-tree/
"""
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # BFS solution
        quene = []  # we use first in first out quene for Breadth-First-search
        res = []
        quene.append(root)
        
        while(quene):   # loop through every level
            qlen = len(quene)   # how many elements in the current row
            tmp = 0
            for i in range(qlen):   # loop through elements in current level
                node = quene.pop(0)
                tmp += node.val
                if node.left:   
                    quene.append(node.left)
                if node.right:
                    quene.append(node.right)
            res.append(tmp/qlen)    # calculate the average 
        
        return res
