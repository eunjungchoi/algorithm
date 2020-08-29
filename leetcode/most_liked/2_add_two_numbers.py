# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        prev = head

        carry = 0
        while l1 or l2 or carry:
            new_val = 0
            if l1:
                new_val += l1.val
                l1 = l1.next
            if l2:
                new_val += l2.val
                l2 = l2.next

            carry, new_val = divmod(carry + new_val, 10)

            prev.next = ListNode(val=new_val)
            prev = prev.next

        return head.next


# 1563 / 1563 test cases passed.
# Status: Accepted
# Runtime: 68 ms
# Memory Usage: 13.7 MB
#
# Your runtime beats 92.41 % of python3 submissions.
# Your memory usage beats 90.68 % of python3 submissions.
