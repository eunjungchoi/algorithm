# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
#
# (Here, the distance between two points on a plane is the Euclidean distance.)
#
# You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
#
#
#
# Example 1:
#
# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
# Example 2:
#
# Input: points = [[3,3],[5,-1],[-2,4]], K = 2
# Output: [[3,3],[-2,4]]
# (The answer [[-2,4],[3,3]] would also be accepted.)
#
#
# Note:
#
# 1 <= K <= points.length <= 10000
# -10000 < points[i][0] < 10000
# -10000 < points[i][1] < 10000

# 평면 상에 points 목록이 있을 때 원점 (0, 0)에서 K 번 가까운 점 목록을 순서대로 출력하라.
# 평면 상 두 점의 거리는 유클리드 거리로 한다.
# K번 추출이라는 단어에서 바로, 우선순위 큐를 떠올릴 수 있다.


import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))

        result = []
        for _ in range(K):
            dist, x, y = heapq.heappop(heap)
            result.append([x, y])

        return result


# 83 / 83 test cases passed.
# Status: Accepted
# Runtime: 720 ms
# Memory Usage: 19.5 MB
#
# Your runtime beats 73.64 % of python3 submissions.
# Your memory usage beats 27.85 % of python3 submissions.
