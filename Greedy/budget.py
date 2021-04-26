# Greedy 문제
# 오름차순 sort
# 앞 인덱스부터의 합 > budget까지 answer += 1
def solution(d, budget):
    answer = 0
    sum = 0

    d.sort()

    for n in d:
        sum += n
        if sum > budget:
            return answer
        answer += 1

    return answer
