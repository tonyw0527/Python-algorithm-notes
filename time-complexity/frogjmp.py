
# 처음 작성한 코드
# 간단한 문제는 풀었으나, X값에 극도로 큰값이 주어졌을 때 시간 초과
# 시간복잡도 - O(N), codility에서는 O(Y-X)라고 표현
# O(N)을 좀더 다이나믹하게 표현하는 듯하다.
# 입력값에따라 점프횟수가 엄청 작거나 또는 엄청 크게 증가할 수 있기 때문!
# 아래 솔루션이 틀린이유가 바로 여기에 있다.
def false_solution(X, Y, D):
    #print('init', X, Y, D)
    result = 0
    sum = X + D

    # X == Y 체크
    if(X == Y):
        return 0

    while True:
        # X < Y이면 일단 한번 점프!
        result += 1
        if sum >= Y:
            break
        else:
            sum += D
            continue

    return result

# 다시 작성한 답
# 시간복잡도 - O(1)로 매우 빠르게 return
# 그냥 나누면 되는 것이었다..


def solution1(X, Y, D):
    # X == Y 체크
    if(X == Y):
        return 0

    share = (Y-X) // D
    rmd = (Y-X) % D

    if rmd == 0:
        return share
    else:
        return share + 1

# divmode 메서드를 사용한 풀이


def solution2(X, Y, D):
    # X == Y 체크
    if(X == Y):
        return 0

    share, rmd = divmod(Y-X, D)

    if rmd == 0:
        return share
    else:
        return share + 1
