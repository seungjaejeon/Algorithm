import sys
min_l = 0
k, n = map(int, sys.stdin.readline().split())
list_l = []
for i in range(k):
    l = int(sys.stdin.readline())
    list_l.append(l)
    min_l = max(min_l, l)
result = 0
end = min_l
start = 1
t = 0

while start <= end:
    cnt = 0
    mid = (start + end)//2
    for i in list_l:
        cnt += i//mid
    if cnt >= n:
        start = mid + 1
    elif cnt < n:
        end = mid - 1

print(end)