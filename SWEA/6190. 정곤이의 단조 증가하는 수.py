T = int(input())
def isitdanjo(d):
    string = str(d)
    for i in range(1, len(string)):
        if string[i-1] > string[i]:
            return False
    return True
for test_case in range(1, T + 1):
    # 입력의 곱들 1자로 나열
    # 그중 단조 확인하면서 최댓값에 저장하기.
    N = int(input())
    A = list(map(int, input().split()))
    danjo = []
    result = -1
    for i in range(N-1):
        for j in range(i+1, N):
            danjo.append(A[i]*A[j])
    for i, val in enumerate(danjo):
        if isitdanjo(val):
            if val>result:
                result = val
        else:
            continue
    print(f'#{test_case} {result}')