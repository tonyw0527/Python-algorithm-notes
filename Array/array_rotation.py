# problem

# Hint

# A - 리스트, K - 리스트를 돌릴 횟수
def solution(A, K):
    # empty array 처리
    if(len(A) == 0):
        return A

    result = []

    # length만큼의 경우의 수 가능
    length = len(A)
    # k와 length의 나머지를 통해 경우 계산
    rmd = K % length

    for i in range(length):
        index = -rmd + i
        print(index)
        result.append(A[index])
        print(result)

    return result


# exam
A = []
K = 3
solution(A, K)
