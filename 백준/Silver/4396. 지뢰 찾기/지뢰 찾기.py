import sys
N = int(sys.stdin.readline())
dx = [0,0,-1,1,1,1,-1,-1]
dy = [1,-1,0,0,-1,1,1,-1]
def find_mine_count(x,y):
    count = 0
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or ny<0 or nx>=N or ny>=N:
            continue

        if pan[nx][ny]=='*':
            count += 1
    return count

def game_over():
    for i in range(N):
        for j in range(N):
            if pan[i][j]=='*':
                open[i][j] = '*'
       
pan = []
open = []
result = [['.' for i in range(N)] for j in range(N)]
for i in range(N):
    line = list(map(str, sys.stdin.readline().strip()))
    pan.append(line)


for i in range(N):
    line = list(map(str, sys.stdin.readline().strip()))
    open.append(line)
gameover = False
for i in range(N):
    for j in range(N):
        if open[i][j]=='x':
            open[i][j] = find_mine_count(i,j)
            if pan[i][j]=='*':
                game_over()
               

for l in open:
    for i in l:
        print(i,end='')
    print()
    
