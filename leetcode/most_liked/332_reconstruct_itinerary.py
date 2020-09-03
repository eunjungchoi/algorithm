# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
#
# Note:
#
# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# One must use all the tickets once and only once.
# Example 1:
#
# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
# Example 2:
#
# Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
#              But it is larger in lexical order.
import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # graph 구현
        graph = collections.defaultdict(list)

        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route = []

        # recursive
        def dfs(a):
            # 첫번째 값을 읽어서 어휘순으로 방문한다. (sorted에서 reverse=False 일 때. pop(0)으로 큐 처럼 연산)
            # 마지막 값을 읽어서 어휘순으로 방문
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)

        dfs('JFK')

        # iterative
        # stack = ['JFK']
        # while stack:  # 마지막 방문지가 남지 않을 때까지
        #     while graph[stack[-1]]:  # 그래프에 값이 있으면 
        #         spot = graph[stack[-1]].pop(0)  # pop(0)으로 맨 처음 값을 추출.
        #         stack.append(spot)  # 스택에 넣는다.  = 큐 연산
        #     route.append(stack.pop())  # 재귀와 달리 반복으로 풀이하려면, 이처럼 한번 더 풀어낼 수 있는 변수가 필요하다.
        #     # 경로가 풀리면서 거꾸로 담기게 됨.

        # 다시 뒤집어서 어휘순으로 반환.
        return route[::-1]


# 80 / 80 test cases passed.
# Status: Accepted
# Runtime: 76 ms
# Memory Usage: 14.1 MB
#
# Your runtime beats 94.37 % of python3 submissions.
# Your memory usage beats 64.04 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.

