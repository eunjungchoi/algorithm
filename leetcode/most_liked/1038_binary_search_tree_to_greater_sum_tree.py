# Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the sum of the values of the original tree that are greater than or equal to node.val.
#
# As a reminder, a binary search tree is a tree that satisfies these constraints:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
# Example 1:
#
#
#
# Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
#
#
# Constraints:
#
# The number of nodes in the tree is between 1 and 100.
# Each node will have value between 0 and 100.
# The given tree is a binary search tree.
# Note: This question is the same as 538: https://leetcode.com/problems/convert-bst-to-greater-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    val: int = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 중위 순회 노드 값 누적
        if root:
            self.bstToGst(root.right)
            self.val += root.val  # self.val : 지금까지 누적된 값
            root.val = self.val  # root.val: 현재 노드의 값
            self.bstToGst(root.left)

        return root


# 28 / 28 test cases passed.
# Status: Accepted
# Runtime: 32 ms
# Memory Usage: 14 MB
#
# Your runtime beats 72.55 % of python3 submissions.
# Your memory usage beats 7.86 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.
