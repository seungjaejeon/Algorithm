from collections import deque
T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    R = []
    W = []
    waiting = deque([])
    result = 0
    parking = [0 for i in range(n)]
    for i in range(n):
        R.append(int(input()))
    for i in range(m):
        W.append(int(input()))
    for i in range(2*m):
        x = int(input())
        if x > 0: # 들어오는 차라면
            # 이 때 만약 이미 기다리는 사람들이 있다면?
            for j in range(n):
                if parking[j] == 0: # 빈자리가 있다면
                    parking[j] = x # 빈자리에 주차
                    result += R[j]*W[x-1] # 돈 받기
                    break
            else: # 빈자리가 없다면 waiting하기
                waiting.append(x)
        else: # 나가는 차라면
            x = abs(x)
            for j in range(n):
                if parking[j] == x: # 차 뺴요~
                    # 차빠지는데 기다리는 사람이 있다면
                    if len(waiting)>0:
                        x = waiting.popleft()
                        parking[j] = x
                        result += R[j]*W[x-1]
                        break
                    else: 
                        parking[j] = 0
                        break
    print(f'#{test_case} {result}')