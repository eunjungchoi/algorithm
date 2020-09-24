# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.
#
# The lock initially starts at '0000', a string representing the state of the 4 wheels.
#
# You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.
#
# Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.
#
#
#
# Example 1:
#
# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6
# Explanation:
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
# because the wheels of the lock become stuck after the display becomes the dead end "0102".
# Example 2:
#
# Input: deadends = ["8888"], target = "0009"
# Output: 1
# Explanation:
# We can turn the last wheel in reverse to move from "0000" -> "0009".
# Example 3:
#
# Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
# Output: -1
# Explanation:
# We can't reach the target without getting stuck.
# Example 4:
#
# Input: deadends = ["0000"], target = "8888"
# Output: -1
#
#
# Constraints:
#
# 1 <= deadends.length <= 500
# deadends[i].length == 4
# target.length == 4
# target will not be in the list deadends.
# target and deadends[i] consist of digits only.
from collections import deque
from typing import List


class Solution:
    """
    4개의 원형 바퀴가 달린 자물쇠가 있다. 각 휠에는 0-9의 10개의 슬롯이 있다. 바퀴는 자유롭게 회전하고 감을 수 있다. 9를 0으로, 0을 9로 바꿀 수 있다. 각각의 움직임은 한 바퀴를 한 슬롯씩 돌리는 것으로 구성된다.

    잠금 장치는 처음에 4개의 휠 상태를 나타내는 문자열인 0000에서 시작한다.

    막다른 골목의 목록이 주어진다. 즉, 자물쇠에 이런 코드가 표시되면 자물쇠의 바퀴가 돌지 않고 그것을 열 수 없게 된다.

    잠금을 해제할 휠의 값을 나타내는 표적을 지정하면 잠금을 여는 데 필요한 최소 총 회전 수를 반환하라. 불가능한 경우 -1을 반환하라.

    """

    # 이 문제를 그래프의 최단 경로 문제로 생각할 수 있다.
    # 1000개의 노드가 있고  (0000-9999까지)  두 노드가 한 자릿수가 다르면 두 노드 사이에는 edge가 있다.
    # (0과 9은 1만큼 차이난다) 두 노드가 모두 데드엔드에 있지 않을 경우에.

    # 너비우선탐색 BFS을 사용해 풀이할 수 있다. queue + set을 사용한다. set에는 노드가 큐에 들어갔었는지 여부를 저장한다.
    # 자물쇠 i = 0, 1, 2, 3  각각의 포지션에 대해 d = -1, 1 방향으로 돌린 후 i번째 자물쇠의 잠금값을 결정한다.
    # 0000이 위험한지 처음에 확인해야 한다.

    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i + 1:]

        dead = set(deadends)
        queue = deque([('0000', 0)])
        seen = {'0000'}

        while queue:
            node, depth = queue.popleft()
            if node == target:
                return depth

            if node in dead:
                continue

            for neighbor in neighbors(node):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, depth + 1))

        return -1


# 46 / 46 test cases passed.
# Status: Accepted
# Runtime: 744 ms
# Memory Usage: 14.9 MB
#
# Your runtime beats 50.19 % of python3 submissions.
# Your memory usage beats 65.39 % of python3 submissions.
