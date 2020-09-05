# Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.
#
# Example :
#
# Input: root = [4,2,6,1,3,null,null]
# Output: 1
# Explanation:
# Note that root is a TreeNode object, not an array.
#
# The given tree [4,2,6,1,3,null,null] is represented by the following diagram:
#
#           4
#         /   \
#       2      6
#      / \
#     1   3
#
# while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
# Note:
#
# The size of the BST will be between 2 and 100.
# The BST is always valid, each node's value is an integer, and each node's value is different.
# This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/


# Definition for a binary tree node.
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    prev = -sys.maxsize
    result = sys.maxsize

    def minDiffInBST(self, root: TreeNode) -> int:
        # 재귀 구조 중위 순회 비교 결과

        if root.left:
            self.minDiffInBST(root.left)

        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.result

        # recursive

        # prev = -sys.maxsize
        # result = sys.maxsize

#         stack = []
#         node = root

#         # 반복 구조 중위 순회 비교 결과
#         while stack or node:
#             while node:
#                 stack.append(node)
#                 node = node.left

#             node = stack.pop()

#             result = min(result, node.val - prev)
#             prev = node.val
#             node = node.right

#         return result

# 45 / 45 test cases passed.
# Status: Accepted
# Runtime: 28 ms
# Memory Usage: 13.8 MB
#
# Your runtime beats 92.10 % of python3 submissions.
# Your memory usage beats 84.48 % of python3 submissions.
# 파이썬 알고리즘 인터뷰. 참고.

