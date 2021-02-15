# problem
# check every binary gap

# Hint
# 1을 만날때마다 연속된 0의 누적값을 리스트에 저장하고 누적값을 다시 0으로 초기화

# inputs / output
# 100101 / [2,1]
# 10000100 / [4]
# 1001000100 / [2,3]


# solve
def solution(N):
    print('solution start')
    print('input', N)
    # 연속된 0의 갯수를 셀 변수
    length = 0
    # output 으로 반환할 결과 배열
    resultArr = []

    # for문으로 detecting
    for i in N:
        # 1일 때
        if int(i) == 1:
            if length != 0:
                resultArr.append(length)
                length = 0
        # 0일 때
        else:
            length += 1

    print('output', resultArr)
    return resultArr


# exam
N = '1001000100'
solution(N)
