dx = [0,0,1,1,1,-1,-1,-1]
dy = [1,-1,1,-1,0,1,-1,0]
def dfs(i, j, d, count):
    global result
    if count >= 5:
        result = "YES"
        return
    nx = i + dx[d]
    ny = j + dy[d]
    if nx<0 or ny<0 or nx>=N or ny>=N:
        return
    if pan[nx][ny]==1:
        dfs(nx, ny, d, count + 1)
    else:
        return
T = int(input())
for test_case in range(1, T + 1):
    result = "NO"
    N = int(input())
    pan = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        line = input().rstrip()
        for j, val in enumerate(line):
            if val == '.':
                pan[i][j] = 0
            else:
                pan[i][j] = 1
    for i in range(N):
        for j in range(N):
            if pan[i][j]==1:
                for d in range(8):
                    dfs(i,j,d,1)
            if result=="YES":
                break
    print(f'#{test_case} {result}')
                