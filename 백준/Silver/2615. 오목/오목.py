import sys

pan = []
for i in range(19):
    line = list(map(int, sys.stdin.readline().split()))
    pan.append(line)

dx = [1,1,0,1,0,-1,-1,-1]
dy = [0,1,1,-1,-1,0,-1,1]
#d = 0이면 오른쪽, 1이면 오른쪽아래, 2면 아래
def look_start(x, y, wb, i):
    ax = x
    ay = y
    while 1:
        nx = ax - dx[i]
        ny = ay - dy[i]
        if nx<0 or ny<0 or nx>=19 or ny>=19:
            break
        if pan[nx][ny] == wb:
            ax = nx
            ay = ny
        else:
            break
    start_x = ax
    start_y = ay
    return start_x, start_y

def look_d(x, y, wb, i):
    start_x, start_y = look_start(x, y, wb, i)
    ax = start_x
    ay = start_y
    count = 1
    while 1:
        nx = ax + dx[i]
        ny = ay + dy[i]
        if nx<0 or ny<0 or nx>=19 or ny>=19:
            break
        if pan[nx][ny] == wb:
            ax = nx
            ay = ny
            count += 1
        else:
            break
    return count

def is_five(x, y, wb):
    for i in range(8):
        count = 0
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=19 or ny>=19:
            continue
        if pan[nx][ny] == wb:
            count = look_d(x, y, wb, i)
        if count == 5:
            return True

    return False

result = []
win = 0
for i in range(19):
    for j in range(19):
        if pan[i][j]!=0:
            if is_five(i, j, pan[i][j]):
                win = pan[i][j]
                result.append([i+1, j+1])

result.sort(key = lambda x : (x[1], x[0]))
print(win)
if win != 0:
    print(result[0][0], result[0][1])
