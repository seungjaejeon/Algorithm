def star(a, b):
    if a == 1:
        return
    if b == 1:
        return
    for i in range(a//3, 2*a//3):
        for j in range(b//3, 2*b//3):
            s[i][j] = " "
    
    star(a//3, b//3)

import sys
n = int(sys.stdin.readline())
s = [["*" for i in range(n)] for j in range(n)]
t = n
star(n, n)
for i in range(n):
    for j in range(n):
        print(s[i][j], end="")
    print("")