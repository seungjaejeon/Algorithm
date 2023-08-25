import sys
from collections import deque
N, M, H = map(int, sys.stdin.readline().split())
box = [] # 3차원 H, M, N
for i in range(H):
    pan = []
    for j in range(M):
        pan.append(list(map(int, sys.stdin.readline().split())))
    box.append(pan)

dx = [0,0,-1,1,0,0] # 상하좌우앞뒤
dy = [1,-1,0,0,0,0]
dz = [0,0,0,0,-1,1]

q = deque()
for i in range(H):
    for j in range(M):
        for k in range(N):
            if box[i][j][k]==1:
                q.append((i,j,k,0))

age = []

def bfs():
    while q:
        x,y,z,count = q.popleft()
        age.append(count+1)
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx<0 or ny<0 or nz<0 or nx>=H or ny>=M or nz>=N:
                continue
            if box[nx][ny][nz]==0:
                box[nx][ny][nz] = 1
                q.append((nx,ny,nz,count+1))

bfs()
flag = True

for i in range(H):
    for j in range(M):
        for k in range(N):
            if box[i][j][k]==0:
                flag = False

if flag==False:
    print(-1)
else:
    print(max(age)-1)