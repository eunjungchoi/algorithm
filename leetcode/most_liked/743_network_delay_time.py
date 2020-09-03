# There are N network nodes, labelled 1 to N.
#
# Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.
#
# Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.
#
#
#
# Example 1:
#
#
#
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
# Output: 2
#
#
# Note:
#
# N will be in the range [1, 100].
# K will be in the range [1, N].
# The length of times will be in the range [1, 6000].
# All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # 그래프 구성
        graph = collections.defaultdict(list)
        for start, target, weight in times:
            graph[start].append((target, weight))

        # 우선순위 큐를 위한 큐 변수 정의
        Q = [(0, K)]  # [(소요시간, 정점))]
        dist = collections.defaultdict(int)

        # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:  # dist 에 node 포함 여부부터 체크. 비어있는 경우에만 힙에 푸시. dist에는 항상 최솟값이 세팅됨. 수도코드일 때는 dist를 무한대로 채우고 시작.
                dist[node] = time

                for target, weight in graph[node]:
                    alt = time + weight
                    heapq.heappush(Q, (alt, target))

        # 모든 경로의 최단 경로 존재 여부 판별
        if len(dist) == N:
            return max(dist.values())
        return -1


# 51 / 51 test cases passed.
# Status: Accepted
# Runtime: 496 ms
# Memory Usage: 15.5 MB
#
# Your runtime beats 79.56 % of python3 submissions.
# Your memory usage beats 78.38 % of python3 submissions.
