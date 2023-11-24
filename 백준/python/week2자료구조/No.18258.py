import sys
from collections import deque
queue = deque([])
N = int(sys.stdin.readline())
for i in range(N):
    con = list(sys.stdin.readline().rstrip().split())
    if con[0] == "push":
        queue.append(con[1])
    if con[0] == "pop":
        print(queue.popleft()) if queue else print(-1)
    if con[0] == "size":
        print(len(queue))
    if con[0] == "empty":
        print(0) if queue else print(1)
    if con[0] == "front":
        print(queue[0]) if queue else print(-1)
    if con[0] == "back":
        print(queue[-1]) if queue else print(-1)
