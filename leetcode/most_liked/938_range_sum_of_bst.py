# Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
#
# The binary search tree is guaranteed to have unique values.
#
#
#
# Example 1:
#
# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32
# Example 2:
#
# Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# Output: 23
#
#
# Note:
#
# The number of nodes in the tree is at most 10000.
# The final answer is guaranteed to be less than 2^31.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        # recursive
        def dfs(node: TreeNode):
            if not node:
                return 0

            if node.val < L:
                return dfs(node.right)
            elif node.val > R:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)


        # iterative

#         sum = 0
#         stack = [root]

#         while stack:
#             node = stack.pop()
#             if node:
#                 if node.val > L:
#                     stack.append(node.left)
#                 if node.val < R:
#                     stack.append(node.right)

#                 if L <= node.val <= R:
#                     sum += node.val

#         return sum

# 42 / 42 test cases passed.
# Status: Accepted
# Runtime: 224 ms
# Memory Usage: 22 MB
#
# Your runtime beats 94.37 % of python3 submissions.
# Your memory usage beats 29.43 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.

