# graph traversal

# adjacency List
graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

# DFS  (depth-first search)

# recursive


def recursive_dfs(v, discovered=[]):
    discovered.append(v)   # discovered에  정점 추가
    for destination in graph[v]:  # 그 정점에서 출발하는 도착지 목록을 하나씩 순회하면서
        if destination not in discovered:     # 도착지가 discovered에 포함이 안되어 있으면
            discovered = recursive_dfs(destination, discovered)   # 그 도착지 정점과 discovered 목록을 다시 넣어서 재귀적으로 함수 호출.

    return discovered  # 최종 discovered 리스트 반환.

# discovered
# [1],
# [1, 2],
# [1, 2, 5],
# [1, 2, 5, 6],
# [1, 2, 5, 6, 7],
# [1, 2, 5, 6, 7, 3],
# [1, 2, 5, 6, 7, 3, 4]


# iterative

def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]  # 스택에 첫 출발 정점을 삽입

    while stack:   # 스택에 아이템이 하나라도 있으면
        v = stack.pop()  # 스택에서 top=가장 뒤에 넣은 것을 뽑아냄
        if v not in discovered:   # 스택에서 뽑은 정점이 discovered에 포함이 안되어 있으면
            discovered.append(v)  # discovered에  추가
            for destination in graph[v]:   # 그 정점에서 출발하는 도착지 정점들 리스트를 하나식 순회하며
                stack.push(destination)  # 그 도착지 정점들을 스택에 추가

    return discovered

# discovered
# [1]
# [1, 4],
# [1, 4, 3]
# [1, 4, 3, 5]
# [1, 4, 3, 5, 7]
# [1, 4, 3, 5, 7, 6]
# [1, 4, 3, 5, 7, 6, 2]

# stack
# [1]
# [2, 3, 4]
# [2, 3]
# [2]
# [2, 5]
# [2, 6, 7]
# [2, 6, 3]
# [2, 6]
# [2]
# []




