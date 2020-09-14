# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
# Input: 1->2
# Output: false
# Example 2:
#
# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.

# 연결리스트가 팰린드롬 구조인지 판별하라.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        if not head:
            return True

        # 1. 리스트로 변환
        #         array = []
        #         while head:
        #             array.append(head.val)
        #             head = head.next
        #         return array == array[::-1]

        # 2. 빠른 runner, 느린 runner를 이용한 풀이

        # 빠른 러너와 느린 러너를 각각 출발시키면, 빠른 러너가 끝에 다다를 때 느린 러너는 정확히 중간 지점에 도달.
        # 느린 러너는 중간까지 이동하면서 역순으로 연결 리스트 rev를 만들어나감.
        # 중간에 도달한 느린 러너가 나머지 경로를 이동할 때 역순으로 만든 연결 리스트의 값들과 일치하는지 확인

        fast = slow = head
        reverse = None

        # 러너를 이용해 역순 연결리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            reverse, reverse.next, slow = slow, reverse, slow.next
            # 역순 연결리스트는 현재 값을 slow로 교체하고 rev.next는 rev가 된다.
            # 앞에 계속 새로운 노드가 추가되는 형태
            # reverse는 slow의 역순 연결리스트가 됨.

        if fast:  # 입력값이 홀수일 때는 slow 러너가 한 칸 더 앞으로 이동해서 중앙값을 벗어나야 함.
            # 중앙값은 팰린드롬 체크에서 배제되어야 하기 때문에
            # 이는 곧 fast가 아직 none이 아닌 경우와 같음. 이때는 slow 한 칸 더 이동.
            slow = slow.next

            # 팰린드롬 여부 체크
        while reverse and reverse.val == slow.val:
            slow, reverse = slow.next, reverse.next

        return not reverse  # 정상적으로 비교가 종료됐으면 slow와 rev 둘다 none이 되어야 함.


# 26 / 26 test cases passed.
# Status: Accepted
# Runtime: 68 ms
# Memory Usage: 23.9 MB
#
# Your runtime beats 88.54 % of python3 submissions.
# Your memory usage beats 82.04 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.
