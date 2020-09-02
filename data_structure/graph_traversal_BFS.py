
# BFS (breath-first Search)

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def iterative_bfs(start_v):
    discovered = [start_v]     # discovered에  첫 출발 정점 삽입
    queue = [start_v]   # 큐에 첫 출발 정점 삽입

    while queue:   # 큐에 아이템이 하나라도 있을 때
        v = queue.pop(0)   # 큐의 맨 앞에 있는 정점을 추출
        for destination in graph[v]:    # 그 정점에서 출발하는 도착지 리스트를 순회하며
            if destination not in discovered:   # 도착지 정점들이 discovered에 없으면
                discovered.append(destination)    # 그 도착지 정점을 discovered에 추가
                queue.append(destination)    # 도착지 정점을 큐에도 추가

    return discovered


# discovered
# [1]
# [1, 2, 3, 4]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5, 6, 7]

# queue
# [1]
# []
# [2, 3, 4]
# [3, 4]
# [3, 4, 5]
# [4, 5]
# [5]
# []
# [6, 7]
# [7]
# []


