# Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.
#
# Example:
#
# Given the following 3x6 height map:
# [
#   [1,4,3,1,3,2],
#   [3,2,1,3,2,4],
#   [2,3,3,2,3,1]
# ]
#
# Return 4.
#
#
# The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.
#
#
#
#
#
# After the rain, water is trapped between the blocks. The total volume of water trapped is 4.
#
#
#
# Constraints:
#
# 1 <= m, n <= 110
# 0 <= heightMap[i][j] <= 20000

# matrix, heap, memoization, BFS

import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # 이 문제 진짜 짱이네. 아름답다 진짜

        # 예외처리
        if not heightMap or not heightMap[0]:
            return 0

        # 변수 선언
        rows = len(heightMap)
        cols = len(heightMap[0])
        heap = []
        result = 0
        # memoization . 방문했던 곳 저장.
        visited = [[0] * cols for _ in range(rows)]

        # grid의 border cell을 모두 heap에 집어넣기. (python heap은 최소 힙)
        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0 or i == rows - 1 or j == cols - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    # 방문했다고 저장.
                    visited[i][j] = 1

        # heap에서 최소값을 뽑아서
        while heap:
            height, i, j = heapq.heappop(heap)
            # 셀을 중심으로 동서남북 탐방
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                # 현재 셀과 동서남북 셀의 높이를 각각 비교해서 주변 셀이 더 낮으면 그 차이를 result에 합산. 주변 셀이 높으면 0을 더해줌.

                if 0 <= x < rows and 0 <= y < cols and not visited[x][y]:
                    result += max(0, height - heightMap[x][y])
                    # 주변 셀을 다시 heap에 넣어줌. 높이는 height와  주변 셀의 height 중 최대값으로 설정.
                    heapq.heappush(heap, (max(height, heightMap[x][y]), x, y))
                    visited[x][y] = 1

        return result


# 39 / 39 test cases passed.
# Status: Accepted
# Runtime: 180 ms
# Memory Usage: 15.1 MB
#
# Your runtime beats 85.39 % of python3 submissions.
# Your memory usage beats 63.56 % of python3 submissions.
