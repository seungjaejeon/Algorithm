import sys
def bell(startnode):
    distance[startnode] = 0
    for i in range(N):
        for edge in edges:
            cur_node, next_node, cost = edge
            if distance[next_node] > distance[cur_node] + cost:
                distance[next_node] = distance[cur_node] + cost
                if i == N-1:
                    return True
    return False

TC = int(sys.stdin.readline())
for i in range(TC):
    N, M, W = map(int, sys.stdin.readline().split())
    edges = []
    distance = [2000000000 for j in range(N+1)]
    for j in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    for j in range(W):
        S, E, T = map(int, sys.stdin.readline().split())
        edges.append((S, E, -T))

    if(bell(1)):
        print('YES')
    else:
        print('NO')
