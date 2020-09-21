# You are given a m x n 2D grid initialized with these three possible values.
#
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
#
# Example:
#
# Given the 2D grid:
#
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# After running your function, the 2D grid should be:
#
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4
import collections
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # BFS, queue

        deque = collections.deque([(i, j) for i, row in enumerate(rooms) for j, room in enumerate(row) if room == 0])
        # 값이 0인 인덱스만 담음.

        while deque:
            i, j = deque.popleft()
            # 해당 인덱스의 동서남북을 탐색

            for I, J in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= I < len(rooms) and 0 <= J < len(rooms[0]) and rooms[I][J] > 2 ** 30:
                    rooms[I][J] = rooms[i][j] + 1
                    deque.append((I, J))


# 62 / 62 test cases passed.
# Status: Accepted
# Runtime: 268 ms
# Memory Usage: 17.2 MB
#
# Your runtime beats 90.21 % of python3 submissions.
# Your memory usage beats 33.70 % of python3 submissions.
#