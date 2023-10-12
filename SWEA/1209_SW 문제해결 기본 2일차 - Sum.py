T = 10
for _ in range(10):
    test_case = int(input())
    result = 0
    pan = [0 for i in range(100)] # 세로의 합을 저장할 배열
    cnt = 0 
    cnt1 = 0 
    for i in range(100):
        line = list(map(int, input().split()))
        result = max(result, sum(line)) # 가로의 합
        cnt += line[i] # 아래 오른쪽 대각선의 합을 저장할 cnt
        cnt1 += line[99-i] # 아래 왼쪽 대각선의 합을 저장할 cnt1
        for j in range(100):
            pan[j]+= line[j] # 세로값 저장
    
    result = max(result, max(pan), cnt, cnt1) #최댓값 
    print(f'#{test_case} {result}')