import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
q = deque([i+1 for i in range(N)])
pus = []
while len(q):
    for i in range(K-1):
        q.append(q.popleft())
    pus.append(q.popleft())
print("<", end="")
for p in pus:
    if pus[-1]==p:
        print(p, end="")
        break
    print("{0}, ".format(p), end="")
print(">")