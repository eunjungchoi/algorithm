# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
# Example 2:
#
# Input: n = 1, k = 1
# Output: [[1]]
#
#
# Constraints:
#
# 1 <= n <= 20
# 1 <= k <= n
import itertools
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # return list(itertools.combinations(range(1, n + 1), k))

        results = []

        def dfs(elements, start, k):
            if k == 0:
                results.append(elements[:])

            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()

        dfs([], 1, k)

        return results

# n = 4, k = 2
# dfs([], 1, 2)
# i in range(1, 5)
# elements = [1]
# dfs([1], 2, 1)
# i in range(2, 5)
# elements = [1, 2]
# dfs([1, 2], 3, 0)
# results.append([1, 2])
#
# i in range(3, 5)
# elements.append(3)
# elements = [1, 2, 3]
# dfs([1, 2, 3], 4, -1)
# i in range(4, 5)
# elements.append(4)
# elements = [1, 2, 3, 4]
# dfs([1, 2, 3,4], 5, -2)
#
# elements.pop()
# elements = [1, 2, 3]
# elements.pop()
# elements = [1, 2]
# ...
# elements.pop()
# elements = [1]
# i = 3
# elements = [1, 3]


# 27 / 27 test cases passed.
# Status: Accepted
# Runtime: 68 ms
# Memory Usage: 15 MB
#
# using itertools
# Your runtime beats 99.91 % of python3 submissions.
# Your memory usage beats 92.19 % of python3 submissions.

# using DFS
# Your runtime beats 68.67 % of python3 submissions.
# Your memory usage beats 84.93 % of python3 submissions.
