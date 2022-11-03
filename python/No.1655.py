#heap사용
import sys
from heapq import heappush, heappop, heapify
N = int(sys.stdin.readline())
arr = [] #최소힙
brr = [] #최대힙
p = 0
for i in range(N):
    num = int(sys.stdin.readline())
    if i == 0:
        heappush(brr, -num)
        print(-brr[0])
    elif i == 1:
        heappush(arr, num)
        if arr[0] < -brr[0]:
            arr[0], brr[0] = -brr[0], -arr[0]
        print(-brr[0])
    else:
        if len(brr) <= i/2:
            heappush(brr, -num)
        else: 
            heappush(arr, num)
        if arr[0] < -brr[0]:
            heappush(brr, -heappop(arr))
            heappush(arr, -heappop(brr))
        print(-brr[0])