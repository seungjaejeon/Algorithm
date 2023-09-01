import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
MAXRANGE = 100001 # N, K의 최대 범위가 100000이다
visited = [-1 for _ in range(MAXRANGE)] # 중복으로 q에 값이 들어감을 방지하기 위한 visited 배열이다.
def bfs(cur):
    q = deque([])
    q.append(cur) # q에 초기값을 넣어준다.
    visited[cur] = 0
    if cur==K:
        return 0
    while q:
        n = q.popleft()
        if n==K: # K에 도달한 값을 출력
            return visited[n]
        for next_n in (2*n, n-1, n+1): # n+1, n-1, 2*n을 모두 시행해보고 조건에 부합하면 q에 더해준다.
            if 0 <= next_n < MAXRANGE and visited[next_n]==-1 and next_n == 2*n: # 방문한적이 없는지, 범위내에 존재하는지 확인한다.
                q.append(next_n)
                visited[next_n] = visited[n]
            elif 0 <= next_n < MAXRANGE and visited[next_n]==-1 and next_n != 2*n:
                q.append(next_n)
                visited[next_n] = visited[n] +1

print(bfs(N))
