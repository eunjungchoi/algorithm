# There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.
#
# Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.
#
# Example 1:
# Input:
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation:
# The graph looks like this:
#
#
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
# Example 2:
# Input:
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500
# Explanation:
# The graph looks like this:
#
#

# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
#
#
# Constraints:
#
# The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
# The size of flights will be in range [0, n * (n - 1) / 2].
# The format of each flight will be (src, dst, price).
# The price of each flight will be in the range [1, 10000].
# k is in the range of [0, n - 1].
# There will not be any duplicated flights or self cycles
import collections
import heapq
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # 그래프 구성
        graph = collections.defaultdict(list)
        for start, target, weight in flights:
            graph[start].append((target, weight))

        # 우선순위 큐를 위한 큐 변수 정의
        Q = [(0, src, K)]  # [(가격, 정점, 남은 가능한 경유지 수))]

        # 우선순위 큐 최솟값 기준으로 정점까지 최소 비용 판별
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price

            if k >= 0:
                for target, weight in graph[node]:
                    alt = price + weight
                    heapq.heappush(Q, (alt, target, k - 1))

        return -1


# 47 / 47 test cases passed.
# Status: Accepted
# Runtime: 84 ms
# Memory Usage: 19.5 MB
#
# Your runtime beats 93.78 % of python3 submissions.
# Your memory usage beats 29.72 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.
