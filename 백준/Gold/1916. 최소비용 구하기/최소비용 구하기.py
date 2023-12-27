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
    heapq.heappush(q, (s, 0))
    while q:
        x, c = heapq.heappop(q)
        if dist[x] < c:
            continue
        for nxt, cost in bus[x]:
            if dist[nxt] > c + cost:
                dist[nxt] = c + cost
                heapq.heappush(q, (nxt, dist[nxt]))


dijkstra(s)
print(dist[e])
