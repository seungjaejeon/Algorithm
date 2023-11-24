from heapq import heappop, heappush
import sys
heap_minus = []
heap_plus = []
N = int(sys.stdin.readline())
for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap_plus) + len(heap_minus) == 0: # 배열이 비어있는 경우
            print(0)
        elif len(heap_plus) == 0: 
            print(-heappop(heap_minus))
        elif len(heap_minus) == 0:
            print(heappop(heap_plus))
        else:
            if heap_minus[0]>heap_plus[0]: # 양수힙의 최솟값이 더 작을경우
                print(heappop(heap_plus))
            else:
                print(-heappop(heap_minus)) # 음수힙의 최솟값이 더 작을경우, 같을경우
        
    elif x > 0:
        heappush(heap_plus, x) # plus에 push
    else: 
        heappush(heap_minus, -x) # minus에 push
