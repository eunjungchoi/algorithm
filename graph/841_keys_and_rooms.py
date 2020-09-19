# There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and
# each room may have some keys to access the next room.
#
# Formally, each room i has a list of keys rooms[i],
# and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.
# A key rooms[i][j] = v opens the room with number v.
#
# Initially, all the rooms start locked (except for room 0).
#
# You can walk back and forth between rooms freely.
#
# Return true if and only if you can enter every room.
#
# Example 1:
#
# Input: [[1],[2],[3],[]]
# Output: true
# Explanation:
# We start in room 0, and pick up key 1.
# We then go to room 1, and pick up key 2.
# We then go to room 2, and pick up key 3.
# We then go to room 3.  Since we were able to go to every room, we return true.
# Example 2:
#
# Input: [[1,3],[3,0,1],[2],[0]]
# Output: false
# Explanation: We can't enter the room with number 2.
# Note:
#
# 1 <= rooms.length <= 1000
# 0 <= rooms[i].length <= 1000
# The number of keys in all rooms combined is at most 3000.
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)  # 각 노드마다 방문 여부를 저장
        visited[0] = True
        stack = [0]  # keys to use

        while stack:
            node = stack.pop()

            for other_room in rooms[node]:
                if not visited[other_room]:
                    visited[other_room] = True
                    stack.append(other_room)

        return all(visited)  # Return true if we've visited every room


# Time Complexity: O(N + E), where N is the number of rooms, and E is the total number of keys.
# Space Complexity: O(N) in additional space complexity, to store stack and visited.

# 67 / 67 test cases passed.
# Status: Accepted
# Runtime: 68 ms
# Memory Usage: 14.3 MB
#
# Your runtime beats 73.95 % of python3 submissions.
# Your memory usage beats 35.86 % of python3 submissions.

