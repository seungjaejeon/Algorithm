import sys
from collections import deque
T = int(sys.stdin.readline())
for i in range(T):
    error = 1
    num = deque()
    com = str(sys.stdin.readline().rstrip())
    N = int(sys.stdin.readline())
    string = str(sys.stdin.readline().rstrip())
    for j in string:
        if ord(j) == 91 or ord(j) == 93 or ord(j) == 44:
            continue
        else:
            num.append(j)
    for k in com:
        if k == "R":
            num.reverse()
        if k == "D":
            if len(num) == 0 :
                error = 0
            else: num.popleft()
    if error == 1:
        print("[", end="")
        result = ",".join(map(str, num))
        print(result,end="")
        print("]")
    else:
        print("error")
