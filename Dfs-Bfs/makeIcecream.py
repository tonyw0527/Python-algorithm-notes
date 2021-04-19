# N X M 크기의 얼음틀, 0은 구멍, 1은 칸막이.
# 0인 부분이 상하좌우로 붙어 있으면 연결된 것으로 간주.
# ex) 3 X 3 크기, 3개의 아이스크림이 생성됨.
'''
3 3
0 0 1
0 1 0
1 0 1
'''
# ploblem - 생성된 아이스크림의 수를 return

# Hint - DFS를 이용

# 풀이 - DFS를 이용하여 시작 노드로부터 상하좌우에 0인 부분이 있다면 끝까지, 범위 밖이나 1인 부분을 만날 때까지 1로 방문처리한다.
# 다시 말해, 아이스크림이 만들어지는 0으로 구성된 묶음 중 한곳의 0이라도 만나면 그 묶음을 모두 1로 채우고 단 한번 True값을 반환하여 묶음의 개수를 카운드 한다.
# answer
# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문


def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)  # 정답 출력
