# Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.
#
# The length of path between two nodes is represented by the number of edges between them.
#
#
#
# Example 1:
#
# Input:
#
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output: 2
#
#
#
# Example 2:
#
# Input:
#
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output: 2
#
#
#
# Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result: int = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:

        def dfs(node: TreeNode):
            if node is None:
                return 0

            # 왼쪽, 오른쪽의 각 리프 노드까지 탐색. 존재하지 않는 노드까지 DFS 재귀 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 현재 노드가 자식 노드와 동일한 경우 거리 1 증가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0

            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # 왼쪽 자식과 오른쪽 자식 노드 간 거리의 합 최대값이 결과
            self.result = max(self.result, left + right)
            return max(left, right)

        dfs(root)
        return self.result


# Runtime: 444 ms, faster than 70.90% of Python3 online submissions for Longest Univalue Path.
# Memory Usage: 17.2 MB, less than 58.85% of Python3 online submissions for Longest Univalue Path.
# <파이썬 알고리즘 인터뷰> 참고.



