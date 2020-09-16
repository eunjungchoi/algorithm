# You are given a binary tree in which each node contains an integer value.
#
# Find the number of paths that sum to a given value.
#
# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
#
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
#
# Example:
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
#
# Return 3. The paths that sum to 8 are:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11


#          1 High level walk through
# In order to optimize from the brutal force solution,
# we will have to think of a clear way to memorize the intermediate result.
# Namely in the brutal force solution, we did a lot repeated calculation.
# For example 1->3->5, we calculated: 1, 1+3, 1+3+5, 3, 3+5, 5.
# This is a classical 'space and time tradeoff':
# we can create a dictionary (named cache) which saves all the path sum (from root to current node) and their frequency.
# Again, we traverse through the tree,
# at each node, we can get the currPathSum (from root to current node).
# If within this path, there is a valid solution,
# then there must be a oldPathSum such that currPathSum - oldPathSum = target.
# We just need to add the frequency of the oldPathSum to the result.
# During the DFS break down, we need to -1 in cache[currPathSum], because this path is not available in later traverse.
# Check the graph below for easy visualization.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # define global result
    result = 0

    def pathSum(self, root: TreeNode, target: int) -> int:
        cache = {0: 1}

        currPathSum = 0
        # recursive to get result

        self.dfs(root, target, currPathSum, cache)
        return self.result

    def dfs(self, root, target, currPathSum, cache):
        # exit condition
        if root is None:
            return

        # calculate currPathSum and required oldPathSum
        currPathSum += root.val  # 윗 노드에서부터 내려온 sum에 현재 노드의 val을 더함.
        oldPathSum = currPathSum - target  # root부터 currentNode까지의 합에서 target을 뺀 나머지 숫자.

        # update result and cache

        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1

        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)

        # when move to a different branch, the currPathSum is no longer available, hence remove one.
        cache[currPathSum] -= 1


# 126 / 126 test cases passed.
# Status: Accepted
# Runtime: 44 ms
# Memory Usage: 14.5 MB
#
# Your runtime beats 96.17 % of python3 submissions.
# Your memory usage beats 91.52 % of python3 submissions.


