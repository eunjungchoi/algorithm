# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
#
# Note: The length of path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    longest: int = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1

            # 상태값 : 리프 노드에서 현재 노드까지의 거리
            # 거리: 왼쪽 자식 노드의 상태값 + 오른쪽 자식 노드의 상태값 + 2
            # 가장 밑단의 존자하지 않는 자식 노드에 -1 씩을 부여함

            # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
            left = dfs(node.left)  # 자식노드가 하나도 없는 경우 left, right 모두 -1. 이때 거리는 0, 상태도 0.
            right = dfs(node.right)

            # 가장 긴 경로 업데이트
            self.longest = max(self.longest, left + right + 2)  # 최종 결과가 될 가장 긴 경로. 거리는 왼쪽, 오른쪽 자식 사이의 경로이므로 2를 더함.

            # 해당 노드의 상태값을 반환.
            return max(left, right) + 1  # 상태값. 양쪽 자식 중 최대 상태값과 부모까지의 거리인 1을 더함.

        dfs(root)
        return self.longest


# 106 / 106 test cases passed.
# Status: Accepted
# Runtime: 40 ms
# Memory Usage: 15.8 MB
#
# Your runtime beats 94.28 % of python3 submissions.
# Your memory usage beats 52.05 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.
