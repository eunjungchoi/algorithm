# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example:
#
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dynamic programming

        dp = [[0] * (len(grid[0]) + 1) for _ in range(len(grid) + 1)]

        for i in range(1, len(grid) + 1):
            for j in range(1, len(grid[0]) + 1):
                if i == 1:
                    dp[i][j] = dp[i][j - 1] + grid[i - 1][j - 1]
                elif j == 1:
                    dp[i][j] = dp[i - 1][j] + grid[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]

        return dp[-1][-1]


# 61 / 61 test cases passed.
# Status: Accepted
# Runtime: 100 ms
# Memory Usage: 15.4 MB
#
# Your runtime beats 84.16 % of python3 submissions.
# Your memory usage beats 53.50 % of python3 submissions.
