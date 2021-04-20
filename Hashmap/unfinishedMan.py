# 첫 번째 답. 정확성만 만점, 효율성은 모두 실패 - O(N^3)
import collections


def solution1(participant, completion):
    for p in participant:  # O(N)
        if p in completion:  # O(N)
            completion.remove(p)  # O(N) 이 부분에서 시간이 많이 걸리는 듯 하다.
        else:
            return p

# 두 번째 답. 정확성과 효율성 모두 만점 - O(N LogN + N LogN + N)


def solution2(participant, completion):
    participant.sort()  # O(N Log N)
    completion.sort()  # O(N Log N)

    for p, c in zip(participant, completion):  # O(N)
        if p != c:
            return p
    return participant[-1]


# 제일 간결한 코드 - 다른 사람의 답 - O(N) + O(N) + O(1) + O(1)


def solution3(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


# 출처 - 프로그래머스 - 완주하지 못한 선수
