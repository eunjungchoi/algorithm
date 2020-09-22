# You want to build a house on an empty land which reaches all buildings in the shortest amount of distance.
# You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:
#
# Each 0 marks an empty land which you can pass by freely.
# Each 1 marks a building which you cannot pass through.
# Each 2 marks an obstacle which you cannot pass through.
# Example:
#
# Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
#
# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
#
# Output: 7
#
# Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
#              the point (1,2) is an ideal empty land to build a house, as the total
#              travel distance of 3+3+1=7 is minimal. So return 7.
# Note:
# There will be at least one building.
# If it is not possible to build such house according to the above rules, return -1.
import collections
from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:

        # Use hit : to record how many times a 0 grid has been reached.
        # use distSum: to record the sum of distance from all 1 grids to this 0 grid.
        # A powerful pruning is that during the BFS we use count1 to count how many 1 grids we reached.
        # If count1 < buildings then we know not all 1 grids are connected are we can return -1 immediately,
        # which greatly improved speed (beat 100% submissions).

        # M x N 매트릭스에서 기존 빌딩 (1) 인 곳들에서부터 각각 출발해 모든 매트릭스를 순회.
        # 그 과정에서 값이 0인 빈 셀 [i, j]을 만날 때마다 출발 빌딩부터 그 셀까지의 거리를  거리합 테이블[i][j]에 + 합산해줌.
        # 이때 몇개의 출발 빌딩에서 해당 0 셀을 방문했는지 hit 수도 기록함. 이 숫자가 전체 빌딩 수와 같아야 이 0 셀에 건물 짓기 가능.
        # 한 빌딩에서 출발해서 계속 방문할 목록들은 queue로 관리. 한 셀 방문 후 해당 셀의 동서남북을 방문하고 해당 셀이 0이면 그 주변 셀을 다시 큐에 삽입.
        # 각 셀에 해당하는 hit 수 테이블과 distSum 테이블은 전역적으로 관리
        # visited 테이블은 각 빌딩에서 출발하는 BFS 탐색마다 새로 리셋해서 관리.  매 빌딩마다 전체 매트릭스를 새로 탐색해야 함.
        # 탐색 중 또다른 빌딩 셀을 마주쳤을 때는  빌딩 방문수 count1 을 1 추가해줌. 한 빌딩에서  다른 모든 빌딩을 방문할 때마다 +1 해주고  최종 count가 전체 빌딩수보다 작으면
        # 길이 막혀서 모든 빌딩을 연결하지 못한다는 말. -1을 리턴

        # 예외 처리
        if not grid or not grid[0]:
            return -1

        # 자료 구조
        M, N = len(grid), len(grid[0])
        buildings = sum(val for row in grid for val in row if val == 1)  # O(mn)  기존 빌딩의 개수
        hit = [[0] * N for i in range(M)]  # space: O(mn)
        distSum = [[0] * N for i in range(M)]  # 이 셀에서부터 모든 빌딩까지의 거리의 합.

        def BFS(start_x, start_y):  # grid[x][y] == 1일 때
            visited = [[False] * N for k in range(M)]   # 각 빌딩에서 출발하는 BFS 마다 새롭게 visited 테이블 설정.
            visited[start_x][start_y] = True
            count1 = 1
            queue = collections.deque([(start_x, start_y, 0)])  # (i, j, distance)   출발점을 큐에 삽입. 거리는 = 0

            while queue:
                x, y, dist = queue.popleft()
                # 동서남북 탐색
                for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= i < M and 0 <= j < N and not visited[i][j]:
                        visited[i][j] = True

                        if grid[i][j] == 0:  # 동서남북 셀의 값이 0이면 = 빈 공간이면   빈 곳을 계속 큐에 추가.
                            queue.append((i, j, dist + 1))  # 해당 셀을 큐에 추가 (거리에 1 추가)
                            hit[i][j] += 1  # 각 빌딩에서 출발해서 이 0번 셀에 도달했으면 값 1 추가. 모든 빌딩의 숫자와 같아져야만 이 셀에 건물 짓기 가능
                            distSum[i][j] += dist + 1  # 거리합 테이블에 1 추가. grid[i][j] == 0인 곳만  값을 정산
                        elif grid[i][j] == 1:  # 특정 빌딩에서 다른 빌딩으로 도달했다는 것.
                            count1 += 1  # 빌딩(=1) 셀 몇개에 도달했는지

            return count1 == buildings  # 다른 모든 빌딩들에 도달했으면 True, 아니면 false  (다른 모들 빌딩에 도달해야 성립됨)

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    if not BFS(i, j):   # 매 빌딩마다 너비 우선 탐색으로  다른 모들 빌딩에 도착하는지 체크. False면 -1 반환.
                        return -1

        result = [distSum[i][j] for i in range(M) for j in range(N) if grid[i][j] == 0 and hit[i][j] == buildings]
        if not result:
            return -1

        # 빈 땅 = 각 0셀에 해당하는 거리합 테이블 값 중에  가장 값이 작은 곳이  ==>  건물 짓기 후보가 됨.  = shortest distance from all buildings. 
        return min(result)

        # return min([distSum[i][j] for i in range(M) for j in range(N) if grid[i][j] == 0 and hit[i][j] == buildings] or [-1])


# 72 / 72 test cases passed.
# Status: Accepted
# Runtime: 92 ms
# Memory Usage: 13.9 MB
#
# Your runtime beats 93.38 % of python3 submissions.
# Your memory usage beats 93.14 % of python3 submissions.
