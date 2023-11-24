import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
queue = deque([i for i in range(1, N+1)])
count = 0
for number in num:
    if queue.index(number) < len(queue)/2:
        while number != queue[0]:
            queue.append(queue.popleft())
            count += 1
    else:
        while number != queue[0]:
            queue.appendleft(queue.pop())
            count += 1 
    if number == queue[0]:
        queue.popleft()
print(count)