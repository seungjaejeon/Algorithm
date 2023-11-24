import sys
from collections import deque
T = int(sys.stdin.readline())
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def bfs(x,y):
    global count
    count += 1
    q = deque()
    q.append((x,y))
    while q:
        a, b = q.popleft()
        pan[a][b] = 0
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            if na>=N or nb>=M or na<0 or nb<0:
                continue
            if pan[na][nb] == 1:
                pan[na][nb] = 0
                q.append((na,nb))
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    pan = [[0 for i in range(M)] for j in range(N)]
    for i in range(K):
        x, y = map(int, sys.stdin.readline().split())
        pan[y][x] = 1
    count = 0
    for i in range(N):
        for j in range(M):
            if pan[i][j] == 1:
                bfs(i,j)

    print(count)
    