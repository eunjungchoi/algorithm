# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
#
#
# Example 1:
#
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:
#
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
from typing import List


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def dfs(i: int, j: int):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':  # 더이상 땅이 아니면 종료
                return

            # 육지였던 곳을 물로 바꿔줌
            grid[i][j] = '0'

            # 동서남북 탐색
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':  # 육지를 발견하면
                    dfs(i, j)  # 거기서 동서남북으로 깊이-우선 탐색.
                    # 연결된 모든 육지 탐험이 끝나면 카운트 +1
                    count += 1

        return count

# 47 / 47 test cases passed.
# Status: Accepted
# Runtime: 136 ms
# Memory Usage: 14.9 MB
#
# Your runtime beats 94.71 % of python3 submissions.
# Your memory usage beats 65.08 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.
