
from collections import deque
T = int(input())
dx = [1,-1,0,0]
dy = [0,0,-1,1]
for test_case in range(1, T + 1):
    N = int(input())
    pan = []
    visited = [[0 for i in range(N)] for j in range(N)]
    def bfs(a,b): # BFS로 세대 정하기
        q = deque()
        q.append((a,b))
        visited[a][b] = 1
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<0 or ny<0 or nx>=N or ny >= N:
                    continue
                if visited[nx][ny]==0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
    for i in range(N):
        pan.append(list(input()))
    result = 0
    bfs(N//2,N//2)
    for i in range(N):
        for j in range(N): 
            if visited[i][j] <= N//2+1: # N/2세대 이하인 부분을 result에 출력하도록 한다.
                result += int(pan[i][j])
                
    print(f'#{test_case} {result}') 
