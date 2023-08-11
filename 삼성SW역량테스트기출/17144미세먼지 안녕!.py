import sys
R,C,T = map(int, sys.stdin.readline().split())
pan = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
# 미세먼지 확산시키는 함수 동시에 일어나야 함
# 공기청정기 돌리는 함수
# T번 돌리고 미세먼지 총량 출력
cur = []
cleaner = []
def spread():
    while cur:
        x,y,value = cur.pop()
        count = 0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=R or ny>=C:
                continue
            if (nx,ny) in cleaner:
                continue
            pan[nx][ny]+=value//5
            count+=1
        pan[x][y] -= (value//5)*count
def clean(a,b):
    # 위에 회전
    x, y = a, 1
    index = 1 # 우부터 시작 우 상 좌 하
    temp = 0 # 공기청정기에서 나오는 바람
    while True:
        nx = x+dx[index]
        ny = y+dy[index]
        if nx==R or ny == C or nx==-1 or ny==-1: # 벽에 닿았을 때
            index = (index-1)%4
            continue
        if x==a and y==0: # 공기청정기로 다시 돌아옴
            break
        pan[x][y], temp = temp, pan[x][y] # swap
        x,y = nx, ny
    # 아래 회전
    x, y = b, 1
    index = 1 # 우부터 시작 우 하 좌 상
    temp = 0 # 공기청정기에서 나오는 바람
    while True:
        nx = x+dx[index]
        ny = y+dy[index]
        if nx==R or ny == C or nx==-1 or ny==-1: # 벽에 닿았을 때
            index = (index+1)%4
            continue
        if x==b and y==0: # 공기청정기로 다시 돌아옴
            break
        pan[x][y], temp = temp, pan[x][y] # swap
        x,y = nx, ny

for i,line in enumerate(pan):
        for j, value in enumerate(line):
            if value>0:
                cur.append((i,j,value))
            if value==-1:
                cleaner.append((i,j))
dx = [-1,0,1,0] # 상 우 하 좌
dy = [0,1,0,-1]           
a = cleaner[0][0] # 공기청정기의 윗부분
b = cleaner[1][0] # 공기청정기의 아랫부분
for t in range(T):
    
    spread()
    clean(a,b)
    for i,line in enumerate(pan):
        for j, value in enumerate(line):
            if value>0:
                cur.append((i,j,value))

    print()
    for i in range(R):
        for j in range(C):
            print(pan[i][j], end=" ")
        print()

print(sum(cur[i][2] for i in range(len(cur))))


# [[0, 0, 0, 0, 0, 1, 8, 6], [0, 0, 1, 0, 3, 0, 5, 5], [-1, 0, 2, 1, 1, 0, 4, 6], [-1, 0, 5, 2, 0, 0, 2, 12], [0, 1, 1, 0, 5, 10, 13, 0], [0, 1, 9, 4, 3, 5, 12, 8], [8, 17, 8, 3, 4, 8, 4, 0]]
# [[0, 0, 0, 0, 2, 7, 6, 5], [0, 0, 1, 0, 3, 1, 3, 6], [-1, 0, 0, 3, 1, 1, 0, 6], [-1, 0, 1, 1, 3, 1, 2, 6], [1, 1, 3, 1, 3, 6, 9, 7], [9, 5, 6, 5, 5, 6, 8, 5], [10, 9, 4, 5, 6, 7, 1, 7]]
# [[0, 0, 0, 3, 5, 5, 5, 5], [0, 0, 1, 0, 3, 2, 5, 5], [-1, 0, 0, 0, 3, 1, 1, 1], [-1, 0, 0, 1, 1, 3, 2, 4], [9, 2, 4, 2, 5, 4, 8, 5], [8, 4, 4, 4, 4, 6, 7, 7], [9, 7, 4, 6, 6, 4, 6, 5]]
# [[0, 0, 4, 3, 4, 5, 5, 4], [0, 0, 1, 0, 4, 4, 3, 2], [-1, 0, 0, 0, 0, 3, 1, 2], [-1, 0, 0, 0, 1, 2, 3, 3], [7, 3, 4, 3, 1, 7, 6, 5], [9, 6, 4, 5, 7, 3, 7, 4], [5, 6, 4, 4, 7, 5, 5, 7]]
# [[0, 4, 3, 5, 3, 3, 5, 2], [0, 0, 1, 0, 4, 5, 4, 2], [-1, 0, 0, 0, 0, 0, 3, 1], [-1, 0, 0, 0, 0, 1, 3, 4], [9, 5, 4, 4, 3, 4, 5, 4], [5, 4, 6, 2, 5, 7, 5, 3], [5, 5, 6, 6, 4, 5, 6, 7]]