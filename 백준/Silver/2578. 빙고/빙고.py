import sys
pan = []

for i in range(5):
    line = list(map(int, sys.stdin.readline().split()))
    pan.append(line)

visited = [[0 for i in range(5)] for j in range(5)]

def cal_score():
    bingo = 0
    for i in range(5):
        if sum(visited[i]) == 5:
            bingo += 1
    for i in range(5):
        cnt = 0
        for j in range(5):
            cnt += visited[j][i]
        if cnt == 5:
            bingo += 1
    cnt = 0
    for i in range(5):
        cnt += visited[i][i]
    if cnt==5:
        bingo += 1
    cnt = 0
    for i in range(5):
        cnt += visited[4-i][i]
    if cnt==5:
        bingo += 1
    return bingo
result = 0
for i in range(5):
    call = list(map(int, sys.stdin.readline().split()))
    for n in range(5):
        for x in range(5):
            for y in range(5):
                if call[n]==pan[x][y]:
                    visited[x][y] = 1
        
        if cal_score()>=3 and result==0:
            result = 5*(i) + n+1
            
    
print(result)