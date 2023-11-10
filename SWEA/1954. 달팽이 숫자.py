T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    pan = [[0 for i in range(N)] for j in range(N)]
    dx = [0,1,0,-1] # 우하좌상
    dy = [1,0,-1,0]
    def snail(x,y,d,num):
        pan[x][y] = num
        nx = x + dx[d]
        ny = y + dy[d]
        if num==N*N:
            return
        if nx < 0 or ny <0 or nx>=N or ny >= N or pan[nx][ny]!=0: # 끝에 도달하면 방향 전환
            d = (d+1)%4
            snail(x,y,d,num)
        else: 
            snail(nx,ny,d,num+1)
            
    
    snail(0,0,0,1)
    print(f'#{test_case}')
    for i in range(N):
        for j in range(N):
            print(pan[i][j], end=" ")
        print()