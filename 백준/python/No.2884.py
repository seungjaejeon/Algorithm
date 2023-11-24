H, M = map(int, input().split())
last_M = M - 45
last_H = H
if last_M < 0:
    last_M += 60
    last_H -= 1
    if last_H < 0:
        last_H += 24
else: last_H = H
print(last_H, last_M)