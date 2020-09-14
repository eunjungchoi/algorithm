# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more than 1.
#
# Example:
#
# Given the sorted array: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # 오름차순으로 정렬된 배열을 높이 균형 height balanced 이진 탐색 트리로 변환하라
        # 이 문제에서 높이 균형이란, 모든 노드의 두 서브 트리간 깊이 차이가 1 이하인 것을 말한다.

        # 이진 검색 결과로 트리 구성
        if not nums:
            return None

        mid = len(nums) // 2

        # 분할 정복으로 이진 검색 결과 트리 구성
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        return node


# 32 / 32 test cases passed.
# Status: Accepted
# Runtime: 92 ms
# Memory Usage: 16.1 MB
#
# Your runtime beats 28.88 % of python3 submissions.
# Your memory usage beats 50.08 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.
