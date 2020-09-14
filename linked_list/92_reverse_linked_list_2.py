# Reverse a linked list from position m to n. Do it in one-pass.
#
# Note: 1 ≤ m ≤ n ≤ length of list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL


# Definition for singly-linked list.

# 인덱스 m에서 n까지를 역순으로 만들어라. 인덱스 m은 1부터 시작한다.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 반복 구조로 노드 뒤집기
        root = start = ListNode(None)
        root.next = head

        # start, end 지정. 이렇게 할당된 start와 end는 끝까지 값이 변하지 않는다.
        for _ in range(m - 1):
            start = start.next  # start는 변경이 필요한 m의 바로 앞 지점을 가리키게 함

        end = start.next

        # 반복하면서 노드 차례대로 뒤집기
        # start.next (2)를 temp에 저장해둠.
        # start.next에는 end.next(3)가 들어온다   1.next 에 end(2)의 next인 3이 저장됨
        # end.next (원래 3)에는 end.next.next(4)가 저장됨
        # 그리고 start.next.next를  temp (2)를 저장.
        # 1 -> 3 -> 2 -> 4가 됐음.

        for _ in range(n - m):
            temp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = temp

        return root.next


# 44 / 44 test cases passed.
# Status: Accepted
# Runtime: 36 ms
# Memory Usage: 13.9 MB
#
# Your runtime beats 42.07 % of python3 submissions.
# Your memory usage beats 79.54 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.
