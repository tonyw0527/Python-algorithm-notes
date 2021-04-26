# 리스트C3 의 조합의 경우의 수를 담은 리스트를 얻는다.
# 각 원소의 합이 소수인 것들의 수만 더한다.
from itertools import combinations
from math import sqrt


def isPrime(num):
    if num < 2:
        return False
    for n in range(2, int(sqrt(num)) + 1):
        if num % n == 0:
            return False
    return True


def solution(nums):
    answer = 0

    cases = list(combinations(nums, 3))

    for c in cases:
        summedNum = sum(c)
        if isPrime(summedNum):
            print(summedNum, ' is prime number')
            answer += 1

    return answer
