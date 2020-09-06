# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            # 전위 순회 첫번째 결과를 가져와 중위 순회를 분할하는 인덱스로 한다
            index = inorder.index(preorder.pop(0))  # 큐 연산

            # 이 값을 현재 노드로 구성.
            # 이를 기준으로 중위 순회 결과를 쪼개서  왼쪽, 오른쪽으로 각각 마무리될 때 분할 정복 구조로 재귀 호출
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index + 1:])

            return node


# Runtime: 144 ms, faster than 60.80% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
# Memory Usage: 52.2 MB, less than 46.36% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
# <파이썬 알고리즘 인터뷰> 참고.
