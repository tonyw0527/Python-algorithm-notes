# 기본 풀이
answer = 0


def dfs(idx, value, numbers, target):
    global answer
    N = len(numbers)

    if idx == N and value == target:
        answer += 1
        return
    if idx == N:
        return

    dfs(idx + 1, value + numbers[idx], numbers, target)
    dfs(idx + 1, value - numbers[idx], numbers, target)


def solution1(numbers, target):
    global answer
    dfs(0, 0, numbers, target)
    return answer

# 다른 사람의 풀이 - 재귀함수를 사용한 간결한 코드..


def solution2(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution2(numbers[1:], target-numbers[0]) + solution2(numbers[1:], target+numbers[0])
