import sys
from collections import deque
R, C = map(int, sys.stdin.readline().split())
pan = []
for i in range(R):
    line = list(sys.stdin.readline().strip())
    pan.append(line)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(original, x, y):
    max_len = 1
    q = set([(x, y, original[y][x])])  # set로 변경
    while q:
        x, y, alpha = q.pop()  # pop으로 변경
        max_len = max(max_len, len(alpha))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < C and 0 <= ny < R and original[ny][nx] not in alpha:
                q.add((nx, ny, alpha + original[ny][nx]))  # add로 변경

    return max_len

print(bfs(pan, 0, 0))
    