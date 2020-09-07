# # merge sort
#
#
# Sort a linked list in O(n log n) time using constant space complexity.
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


# using merge sort
class Solution:
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     if l1 and l2:
    #         if l1.val > l2.val:
    #             l1, l2 = l2, l1
    #         l1.next = self.mergeTwoLists(l1.next, l2)
    #
    #     return l1 or l2
    #
    # def sortList(self, head: ListNode) -> ListNode:
    #     if not (head and head.next):
    #         return head
    #
    #     # 런너 기법 활용
    #     half, slow, fast = None, head, head
    #     while fast and fast.next:
    #         half, slow, fast = slow, slow.next, fast.next.next
    #
    #     half.next = None
    #
    #     # 분할 재귀 호출
    #     l1 = self.sortList(head)
    #     l2 = self.sortList(slow)
    #
    #     return self.mergeTwoLists(l1, l2)

    def sortList(self, head: ListNode) -> ListNode:
        # 연결리스트 -> 파이썬 List
        pointer = head
        list_ = []

        while pointer:
            list_.append(pointer.val)
            pointer = pointer.next

        # 정렬
        list_.sort()

        # 파이썬 리스트 -> 연결리스트
        pointer = head
        for i in range(len(list_)):
            pointer.val = list_[i]
            pointer = pointer.next

        return head


# sort() 내장 함수 이용
# Runtime: 88 ms, faster than 98.81% of Python3 online submissions for Sort List.
# Memory Usage: 21.2 MB, less than 99.81% of Python3 online submissions for Sort List.

# merge sort 활용
# Runtime: 276 ms
# Memory Usage: 40.3 MB
# Your runtime beats 45.33 % of python3 submissions.
# Your memory usage beats 6.39 % of python3 submissions.

