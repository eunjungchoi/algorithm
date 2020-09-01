# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
#
#
# Example:
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            node = head.next
            head.next = self.swapPairs(node.next)
            node.next = head
            return node
        return head


# 55 / 55 test cases passed.
# Status: Accepted
# Runtime: 32 ms
# Memory Usage: 13.8 MB
#
# Your runtime beats 72.51 % of python3 submissions.
# Your memory usage beats 62.98 % of python3 submissions.
