import sys
from collections import deque
N,M,V = map(int, sys.stdin.readline().split())
dic = {}
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if a not in dic:
        dic[a] = [b]
    else:
        dic[a].append(b)
    if b not in dic:
        dic[b] = [a]
    else:
        dic[b].append(a)
for i in dic.values():
    i.sort(reverse = True)
print(dic)

# dfs stack or 재귀
# bfs queue