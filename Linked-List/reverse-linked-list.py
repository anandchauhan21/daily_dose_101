"""
reverse-linked-list
Given the head of a singly linked list, write a program to reverse the linked list,
and return the head pointer to the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

qustion link https://leetcode.com/problems/reverse-linked-list/
"""
import typing
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    # function to add elements to linked list
    def append(self, data):
        # if linked list is empty then last_node will be none so in if condition head will be created
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        # adding node to the tail of linked list
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    # function to print the content of linked list
    def display(self):
        current = self.head
        # traversing the linked list
        while current is not None:
            # at each node printing its data
            print(current.data, end=' ')
            # giving current next node
            current = current.next
        print()


class Solution:
    def reverseList(self, head: typing.Optional[Node]) -> typing.Optional[Node]:
        curr = head
        prev = None
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        return prev

x= Solution()
list1 =[1,2,3,4,5]
l = LinkedList
for i in range(len(list1)):
    print(list1[i])
    l.append(1)
print(x.reverseList(l))
### T(n) ,M(1)
len(list1)


