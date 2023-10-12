T = 10
for _ in range(10):
    test_case = int(input())
    result = 0
    pan = [[] for i in range(100)]
    for i in range(100):
        line = list(map(int, input().split()))
        result = max(result, sum(line)) # 가로의 합
        for j in range(100):
            pan[j].append(line[j])
    for i in range(100):
        result = max(result, sum(pan[i])) # 세로의 합
    cnt = 0 
    cnt1 = 0 
    for i in range(100):
        cnt += pan[i][i] # 아래 오른쪽 대각선
        cnt1 += pan[i][99-i] # 아래 왼쪽 대각선
    result = max(result, cnt, cnt1) # 최대값 저장
    print(f'#{test_case} {result}')