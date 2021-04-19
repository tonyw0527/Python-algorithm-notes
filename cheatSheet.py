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

# Depth First Search - stack 자료구조를 기반으로함. -> 따라서 재귀 함수를 이용하여 간결하게 구현.


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

# Breadth First Search - queue 자료구조 기반. O(N)의 시간 복잡도. 일반적인 경우 실제 수행 시간은 DFS보다 좋은 편.


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

# Dynamic Programming

# 피보나치 함수(Fibonacci Function)을 재귀함수로 구현 -> O(2^N)의 지수 시간 복잡도...


def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)


print(fibo(4))

# 탑다운(재귀함수사용) 다이나믹 프로그래밍 - 피보나치 함수(Fibonacci Function)를 재귀함수로 구현 -> O(N)의 상수 시간 복잡도
# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화 - 메모이제이션은 탑다운 방식에 국한되어 사용
d = [0] * 100


def fibo1(x):
    # 종료 조건(1 혹은 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]


print(fibo1(99))

d = [0] * 100

# 바텀업(반복문 사용) 다이나믹 프로그래밍 - 일반적으로 반복문을 이용한 DP가 더 성능이 좋다. DP의 전형적인 방식.
# 앞서 계산된 결과를 저장하기 위한 'DP 테이블' 초기화
d = [0] * 100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수(Fibonacci Function) 반복문으로 구현
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])
