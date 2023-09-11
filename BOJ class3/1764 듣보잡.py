import sys
N, M = map(int, sys.stdin.readline().split())
dic = dict()
result = []
for i in range(N):
    canthear = sys.stdin.readline().strip()
    dic[canthear] = 1

for i in range(M):
    cantsee = sys.stdin.readline().strip()
    if cantsee in dic:
        result.append(cantsee)
result.sort()
print(len(result))
for i in result:
    print(i)