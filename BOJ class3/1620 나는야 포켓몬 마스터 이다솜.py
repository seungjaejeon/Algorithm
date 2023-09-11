import sys
N, M = map(int, sys.stdin.readline().split())
poketmon = dict()
number = dict()
for i in range(1, N+1):
    po = sys.stdin.readline().strip()
    poketmon[i] = po# O(N)
    number[po] = i

for i in range(M):
    find = sys.stdin.readline().strip()
    if find[0].isalpha():
        print(number[find]) # O(M)
    else:
        print(poketmon[int(find)])