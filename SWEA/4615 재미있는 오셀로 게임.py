T = int(input())

dx = [0,0,1,1,-1,-1,1,-1]
dy = [1,-1,0,-1,0,1,1,-1] # 상하좌우대각선

def change(a, b, color, d):
    na = a + dx[d]
    nb = b + dy[d]
    if na < 0 or nb < 0 or na >=N or nb >= N:
        return
    if pan[na][nb] == color:
        return
    if pan[na][nb] != 0 and pan[na][nb] != color:
        pan[na][nb] = color
        change(na, nb, color, d)
    
                
    
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    pan = [[0 for _ in range(N)] for i in range(N)]
    pan[N//2-1][N//2-1] = 2
    pan[N//2][N//2-1] = 1
    pan[N//2-1][N//2] = 1
    pan[N//2][N//2] = 2
    for i in range(M):
        y, x, color = map(int, input().split()) # color == 1? black/ color == 2? white
        pan[x-1][y-1] = color
        for j in range(8):
        	change(x-1, y-1, color, j)
        for t in range(N):
            print(pan[t])