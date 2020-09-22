# There are a total of n courses you have to take labelled from 0 to n - 1.
#
# Some courses may have prerequisites,
# for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.
#
# Given the total number of courses numCourses and a list of the prerequisite pairs,
# return the ordering of courses you should take to finish all courses.
#
# If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
#
#
#
# Example 1:
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0.
# So the correct course order is [0,1].
# Example 2:
#
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2.
# Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
# Example 3:
#
# Input: numCourses = 1, prerequisites = []
# Output: [0]
from collections import defaultdict
from typing import List


class Solution:
    WHITE = 1
    GRAY = 2
    BLACK = 3

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # Depth First Search
        # 1. 스택 초기화. 스택에는 그래프에 있는 코스들의 위상 정렬 순서를 담는다.
        # 2. input으로 주어진 edge 쌍을 이용해 인접리스트를 생성한다. [a, b] 와 같은 쌍은 코스 a를 위해 코스 b가 선행되어야 한다는 것을 나타낸다.
        #  b -> a 의 간선 형태를 의미. 알고리즘 구현시 유의.
        # 3. 그래프의 각 노드들에 대해, (그 노드가 아직 다른 노드의 DFS 순회를 통해 방문되지 않은 경우), DFS 탐색을 실행한다.
        # 4. 노드 N에 대해 DFS를 실행하고 있다고 하자.  N 노드의 모든 이웃들 (이전에 처리되지 않았던) 을 재귀적으로 순회할 것이다.
        # 5. 모든 이웃들에 대한 처리가 완료되면 n 노드를 스택에 추가한다. 필요한 순서를 시뮬레이트 하기 위해 스택을 사용한다.
        # 노드 N을 스택에 추가할 때, 노드 N을 선행조건으로 필요로 하는 모든 노드가 스택에 이미 들어가있을 것이다.
        # 6. 모든 노드가 처리되면, 노드들을 반환한다. top에서 bottom까지 스택의 순서 그대로.

        # Create the adjacency list representation of the graph
        adj_list = defaultdict(list)  # 인접리스트 생성.

        # A pair [a, b] in the input represents edge from b --> a
        for dest, src in prerequisites:  # 선행조건 리스트를 순회하며 인접리스트에 b-> a 순서로 추가
            adj_list[src].append(dest)

        topological_sorted_order = []  # 위상 정렬 순서를 담을 리스트.
        is_possible = True

        # By default all vertices are WHITE
        color = {i: Solution.WHITE for i in range(numCourses)}

        def dfs(node):
            nonlocal is_possible

            # Don't recurse further if we found a cycle already
            if not is_possible:
                return

            # Start the recursion
            color[node] = Solution.GRAY

            # Traverse on neighboring vertices
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution.WHITE:  # 이웃 노드가 아직 방문하지 않은 노드이면, 이웃 노드로 DFS 진행.
                        dfs(neighbor)
                    elif color[neighbor] == Solution.GRAY:  # 이미 DFS가 진행 중인 이웃노드를 발견했다면 cycle이 있다는 말. 더 이상 재귀 불가.
                        # An edge to a GRAY vertex represents a cycle
                        is_possible = False

            # Recursion ends. We mark it as black
            # 이웃들까지 재귀적으로 순환이 끝내면  현재 node를 black으로 변경. 탐색 끝.
            color[node] = Solution.BLACK
            topological_sorted_order.append(node)

        for vertex in range(numCourses):  # 모든 정점을 순회하며, 아직 방문하지 않않은 정점을 DFS 탐색 실행
            # If the node is unprocessed, then call dfs on it.
            if color[vertex] == Solution.WHITE:
                dfs(vertex)

        return topological_sorted_order[::-1] if is_possible else []



# 44 / 44 test cases passed.
# Status: Accepted
# Runtime: 156 ms
# Memory Usage: 17.1 MB
#
# Your runtime beats 27.35 % of python3 submissions.
# Your memory usage beats 12.19 % of python3 submissions.
