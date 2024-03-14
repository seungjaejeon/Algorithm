from collections import deque
def solution(board):
    N = len(board)
    M = len(board[0])
    dx = [0,0,1,-1] # 오 왼 아래 위
    dy = [1,-1,0,0] # 0 1 2 3
    def go(x,y,i):
        while True:
            x += dx[i]
            y += dy[i]
            if x<0 or y<0 or x >=N or y >= M or board[x][y] == "D": #벽에 막힘
                return x-dx[i], y-dy[i]
            else:
                continue 
    visit = [[0 for i in range(M)] for j in range(N)]
    def bfs(x,y):
        q = deque([])
        q.append([x,y])
        visit[x][y] = 0
        while q:
            a,b = q.popleft()
            for i in range(4):
                nx, ny = go(a,b,i)
                if board[nx][ny] == "G":
                    visit[nx][ny] = visit[a][b] + 1
                    return visit[nx][ny]
                if visit[nx][ny] == 0 and board[nx][ny] == ".":
                    visit[nx][ny] = visit[a][b] + 1
                    q.append([nx,ny])
                elif visit[nx][ny] != 0:
                    continue
        return -1
                
    for i in range(N):
        board[i] = list(board[i])
        for j in range(M):
            if board[i][j] == "R":
                startx, starty = i, j
            if board[i][j] == "G":
                goalx, goaly = i,j
    answer = bfs(startx, starty)
    return answer
