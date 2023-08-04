from collections import deque
import sys
# 드래곤 커브 모양 구현 
# 회전시키기
# 1*1정사각형 개수 구하기 
pan = [[0] * 101 for _ in range(101)]
# 0: 우 1: 상 2: 좌 3: 하
# 우로 시작하는 dp

N = int(sys.stdin.readline())
dx = [1, 0, -1, 0]
dy = [0, -1, 0 ,1]
for _ in range(N):
    x,y,d,g = map(int,sys.stdin.readline().split())

    pan[y][x] = 1
    dp = [[d],[],[],[],[],[],[],[],[],[],[]]
    for i in range(1,g+1):
        for j in range(len(dp[i-1])):
            dp[i].append(dp[i-1][j])
        for k in range(len(dp[i-1])-1,-1,-1):
            dp[i].append((dp[i-1][k]+1)%4)
    for t in dp[g]:
        x += dx[t]
        y += dy[t]
        pan[y][x] = 1
answer = 0
for i in range(100):
    for j in range(100):
        if pan[i][j] == 1 and pan[i + 1][j] == 1 and pan[i][j + 1] == 1 and pan[i + 1][j + 1] == 1:
            answer += 1
    print(pan[i])
print(answer)