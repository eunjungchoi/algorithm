# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
#
#
# Example 1:
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 그래프 구성
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        # 이미 방문했던 노드를 저장. 중복 방문시 순환 구조로 간주.
        traced = set()
        visited = set()  # 방문해서 검증한 곳  가지치기 용.

        def dfs(i):
            # 순환구조면 False 반환.
            if i in traced:
                return False

            if i in visited:
                return True

            traced.add(i)

            for y in graph[i]:
                if not dfs(y):
                    return False

            traced.remove(i)
            visited.add(i)

            return True

        # 순환구조 판별
        for x in list(graph):
            if not dfs(x):
                return False

        return True


# Runtime: 96 ms, faster than 94.83% of Python3 online submissions for Course Schedule.
# Memory Usage: 17.4 MB, less than 6.56% of Python3 online submissions for Course Schedule.
# <파이썬 알고리즘 인터뷰> 참고.
