from collections import deque
def solution(maps):
    answer = 0
    N = len(maps)
    M = len(maps[0])
    visitedE = [[-1 for i in range(M)] for j in range(N)]
    for i in range(N):
        for j in range(M):
            if maps[i][j] == "S":
                sx = i
                sy = j
            if maps[i][j] == "L":
                lx = i
                ly = j
            if maps[i][j] == "E":
                ex = i
                ey = j
                
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    def bfs(a, b, visited):
        q = deque()
        q.append([a, b])
        visited[a][b] = 0
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<0 or ny<0 or nx>=N or ny>=M or visited[nx][ny] != -1 or maps[nx][ny] == "X":
                    continue
                q.append([nx,ny])
                visited[nx][ny] = visited[x][y] + 1
                
    bfs(lx, ly, visitedE)
    
    if visitedE[ex][ey]<0 or visitedE[sx][sy]<0:
        return -1
    else:
        return visitedE[sx][sy] + visitedE[ex][ey]
# bfs로 최소시간 구하기
