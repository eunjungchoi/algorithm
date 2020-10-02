# You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat,
# and seats[i] = 0 represents that the ith seat is empty (0-indexed).
#
# There is at least one empty seat, and at least one person sitting.
#
# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.
#
# Return that maximum distance to the closest person.


# Input: seats = [1,0,0,0,1,0,1]
# Output: 2
# Explanation:
# If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
# Example 2:
#
# Input: seats = [1,0,0,0]
# Output: 3
# Explanation:
# If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.
# Example 3:
#
# Input: seats = [0,1]
# Output: 1
from typing import List
"""
좌석[i] = 1은 i번째 좌석에 앉은 사람을 나타내며, 좌석[i] = 0은 i번째 좌석이 비어 있음을 나타낸다(0-색인).
적어도 빈자리가 하나 있고, 적어도 한 사람이 앉아 있다.
알렉스는 그와 가장 가까운 사람과의 거리가 극대화되는 자리에 앉고 싶어한다.
가장 가까운 사람으로부터 가장 먼 자리를 반환하라. 
"""

class Solution:

    # def maxDistToClosest(self, seats: List[int]) -> int:
    #     v = len(seats)
    #     distance = [None] * len(seats)
    #     for i in range(len(seats)):
    #         if seats[i]:
    #             v = 0
    #         else:
    #             v += 1
    #         distance[i] = v
    #     v = len(seats)
    #     for i in range(len(seats) - 1, -1, -1):
    #         if seats[i]:
    #             v = 0
    #         else:
    #             v += 1
    #         distance[i] = min(v, distance[i])
    #     return max(distance)

    def maxDistToClosest(self, seats: List[int]) -> int:
        dp = [None] * len(seats)
        d = len(seats)

        for i, seat in enumerate(seats):
            if seat == 1:
                d = 0
            elif seat == 0:
                d += 1
            dp[i] = d
        d = len(seats)
        for i in range(len(seats) - 1, -1, -1):
            if seats[i] == 1:
                d = 0
            elif seats[i] == 0:
                d += 1
            dp[i] = min(dp[i], d)

        max_ = max(dp)
        for i, val in enumerate(dp):
            if val == max_:
                return i

    def maxDistToClosest1(self, seats: List[int]) -> int:
        max_ = 1

        for i, occupied in enumerate(seats):
            if not occupied:
                left = right = i
                while 0 <= left and not seats[left] and right <= len(seats) - 1 and not seats[right]:
                    left = left - 1 if left > 0 else left
                    right = right + 1 if right < len(seats) - 1 else right

                max_ = max(max_, i - left, right - i)

        return max_


# 79 / 79 test cases passed.
# Status: Accepted
# Runtime: 148 ms
# Memory Usage: 14.7 MB
#
# Your runtime beats 49.54 % of python3 submissions.
# Your memory usage beats 10.09 % of python3 submissions.
