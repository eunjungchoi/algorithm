# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# Example:
#
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
#
# Note:
#
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    링크드 리스트가 주어진다.
    링크드 리스트 k의 노드를 한 번에 역방향으로 변경하고 수정된 목록을 반환하라.

    k는 양의 정수이며 링크된 리스트의 길이보다 작거나 같다. 노드 수가 k의 배수가 아닐 경우, 결국 좌회전 노드는 그대로 유지되어야 한다.

    참고:
    상수 단위의 추가 메모리만 허용된다.
    목록의 노드에서 값을 변경할 수 없으며 노드 자체만 변경할 수 있다.


    솔루션:
    어떤 추가 공간도 사용하지 말라고 언급한다. 재귀 스택이 사용하는 공간 때문에 재귀 솔루션은 허용되지 않는다. 다만 반복적 접근으로 넘어가기 전에 재귀적 접근을 먼저 검토한다.

    linked list는 재귀적 구조이다.

    k 노드로 구성된 리스트를 거꾸로 뒤집는 것은 단순히 <linked list reversal> 알고리즘일 뿐이다.
    링크드 리스트 traversal와  초기 삽입을 결합하는 방식.

    - head 라는 출발 노드가 있다.
    - reversed linked list의 헤드가 될 다른 포인터를 설정한다. rev_head.
    - 원래 리스트를 가로지르기 위해 포인터를 사용한다.
    - 모든 요ㅛ소에 대해, rev_head를 head로 하는 reverse list의 시작 부분에 삽입. pointer를 계속 한 칸 앞으로 나아가고,  리버스 리스트의 시작 부분에 계속 삽입하면서  결국 전체 리스트를 뒤집기

    이 방법을 활용해 k 노드를 뒤집는 문제를 풀 수 있다.
    이때 문제에서  < k nodes 가 남아있다면 굳이 되돌릴 필요가 없다고 한다.  곧  reversal를 시작하기 전에 k개 노드를 세야 한다는 것. 어느 시점에서든 k 노드가 없다는 것을 알게 되면 링크드 리스트의 해당 부분을 되돌리지 않는다. 곧 두번의 travesal을 의미한다. 하나는 세는 용. 하나는 reversal 용.

    1. 재귀 알고리즘.
    이 문제는 링크드 리스트의 고정된 구간에 대해 한번에 한 부분씩 수정 작업을 요하기 때문에 재귀적 접근은 적합하다. 링크드 리스트의 하위 리스트는 그 자체로 링크드 리스트이기 때문이다.

    재귀 역추적 (backtrack)으로서,  올바르게 연결할 필요가 있다.  만약 1, 2, 3, 4, 5 의 링크드 리스트가 재공되고 한번에 2개의 노드를 되돌려야 한다고 할때,  재귀적 접근에서는 먼저 처음 두개를 반대로 해서 2, 1을 얻는다. 역추적을 반복할 때 4, 3, 5를 얻게 된다. 이때 1과 4를 정확히 연결해야 한다.


    *** 알고리즘 ***
    1. reverse() 함수가 정의되어 있다고 할 때, 이 함수는 링크드 리스트의 head와 k를 받는다. 링크드 리스트의 끝까지 reverse할 필요는 없다. 오직 k 노드만이 한번에 처리된다.
    2. 모든 재귀 호출 시  먼저 연결된 목록에 있는 노드 수를 계산한다. count가 K 개가 되면 break.
    3. k개 미만의 노드가 남아있으면 list의 head를 반환한다.
    4. 그러나 적어도 k개 노드가 남아있을 경우,  첫번째에서 정의된 reverse() 함수를 호출한다.
    5. 우리의 재귀 함수는 reversed linked list의 head를 반환해야 한다. 이는 함수에 전달된 리스트의 k 번째 노드이다. 모든 반전이 끝난 뒤 k번째 노드가 새로운 head가 되기 때문이다.
    6. 모든 재귀 호출에서, 먼저 k 노드를 reverse 한 후,  나머지 linked list에서 반복한다. 재귀가 돌아오면, 적절히 연결한다.


    """

    def reverseLinkedList(self, head: ListNode, k: int) -> ListNode:
        new_head = None
        curr = head  # p : pointer

        while k:
            # keep track of the next node to process in the original list
            next = curr.next  # 다음 노드의 레퍼런스를 따로 next 변수에 담아놓음

            # insert the node pointed to by pointer
            # at the beginning of the reversed list
            curr.next = new_head  # curr의 next 레퍼런스로 new_head가 들어감.
            new_head = curr  # curr 가 새로운 new_head가 됨. 한발짝 왼쪽으로 온 것.

            # move to next node
            curr = next  # next 노드가 담겨있던 레퍼런스가 새로운 curr가 됨.
            k -= 1

        # return the head of the reversed list
        return new_head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count = 0
        p = head

        while count < k and p:
            p = p.next
            count += 1

        if count == k:
            reversed_head = self.reverseLinkedList(head, k)

            # now, recurse on the remaining linked list.
            # to re-wire the connections.
            head.next = self.reverseKGroup(p, k)
            return reversed_head

        return head


# 62 / 62 test cases passed.
# Status: Accepted
# Runtime: 48 ms
# Memory Usage: 15.1 MB
#
# Your runtime beats 83.35 % of python3 submissions.
# Your memory usage beats 8.54 % of python3 submissions.
