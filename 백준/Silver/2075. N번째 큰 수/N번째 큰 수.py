import sys
import heapq
N = int(sys.stdin.readline())
pan = []
heapq.heapify(pan)
for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if len(pan) < N:
            heapq.heappush(pan, line[j])
        else:
            if pan[0] < line[j]:
                heapq.heappop(pan)
                heapq.heappush(pan, line[j])

print(pan[0])