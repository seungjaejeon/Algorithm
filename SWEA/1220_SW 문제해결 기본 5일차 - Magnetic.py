from collections import deque
T = 10
for test_case in range(1, T + 1):
    N = int(input())
    pan = []
    for i in range(N):
        line = list(map(int, input().split()))
        pan.append(line)

    
    result = 0
    for i in range(N):
        q = deque()
        for j in range(N):
            if pan[j][i]!=0:
                q.append(pan[j][i])
        flag = 0
        for val in q:
            if val==1 and flag==0:
                flag=1       
            if val==2 and flag==1:
                result += 1
                flag=0
    print(f'#{test_case} {result}')
    # 교착상태의 경우
    # 한 라인에 N, S가 있을 때
    # N이 위쪽, S가 아래쪽에 있을때