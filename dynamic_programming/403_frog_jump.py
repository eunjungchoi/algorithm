# A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.
#
# Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.
#
# If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.
#
# Note:
#
# The number of stones is ≥ 2 and is < 1,100.
# Each stone's position will be a non-negative integer < 231.
# The first stone's position is always 0.
# Example 1:
#
# [0,1,3,5,6,8,12,17]
#
# There are a total of 8 stones.
# The first stone at the 0th unit, second stone at the 1st unit,
# third stone at the 3rd unit, and so on...
# The last stone at the 17th unit.
#
# Return true. The frog can jump to the last stone by jumping
# 1 unit to the 2nd stone, then 2 units to the 3rd stone, then
# 2 units to the 4th stone, then 3 units to the 6th stone,
# 4 units to the 7th stone, and 5 units to the 8th stone.
# Example 2:
#
# [0,1,2,3,4,8,9,11]
#
# Return false. There is no way to jump to the last stone as
# the gap between the 5th and 6th stone is too large.
from typing import List


class Solution:
    """
    개구리가 강을 건너고 있다. 강은 x 단위로 나뉘며 각 단위에는 돌이 존재할 수도 있고 없을 수도 있다. 개구리는 돌에 뛰어 오를 수 있지만, 물 속으로 뛰어들어서는 안 된다.

오름차순으로 돌의 위치 목록(단위)을 지정하면 개구리가 마지막 돌에 착지해 강을 건널 수 있는지 판단한다. 처음에 개구리는 첫 번째 돌 위에 있고 첫 번째 점프는 1단위여야 한다고 가정한다.

개구리의 마지막 점프가 k 단위였다면 다음 점프는 k - 1, k 또는 k + 1 단위여야 한다. 개구리는 앞으로만 점프할 수 있다는 점에 유의하십시오.

참고:

돌의 수는 ≥ 2이며, < 1,100개>이다.
각 돌의 위치는 음이 아닌 정수 < 231이 될 것이다.
초석의 위치는 항상 0이다.

the 2D array will be something like below.

index:        0   1   2   3   4   5   6   7
            +---+---+---+---+---+---+---+---+
stone pos:  | 0 | 1 | 3 | 5 | 6 | 8 | 12| 17|
            +---+---+---+---+---+---+---+---+
diff      0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 |
val       1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
          2 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
          3 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 |
          4 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 |
          5 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
          6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
          7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
    """

    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [[False] * (n + 1) for _ in range(n)]
        dp[0][1] = True  # dp[돌][돌에서 갈 수 있는 거리]

        for i in range(1, n):  # i = 7  (돌 17)
            for j in range(0, i):  # 이전 돌들.   j = 6 (돌 12)
                diff = stones[i] - stones[j]  # 5
                if diff < 0 or diff > n or not dp[j][diff]:  # diff[6][5]
                    continue
                dp[i][diff] = True
                if diff - 1 >= 0:
                    dp[i][diff - 1] = True
                if diff + 1 <= n:
                    dp[i][diff + 1] = True
                if i == n - 1:
                    return True

        return False


# 39 / 39 test cases passed.
# Status: Accepted
# Runtime: 1732 ms
# Memory Usage: 21.7 MB
#
# Your runtime beats 13.46 % of python3 submissions.
# Your memory usage beats 21.25 % of python3 submissions.
