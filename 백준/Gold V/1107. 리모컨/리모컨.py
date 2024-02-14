import sys
from collections import deque
start = 100
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
if M != 0:
    miss = list(map(int, sys.stdin.readline().split()))
else:
    miss = []
result = abs(N-start)
for i in range(1000000):
    for j in str(i):
        if int(j) in miss:
            break
    else:
        result = min(result, len(str(i))+abs(N-i))

print(result)

# 숫자 누르기
# + or -
# 횟수