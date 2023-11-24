from collections import deque
import sys
n = int(sys.stdin.readline())
Deque = deque()
for i in range(n):
    sen = list(map(str, sys.stdin.readline().rstrip().split()))
    if sen[0] == "push_front":
        Deque.appendleft(sen[1])
    if sen[0] == "push_back":
        Deque.append(sen[1])
    if sen[0] == "pop_front":
        print(Deque.popleft()) if Deque else print(-1)
    if sen[0] == "pop_back":
        print(Deque.pop()) if Deque else print(-1)
    if sen[0] == "size":
        print(len(Deque))
    if sen[0] == "empty":
        print(0) if Deque else print(1)
    if sen[0] == "front":
        print(Deque[0]) if Deque else print(-1)
    if sen[0] == "back":
        print(Deque[-1]) if Deque else print(-1)
         