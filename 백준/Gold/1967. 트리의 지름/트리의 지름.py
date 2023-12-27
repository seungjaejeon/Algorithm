import sys
import heapq

N = int(sys.stdin.readline())
tree = [[] for i in range(N + 1)]
for i in range(N-1):
    start, end, d = map(int, sys.stdin.readline().split())
    tree[start].append((end, d))
    tree[end].append((start, d))



def dijkstra(s):
    q = []
    dist = [float('inf') for i in range(N + 1)]
    dist[s] = 0
    dist[0] = 0
    heapq.heappush(q, (0, s))
    while q:
        c, x = heapq.heappop(q)
        if dist[x] < c:
            continue
        for nxt, cost in tree[x]:
            dist_cost = c + cost
            if dist[nxt] > dist_cost:
                dist[nxt] = dist_cost
                heapq.heappush(q, (dist_cost, nxt))

    return dist

start1 = dijkstra(1)
result = dijkstra(start1.index(max(start1)))
if N>1:
    print(max(result))
else:
    print(0)