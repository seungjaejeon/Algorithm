import sys
N = int(input())
minl = [0,0,0]
maxl = [0,0,0]
for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    minl = [min(minl[0], minl[1]) + line[0], min(minl)+ line[1], min(minl[1], minl[2])+ line[2]]
    maxl = [max(maxl[0], maxl[1]) + line[0], max(maxl)+ line[1], max(maxl[1], maxl[2])+ line[2]]

print(max(maxl), min(minl))
