# Given a reference of a node in a connected undirected graph.
#
# Return a deep copy (clone) of the graph.
#
# Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
#
# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
#
#
# Test case format:
#
# For simplicity sake, each node's value is the same as the node's index (1-indexed). For example, the first node with val = 1, the second node with val = 2, and so on. The graph is represented in the test case using an adjacency list.
#
# Adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
#
# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.
#
#
#
# Example 1:
#
#
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

# Example 2:
#
#
# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list.
# The graph consists of only one node with val = 1 and it does not have any neighbors.

# Example 3:
#
# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.
# Example 4:
#
#
# Input: adjList = [[2],[1]]
# Output: [[2],[1]]
#
#
# Constraints:
#
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# Number of Nodes will not exceed 100.
# There is no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given node.

# Definition for a Node.


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    # 1. DFS recursively
    # def cloneGraph(self, node: 'Node') -> 'Node':
    #     if not node:
    #         return node
    #     memo = {node: Node(node.val)}
    #     self.dfs(node, memo)
    #     return memo[node]
    #
    # def dfs(self, node, memo):
    #     for neighbor in node.neighbors:
    #         if neighbor not in memo:
    #             memo[neighbor] = Node(neighbor.val)
    #             self.dfs(neighbor, memo)
    #         memo[node].neighbors.append(
    #             memo[neighbor])  # 그냥 neighbor가 아니라, memo에 있는 neighbor를 append 해줘야 함. 그래야  reference가 아닌 deepcopy가 됨.

    # 2. DFS iteratively
    def cloneGraph(self, node):
        if not node:
            return node

        memo = {node: Node(node.val)}
        stack = [node]

        while stack:
            item = stack.pop()
            for neighbor in item.neighbors:
                if neighbor not in memo:
                    memo[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                memo[item].neighbors.append(memo[neighbor])

        return memo[node]

# 21 / 21 test cases passed.
# Status: Accepted

# DFS recursively
# Runtime: 40 ms
# Memory Usage: 14 MB
# Your runtime beats 64.94 % of python3 submissions.
# Your memory usage beats 73.37 % of python3 submissions.


# DFS iteratively
# Runtime: 40 ms
# Memory Usage: 13.8 MB
# Your runtime beats 64.94 % of python3 submissions.
# Your memory usage beats 98.85 % of python3 submissions.
