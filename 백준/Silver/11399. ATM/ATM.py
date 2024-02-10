# shortjobfirst 알고리즘

import sys
N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
P.sort()
wating_time = 0
result = 0
for i in P:
    wating_time += i
    result += wating_time

print(result)