import sys
from collections import deque

def spread():
    visited = [[0]*m for i in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if pan[i][j]==2:
                queue.append((i,j))
    while queue:
        x, y = queue.popleft()
        for i in range(4): #상하좌우
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if pan[nx][ny]==0 and visited[nx][ny]==0: #감염
                visited[nx][ny] = 1
                count += 1
                queue.append((nx,ny))
    global answer

    answer = max(result-count,answer)

def wall(wallcount):
    if wallcount==3:
        spread()
        return
    for i in range(n):
        for j in range(m):
            if pan[i][j]==0:
                pan[i][j]=1
                wall(wallcount+1)
                pan[i][j]=0        
n,m = map(int, sys.stdin.readline().split())
pan = []
for i in range(n):
    pan.append(list(map(int,sys.stdin.readline().split())))
result = 0 #초기 공백
for i in range(n):
    for j in range(m):
        if pan[i][j]==0:
            result += 1
dx = [0,0,-1,1]
dy = [-1,1,0,0]
queue = deque()
answer = 0
wall(0)
print(answer-3) # 벽 3개 제거

