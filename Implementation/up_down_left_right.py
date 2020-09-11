########################
# ex
# Input
# 5 (size of the map)
# R R R U D D (routes)
#
# Output
# 3 4 (Final position)
########################

## my code
# Input
N = int(input("Type the size of the map: "))
routes = input("Type the route: ").split()

print(N)
print(routes)

# Initial position
pos = [1,1]

# Travel
for route in routes:
    if route == "U":
        pos[0] -= 1
    elif route == "D":
        pos[0] += 1
    elif route == "L":
        pos[1] -= 1
    elif route == "R":
        pos[1] += 1

    # check out of bound
    if pos[0]==0:
        pos[0] += 1
    elif pos[0] > N:
        pos[0] -= 1
    elif pos[1]==0:
        pos[1] += 1
    elif pos[1] > N:
        pos[1] -= 1

# Output
print(pos) # final position



## book's code

# N을 입력 받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)