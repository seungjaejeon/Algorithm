import sys
import heapq
V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
node = [[] for i in range(V+1)]
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    node[u].append((v, w))

dist = [float('INF') for i in range(V+1)]


def dijkstra(s):
    q = []
    dist[K] = 0
    heapq.heappush(q, (0, s))
    while q:
        c, x = heapq.heappop(q)
        if dist[x] < c:
            continue
        for nxt, cost in node[x]:
            dist_cost = c+cost
            if dist[nxt] > dist_cost:
                dist[nxt] = dist_cost
                heapq.heappush(q, (dist_cost, nxt))


dijkstra(K)

for i in range(1, V+1):
    if dist[i] >= float('inf'):
        print("INF")
    else:
        print(dist[i])