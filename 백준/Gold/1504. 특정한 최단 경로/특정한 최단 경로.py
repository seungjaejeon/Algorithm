import sys
import heapq

N, E = map(int, sys.stdin.readline().split())
node = [[] for i in range(N+1)]
for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    node[a].append((b, c))
    node[b].append((a, c))

x, y = map(int, sys.stdin.readline().split())
# 1 -> x -> y -> N
# 1 -> y -> x -> N
# 비교

# x와 나머지의 최단거리 -> 1 과 x x와 y x와 N
# y와 나머지의 최단거리 -> 1과 y x와 y y와 N
# 전체 최단거리는 1과x + x와y + y와N, 1과y + x와y + x와N

def dikstra(v):
    dis = [float('inf') for i in range(N+1)]
    q = []
    heapq.heappush(q, (v,0))
    while q:
        n, cost = heapq.heappop(q)
        if dis[n] < cost:
            continue
        for nxt, c in node[n]:
            if dis[nxt] > cost + c:
                dis[nxt] = cost + c
                heapq.heappush(q, (nxt, cost+c))
    return dis

dx = dikstra(x)
dy = dikstra(y)
if x==1 and y==N:
    answer = dx[N]
elif x==1:
    answer = dx[y] + dy[N]
elif y==N:
    answer = dx[1] + dx[N]
else:
    answer = min(dx[1]+dx[y]+dy[N], dy[1]+dy[x]+dx[N])
if answer >= float('inf'):
    print(-1)
else:
    print(answer)