# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.

# 연결리스트를 뒤집어라
# 연결리스트를 뒤집는 문제는 매우 일반적이면서도 활용도가 높은 문제로, 실무에서도 빈번하게 쓰인다.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 1. 재귀 구조로 뒤집기
        #         def reverse(node: ListNode, prev: ListNode = None):
        #             if not node:
        #                 return prev

        #             # 다음노드 next와 현재노드 node를 파라미터로 지정한 함수를 계속해서 재귀호출한다.
        #             # node.next에는 이전 prev 리스트를 계속 연결해주면서 node가 None이 될 때까지 재귀호출하면
        #             # 마지막에는 백트래킹되면서 연결 리스트가 거꾸로 연결된다.
        #             # 맨 처음에 리턴된 prev는 뒤집힌 연결리스트의 첫번째 노드가 된다.
        #             next, node.next = node.next, prev
        #             return reverse(next, node)

        #         return reverse(head)

        # 2. 반복 구조로 뒤집기
        node, prev = head, None

        while node:
            n = node.next
            node.next = prev  # node.next를 이전 prev 리스트로 계속 연결하면서 끝날 때까지 반복.
            prev = node
            node = n
        # node가 None이 될 때, prev는 뒤집힌 리스트의 첫 번째 노드가 됨.
        return prev


# 27 / 27 test cases passed.
# Status: Accepted
# Runtime: 32 ms
# Memory Usage: 15.4 MB
#
# Your runtime beats 89.97 % of python3 submissions.
# Your memory usage beats 42.60 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.
