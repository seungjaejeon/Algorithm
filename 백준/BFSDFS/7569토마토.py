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
        age.append(count+1) # 세대 1 증가시키고 넣어주기
        for i in range(6):
            nx = x + dx[i] # 좌표 이동
            ny = y + dy[i]
            nz = z + dz[i]
            if nx<0 or ny<0 or nz<0 or nx>=H or ny>=M or nz>=N: # 인덱스가 범위를 벗어난다면
                continue
            if box[nx][ny][nz]==0: # 익지않은 토마토라면
                box[nx][ny][nz] = 1 # 익히고
                q.append((nx,ny,nz,count+1)) # q에 추가해주기

bfs()
flag = True # 깃발, 익지 않은 토마토가 있다면 False로 바뀜

for i in range(H):
    for j in range(M):
        for k in range(N):
            if box[i][j][k]==0:
                flag = False

if flag==False: # 익지 않은 토마토가 있다면?
    print(-1)
else: # 없다면 세대들 중에서 가장 높은 세대를 출력
    print(max(age)-1)