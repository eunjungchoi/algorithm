# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
#
# But the following [1,2,2,null,3,null,3] is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
#
# Follow up: Solve it both recursively and iteratively.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if not left and not right:
                continue

            if left is None or right is None:
                return False

            if left.val != right.val:
                return False

            stack.append((left.left, right.right))
            stack.append((left.right, right.left))

        return True


# 195 / 195 test cases passed.
# Status: Accepted
# Runtime: 32 ms
# Memory Usage: 14.2 MB
#
# Your runtime beats 82.09 % of python3 submissions.
# Memory Usage: 14.2 MB, less than 5.08% of Python3 online submissions for Symmetric Tree.
