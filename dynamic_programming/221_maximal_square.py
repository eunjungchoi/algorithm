# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
#
# Example:
#
# Input:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Output: 4
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dynamic programming, memoization
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        max_side = 0

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == '1':
                    dp[row + 1][col + 1] = min(dp[row][col], dp[row + 1][col], dp[row][col + 1]) + 1
                    max_side = max(max_side, dp[row + 1][col + 1])

        return max_side * max_side


# 73 / 73 test cases passed.
# Status: Accepted
# Runtime: 200 ms
# Memory Usage: 14.7 MB
#
# Your runtime beats 84.68 % of python3 submissions.
# Your memory usage beats 27.64 % of python3 submissions.
# time complexity: O(mn)
# space complexity: O(mn)
