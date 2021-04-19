# Data Structure

# Stack
from collections import deque
stack = []
stack.append(1)
stack.pop()

# Queue
queue = deque()
queue.append(1)
queue.popleft()
list(queue)

# Algorithm
# Recusive function


def recursive_function(n):
    if n == 10:
        return
    recursive_function(n+1)


recursive_function(1)

# DFS - stack 자료구조를 기반으로함. -> 따라서 재귀 함수를 이용하여 간결하게 구현.


def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [  # 노드의 연결 정보. 연결 여부만 나타낼뿐 거리를 나타내지 않는다.
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9  # 노드의 방문 정보. 노드의 개수는 8개이다.

dfs(graph, 1, visited)

# BFS - queue 자료구조 기반. O(N)의 시간 복잡도. 일반적인 경우 실제 수행 시간은 DFS보다 좋은 편.


def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 시작 노드 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입 및 방문 처리
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [  # 노드의 연결 정보. 연결 여부만 나타낼뿐 거리를 나타내지 않는다.
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9  # 노드의 방문 정보. 노드의 개수는 8개이다.

bfs(graph, 1, visited)
