import sys
n = int(sys.stdin.readline())
for i in range(n):
    count = 0
    str = sys.stdin.readline().rstrip()
    for char in str:
        if char == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            break
    if count == 0:
        print("YES")
    else: print("NO")