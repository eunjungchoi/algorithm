# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
# Example:
#
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

from collections import deque


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # the problem is to return a list of last elements from all levels,
        # so it's the way more natural to implement BFS here.
        # Time complexity is ths same O(N) both for DFS and BFS since one has to visit all nodes.
        # space complexity is O(D) for BFS, where D is a tree diameter.
        # O(N) space in the worst-case scenarioss: complete tree for BFS.

        # BFS implementation
        # push the root into the queue
        # pop out a node from the left
        # push the left child into the queue, and then push the right child.
        # 3 BFS approaches
        # 1. two queues, one for the previous level and one for the current.
        # 2. one queue with sentinel to mark the end of the level
        # 3. one queue + level size measurement

        # 1) BFS: two queues.

        if root is None:
            return []

        next_level = deque([root, ])
        rightside = []

        while next_level:
            curr_level = next_level
            next_level = deque()

            while curr_level:
                node = curr_level.popleft()
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            rightside.append(node.val)

        return rightside

    def rightSideView2(self, root: TreeNode) -> List[int]:
        # 2) BFS: One queue + sentinel

        # to push all the nodes in one queue and to use a sentinel node to separate the levels.
        # Typically, one could use null as a sentinel.

        # the first step is to initiate the first level: root + null as a sentinel.
        # Once it's done, continue to pop the nodes one by one from the left and push their children to the right.
        # Stop each time the current node is null because it means we his the end of the current level.
        # Each stop is a time to update a right side view list and
        # to push null in the queue to mark the end of the next level.

        if root is None:
            return []

        queue = deque([root, None, ])
        rightside = []

        curr = root
        while queue:
            prev, curr = curr, queue.popleft()

            while curr:
                # add child nodes in the queue.
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

                prev, curr = curr, queue.popleft()

            rightside.append(prev.val)
            if queue:
                queue.append(None)

        return rightside

# 211 / 211 test cases passed.
# Status: Accepted
# Runtime: 32 ms
# Memory Usage: 13.9 MB
#
# Your runtime beats 73.41 % of python3 submissions.
# Your memory usage beats 46.88 % of python3 submissions.
