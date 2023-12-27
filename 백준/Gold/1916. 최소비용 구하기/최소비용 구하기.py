import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
bus = [[] for i in range(N + 1)]
for i in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    bus[start].append((end, cost))

s, e = map(int, sys.stdin.readline().split())
dist = [float('inf') for i in range(N + 1)]


def dijkstra(s):
    q = []
    dist[s] = 0
    heapq.heappush(q, (0, s))
    while q:
        c, x = heapq.heappop(q)
        if dist[x] < c:
            continue
        for nxt, cost in bus[x]:
            dist_cost = c + cost
            if dist[nxt] > dist_cost:
                dist[nxt] = dist_cost
                heapq.heappush(q, (dist_cost, nxt))



dijkstra(s)
print(dist[e])
