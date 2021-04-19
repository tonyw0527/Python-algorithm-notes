# N X M 크기의 미로, 0은 괴물이 있는 곳, 1은 괴물이 없는 곳.
# (1,1) 시작점, (N, M) 탈출점
# 괴물을 피해 미로 탈출.
# ex) 5 X 6 크기. 최소 이동 칸수 10
'''
5 6
1 0 1 0 1 0
1 1 1 1 1 1
0 0 0 0 0 1
1 1 1 1 1 1
1 1 1 1 1 1
'''
# ploblem - 미로 탈출 위한 최소 이동 칸의 개수 return

# Hint - BFS를 이용

# 풀이 - (1,1)점을 시작으로 상하좌우를 살피는데, 방문하지 않은 1인 노드를 만나면 이전 노드의 거리에 1을 더한 값을 그래프 리스트에 넣는다.
# answer
from collections import deque

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현


def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]


# BFS를 수행한 결과 출력
print(bfs(0, 0))
