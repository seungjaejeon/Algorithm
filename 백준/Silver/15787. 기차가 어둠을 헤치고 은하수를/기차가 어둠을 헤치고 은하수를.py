import sys

N, M = map(int, sys.stdin.readline().split())
train = [0 for i in range(N)]

for i in range(M):
    line = list(map(int, sys.stdin.readline().split()))
    line[1] = line[1]-1
    if line[0] == 1:
        num = 2**(line[2]-1)
        if train[line[1]] & num != num:
            train[line[1]] += num
    elif line[0] == 2:
        num = 2**(line[2]-1)
        if train[line[1]] & num == num:
            train[line[1]] -= num
    elif line[0] == 3:
        if train[line[1]] & 2**19 == 2**19:
            train[line[1]] -= 2**19
        train[line[1]] = train[line[1]] << 1
        
    elif line[0] == 4:
        if train[line[1]] & 2**0 == 2**0:
            train[line[1]] -= 2**0
        train[line[1]] = train[line[1]] >> 1

result = set(train)


print(len(result))
