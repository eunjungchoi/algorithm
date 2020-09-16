# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
#
#
# Example 1:
#
# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
# Example 2:
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
#
#
#
# Constraints:
#
# The number of elements of the BST is between 1 to 10^4.
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 1. recursive inorder traversal
        # 중위순회하면서 오름차순으로 정렬하기
        # def inorder(root) -> List:
        #     return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        #
        # return inorder(root)[k - 1]

        # 2. iterative  (using stack)
        # 제일 왼쪽 leaf로 이동해서 while문으로 k번 루프를 돌면서 다음(=오른쪽) 노드를 찾기
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left  # 제일 왼쪽 leaf로 이동

            root = stack.pop()

            k -= 1  # k번 루프를 돌면서 1씩 감소
            if k == 0:
                return root.val

            # 다음으로 큰 노드 찾기?
            root = root.right  # 오른쪽 노드로 이동해서 다시 왼쪽 leaf 로 파고들어갈 준비


# 1. recursive
# - time complexity : O(N) to build a traversal.
# - space complexity: O(N) to keep an inorder traversal.

# Your runtime beats 46.10 % of python3 submissions.
# Your memory usage beats 35.84 % of python3 submissions.


# 2. iterative - stack
# - time complexity : O(H + k)  , where H is a tree height
# - space complexity: O(H) , where H is a tree height.


# 91 / 91 test cases passed.
# Status: Accepted
# Runtime: 64 ms
# Memory Usage: 17.9 MB
#
# Your runtime beats 33.56 % of python3 submissions.
# Your memory usage beats 19.11 % of python3 submissions.
