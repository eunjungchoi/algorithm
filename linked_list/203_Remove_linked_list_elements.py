# Remove all elements from a linked list of integers that have value val.
#
# Example:
#
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5

# 정수들의 링크드 리스트 에서 주어진 값과 동일한 값을 가진 모든 요소를 제거하라.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    중간 노드를 삭제하는 것은 쉽다. prev node의 next에  현재 노드의 next를 대입한다

    삭제할 노드가 head node이면 복잡해진다.
    * sentinel node 사용하기 : 센티넬 노드는 의사head, 의사 tail, level end 마커 등으로 tree와 linked list에서 널리 쓰인다. 순전히 기능적이며 대개 어떤 데이터도 저장하지 않는다. 주된 목적은 링크드 리스트를 절대 비워두지 않고 head도 비우지 않고 삽입과 삭제를 단순화하는 것이다.

    sentinel node를 listNode(0)으로 시작하고,  sentinel.next = head로 설정
    curr 노드와 prev 노드 의 두개의 포인터를 사용.

    """

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head

        root = ListNode(0)
        root.next = head
        prev = root
        current = head  # current가 먼저 출발해서 값 비교. prev가 한박자 뒤에서 링크 연결 조작.

        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next

        return root.next

# 65 / 65 test cases passed.
# Status: Accepted
# Runtime: 56 ms
# Memory Usage: 16.9 MB
#
# Your runtime beats 99.71 % of python3 submissions.
# Your memory usage beats 49.91 % of python3 submissions.







