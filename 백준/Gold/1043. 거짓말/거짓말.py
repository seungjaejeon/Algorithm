
# 첫째 줄에 사람의 수 N과 파티의 수 M이 주어진다.
#
# 둘째 줄에는 이야기의 진실을 아는 사람의 수와 번호가 주어진다. 진실을 아는 사람의 수가 먼저 주어지고 그 개수만큼 사람들의 번호가 주어진다. 사람들의 번호는 1부터 N까지의 수로 주어진다.
#
# 셋째 줄부터 M개의 줄에는 각 파티마다 오는 사람의 수와 번호가 같은 방식으로 주어진다.
#
# N, M은 50 이하의 자연수이고, 진실을 아는 사람의 수는 0 이상 50 이하의 정수, 각 파티마다 오는 사람의 수는 1 이상 50 이하의 정수이다.

from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

know = list(map(int, sys.stdin.readline().split()))
party = []
for i in range(M):
    line = deque(map(int, sys.stdin.readline().split()))
    line.popleft()
    part = list(line)
    party.append(part)

visited = [0 for i in range(M)]
man = [0 for i in range(N+1)]
for i in know:
    man[i] = 1

def bfs():
    q = deque(know)
    q.popleft()
    while q:
        n = q.popleft()
        for i, val in enumerate(party):
            if n in val and visited[i] == 0:
                visited[i] = 1
                for j, val2 in enumerate(val):
                    if n != val2:
                        q.append(val2)

bfs()
print(visited.count(0))

# 이야기의 진실을 아는 사람이 있는 파티는 전부 진실만을 말해야 함
# 진실을 말한 파티에 속해있는 사람들 역시 진실을 알게 됨
# 따라서 연관이 없는 파티에만 과장된 이야기를 할 수 있음