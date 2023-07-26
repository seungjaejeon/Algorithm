import sys
N, M, x, y, K = map(int, sys.stdin.readline().split())
ma = []
for i in range(N):
    ma.append(list(map(int, sys.stdin.readline().split())))
d=list(map(int, sys.stdin.readline().split()))

direction = [[0,1],[0,-1],[-1,0],[1,0]]
dice = [0,0,0,0,0,0]
#[1,2,3,4,5,6] 윗면이 1 동쪽이 3 서쪽이 4 아랫면이 6 북쪽이 2 남쪽이 5
# 만약 동쪽으로 이동한다면? => 서쪽이 윗면으로 바뀌고 윗면이 동쪽, 동쪽이 아랫면, 아랫면이 서쪽으로 바뀜 북 남은 그대로
# [4,2,1,6,5,3]
# 서쪽으로 이동한다면? [3,2,6,1,5,4]
# 남쪽으로 이동한다면? [2,6,3,4,1,5]
# 북쪽으로 이동한다면? [5,1,3,4,6,2]
def dicing(d_index):
    a,b,c,d,e,f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if d_index == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d,b,a,f,e,c
    elif d_index == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c,b,f,a,e,d
    elif d_index == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e,a,c,d,f,b
    elif d_index == 4: #남    
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b,f,c,d,a,e
nx = x
ny = y
for d_index in d:
    nx += direction[d_index-1][0]
    ny += direction[d_index-1][1]
    if nx<0 or nx>N-1 or ny<0 or ny>M-1:
        nx -= direction[d_index-1][0]
        ny -= direction[d_index-1][1]
        continue

    dicing(d_index)
    if ma[nx][ny]==0:
        ma[nx][ny] = dice[5]
    else:
        dice[5] = ma[nx][ny]
        ma[nx][ny]=0
    print(dice[0])
