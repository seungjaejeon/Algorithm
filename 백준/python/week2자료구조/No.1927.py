from heapq import heappop, heappush
import sys
heap = []
N = int(sys.stdin.readline())
for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        print(heappop(heap)) if heap else print(0)
    else:
        heappush(heap, x)