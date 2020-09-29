# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# Example 1:
#
# Input: 1->1->2
# Output: 1->2
# Example 2:
#
# Input: 1->1->2->3->3
# Output: 1->2->3


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # sorted linked list (앞뒤가 같은 값인지 비교)

        curr = head
        while curr:
            while curr.next and curr.next.val == curr.val:  # curr.next 가 curr와 다를 때까지 curr.next를 업데이트
                curr.next = curr.next.next
            curr = curr.next
        return head


# 165 / 165 test cases passed.
# Status: Accepted
# Runtime: 40 ms
# Memory Usage: 14.2 MB
#
# Your runtime beats 83.80 % of python3 submissions.
