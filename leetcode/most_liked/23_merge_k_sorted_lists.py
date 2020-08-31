# Given an array of linked-lists lists, each linked list is sorted in ascending order.
#
# Merge all the linked-lists into one sort linked-list and return it.
#
#
#
# Example 1:
#
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:
#
# Input: lists = []
# Output: []
# Example 3:
#
# Input: lists = [[]]
# Output: []


# Definition for singly-linked list.
import heapq
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
                # 각 연결리스트의 루트를 heap에 저장

        while heap:
            node = heapq.heappop(heap)  # 제일 값이 작은 노드가 나옴.
            idx = node[1]  # lists에서 list의 index. node=(노드의 값, 인덱스, 노드)
            result.next = node[2]  # 각 연결리스트의 root 노드를 result 노드의 next에 저장
            result = result.next  # 해당 연결리스트의 root 노드로 이동

            if result.next:  # root 노드에 next 노드가 있으면 heap에 집어넣음. 연결리스트의 인덱스는 그대로 넣어줌.
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next


# 131 / 131 test cases passed.
# Status: Accepted
# Runtime: 112 ms
# Memory Usage: 17.6 MB
#
# Your runtime beats 77.45 % of python3 submissions.
# Your memory usage beats 51.40 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.
