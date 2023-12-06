import sys
import heapq

def dijkstra(s, edge):
    dist = [float('inf')] * (n+1)
    q = []
    heapq.heappush(q,(s,0))
    while q:
        w,d = heapq.heappop(q)
        if dist[w] < d:
            continue
        for nxt, c in edge[w]:
            if dist[nxt] > d + c:
                dist[nxt] = d+c
                heapq.heappush(q,(nxt,d+c))
    return dist

n,m,x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, c = map(int, sys.stdin.readline().split())
    graph[start].append((end, c))
    reverse_graph[end].append((start, c))
back = dijkstra(x, reverse_graph)
go = dijkstra(x, graph)

answer = 0
for i in range(1, n+1):
    if i != x:
        answer = max(answer, go[i] + back[i])

print(answer)