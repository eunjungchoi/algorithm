# Sort a linked list using insertion sort.
#
#
# A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
# With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
#
#
# Algorithm of Insertion Sort:
#
# Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
# It repeats until no input elements remain.
#
# Example 1:
#
# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:
#
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        curr = root = ListNode(0)   # curr에는 정렬을 끝낸 연결리스트를 추가해줌.  pa
        while head:
            while curr.next and curr.next.val < head.val:
                curr = curr.next

            curr.next, head.next, head = head, curr.next, head.next
            if head and curr.val > head.val:   # 꼭 필요한 경우에만 되돌아가게
                curr = root  # 다시 처음으로 되돌아가며 다시 비교

        return root.next


# 22 / 22 test cases passed.
# Status: Accepted
# Runtime: 164 ms
# Memory Usage: 15.7 MB
#
# Your runtime beats 89.43 % of python3 submissions.
# Your memory usage beats 71.50 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.
