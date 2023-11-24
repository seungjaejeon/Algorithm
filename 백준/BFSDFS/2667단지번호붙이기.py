import sys
from collections import deque
N = int(sys.stdin.readline())
house = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
# 이어져있는 집들 확인 (BFS)
# 이어져있는 집들의 개수 count 리스트에 넣고 sort하여 내림차순으로 정리

dx = [0,0,-1,1]
dy = [1,-1,0,0]
count = []  
def bfs(a, b):
    q = deque()
    friend = 1
    q.append((a,b))
    house[a][b] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i] 
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if house[nx][ny]==1:
                q.append((nx,ny))
                house[nx][ny] = 0
                friend += 1
    count.append(friend)

for i in range(N):
    for j in range(N):
        if house[i][j] == 1:
            bfs(i, j)

print(len(count))
count.sort(reverse=True)
while count:
    print(count.pop())
