import sys
from collections import deque
N = int(sys.stdin.readline())
node = [[] for i in range(N+1)]
for i in range(N):
    line = deque(map(int, sys.stdin.readline().split()))
    num = line.popleft()
    line.pop()
    while line:
        v = line.popleft()
        d = line.popleft()
        node[num].append((v, d))

def dfs(v):
    for i in node[v]:
        if visited[i[0]]==0:
            visited[i[0]] = visited[v] + i[1]
            dfs(i[0])
    return

result = 0
# 
visited = [0 for _ in range(N+1)]
visited[1] = 1
dfs(1)
end = visited.index(max(visited))
visited = [0 for _ in range(N+1)]
visited[end] = 1
dfs(end)
print(max(visited)-1)