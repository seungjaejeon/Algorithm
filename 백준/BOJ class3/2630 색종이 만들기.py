import sys
N = int(sys.stdin.readline())
pan = []
for  i in range(N):
    line = list(map(int,sys.stdin.readline().split()))
    pan.append(line)

result = []

def is_right(i,j,n):
    color = pan[i][j]
    for a in range(i, i+n):
        for b in range(j, j+n):
            if color != pan[a][b]:
                is_right(i, j, n//2)
                is_right(i+n//2, j, n//2)
                is_right(i, j+n//2, n//2)
                is_right(i+n//2, j+n//2, n//2)
                return

    if color==1:
        result.append(1)
    elif color == 0:
        result.append(0)

is_right(0,0,N)

print(result.count(0))
print(result.count(1))