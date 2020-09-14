# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
#
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
#
# Example 1:
#
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
# Example 2:
#
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL
#
#
# Constraints:
#
# The relative order inside both the even and odd groups should remain as it was in the input.
# The first node is considered odd, the second node even and so on ...
# The length of the linked list is between [0, 10^4].


# Definition for singly-linked list.

# 연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하라.
# 공간복잡도 O(1), 시간복잡도 O(n)에 풀이하라


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 홀(odd), 짝(even) 노드를 구성한 다음, 홀수 노드의 마지막을 짝수 노드의 처음과 이어준다
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        # 반복하면서 홀짝 노드 처리
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        # 홀수 노드의 마지막을 짝수의 헤드 even_head와 연결
        odd.next = even_head

        return head


# 71 / 71 test cases passed.
# Status: Accepted
# Runtime: 40 ms
# Memory Usage: 15.8 MB
#
# Your runtime beats 89.74 % of python3 submissions.
# Your memory usage beats 49.41 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.


