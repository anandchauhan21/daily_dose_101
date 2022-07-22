"""
partition-list
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]

Constraints:
The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200

Question list https://leetcode.com/problems/partition-list/
"""

### Solution

# make two dummy node left and righr and two tail Variable that take care of the botha left and right tail
# Nov check if the value of node is greater than or less than "x".
# if less than x the add it to the left tail and increment the ltail
# else add it to the right tail and increment the rtail
# Increment the head.
# After the loop point left tail to right.next because it is the head of right list
# point right tail to None that will be last node of the list
# return the left head by left.next because "left" is dummy node

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()
        ltail, rtail = left, right
        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
            head = head.next
        ltail.next = right.next
        rtail.next = None
        return left.next
