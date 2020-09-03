# Invert a binary tree.
#
# Example:
#
# Input:
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

# Trivia:
# This problem was inspired by this original tweet by Max Howell:
#
# Google: 90% of our engineers use the software you wrote (Homebrew),
# but you can’t invert a binary tree on a whiteboard so f*** off.

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            # 부모 노드부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)

        return root


# 68 / 68 test cases passed.
# Status: Accepted
# Runtime: 24 ms
# Memory Usage: 13.6 MB
#
# Your runtime beats 95.44 % of python3 submissions.
# Your memory usage beats 93.52 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.
