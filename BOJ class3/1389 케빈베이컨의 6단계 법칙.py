import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
friend = [[] for i in range(N+1)]
for i in range(M):
    a,b = map(int, sys.stdin.readline().split())
    friend[a].append(b) # 입력값 2차원 배열에 저장
    friend[b].append(a)
def bfs(start): # BFS함수 생성
    q = deque()
    q.append(start) # 초기 값 넣기
    while q: # 모든 연결 가능한 사람까지의 케빈 베이컨 수 구하기
        cur_man = q.popleft() # 현재 사람
        for next_man in friend[cur_man]: # 현재 사람과 연결되어 있는 사람들
            if visited[next_man]==0 and start!=next_man: # 그 사람까지 도달한 적이 없다면 
                visited[next_man] = visited[cur_man] + 1# 현재사람까지의 케빈 베이컨 수 + 1
                q.append(next_man) # 다음사람을 큐에 추가

result = float('inf') # 초기값
for i in range(1, N+1): # 1번 사람부터 N번 사람까지 
    visited = [0 for i in range(N+1)] # kevin 수를 저장할 visited
    bfs(i) # 1번 사람으로부터 시작
    kevin = sum(visited) # 케빈 베이컨 수는 방문할 수 있는 모든 사람들까지의 단계의 합이므로
    if kevin < result: # 그렇게 1번 사람부터 N번 사람까지의 케빈 베이컨중 가장 작은 케빈 베이컨을 가진 사람을 min_kevin_man에 저장
        result = kevin
        min_kevin_man = i

print(min_kevin_man) # 결과 출력

# 1에서 2 + 1에서 3 + 1에서 4 + ... + 1에서 N => 1의 케빈베이컨 수 