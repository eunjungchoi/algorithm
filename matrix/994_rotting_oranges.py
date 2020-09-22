# In a given grid, each cell can have one of three values:
#
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
#
#
#
# Example 1:
#
#
#
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:
#
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:
#
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
#
#
# Note:
#
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.
import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS

        deque = collections.deque()
        fresh = 0

        # 1. 전체 매트릭스 순회하면서 2이면 deque에 추가, 1이면 fresh 카운드 +1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    deque.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        deque.append((-1, -1))  #

        # 2. 썩는 프로세스 BFS
        minutes_elapsed = -1  # 마지막 rotten orange 의 이웃을 찾기 위해 1분을 더 소요하기 때문에. 1을 빼줘야 함.

        while deque:
            i, j = deque.popleft()
            if i == -1:
                # finish one rount of processing
                minutes_elapsed += 1
                if deque:
                    deque.append((-1, -1))

            else:
                # this is a rotten orange
                for I, J in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= I < len(grid) and 0 <= J < len(grid[0]) and grid[I][J] == 1:
                        grid[I][J] = 2
                        fresh -= 1
                        deque.append((I, J))

        return minutes_elapsed if fresh == 0 else -1


# 303 / 303 test cases passed.
# Status: Accepted
# Runtime: 52 ms
# Memory Usage: 13.8 MB
#
# Your runtime beats 70.48 % of python3 submissions.
# Your memory usage beats 66.27 % of python3 submissions.
