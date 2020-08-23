# Merge two sorted linked lists and return it as a new sorted list.
# The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1

        result = ListNode()
        if l1.val <= l2.val:
            result.val = l1.val
            l1 = l1.next
        else:
            result.val = l2.val
            l2 = l2.next

        prev = result
        while l1 or l2:
            if not l1:
                prev.next = ListNode(val=l2.val)
                l2 = l2.next
            elif not l2:
                prev.next = ListNode(val=l1.val)
                l1 = l1.next
            elif l1.val <= l2.val:
                prev.next = ListNode(val=l1.val)
                l1 = l1.next
            else:
                prev.next = ListNode(val=l2.val)
                l2 = l2.next
            prev = prev.next

        return result


