# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        queue = collections.deque([root])  # 데크로 선언  (이중 연결 리스트. 양방향 모두 O(1)에 추출)
        depth = 0

        # 반복 구조 구성
        while queue:
            depth += 1
            # 큐연산 추출 노드의 자식 노드 삽입
            for _ in range(len(queue)):
                current_root = queue.popleft()

                if current_root.left:  # 자식 노드 있는지 판별 후
                    queue.append(current_root.left)  # 자식 노드를 큐에 삽입
                if current_root.right:
                    queue.append(current_root.right)

        # BFS 반복 횟수 = 깊이
        return depth


# 39 / 39 test cases passed.
# Status: Accepted
# Runtime: 40 ms
# Memory Usage: 15 MB
#
# Your runtime beats 85.11 % of python3 submissions.
# Your memory usage beats 88.04 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.

