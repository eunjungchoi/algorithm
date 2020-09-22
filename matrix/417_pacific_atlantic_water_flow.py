# Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.
#
# Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.
#
# Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.
#
# Note:
#
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
#
#
# Example:
#
# Given the following 5x5 matrix:
#
#   Pacific ~   ~   ~   ~   ~
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * Atlantic
#
# Return:
#
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
import collections
from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # 예외 처리
        if not matrix:
            return []

        rows = len(matrix)
        cols = len(matrix[0])

        def bfs(ocean):
            deque = collections.deque(ocean)

            while deque:
                i, j = deque.popleft()

                for I, J in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                    # i, j의 동서남북 셀이 i,j 보다 큰 값이면 ocean에 추가함.
                    if 0 <= I < rows and 0 <= J < cols and (I, J) not in ocean and matrix[I][J] >= matrix[i][j]:
                        ocean.add((I, J))
                        deque.append((I, J))

            return ocean

        pacific = set([(i, 0) for i in range(rows)] + [(0, j) for j in range(cols)])
        atlantic = set([(i, cols - 1) for i in range(rows)] + [(rows - 1, j) for j in range(cols)])

        return list(
            bfs(pacific) &
            bfs(atlantic)
        )


# 113 / 113 test cases passed.
# Status: Accepted
# Runtime: 300 ms
# Memory Usage: 15.2 MB
#
# Your runtime beats 76.05 % of python3 submissions.
# Your memory usage beats 44.11 % of python3 submissions.
