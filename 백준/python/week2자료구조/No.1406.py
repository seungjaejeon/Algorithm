import sys
str = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())
ch = list(str)
chright = []
for i in range(n):
    con = sys.stdin.readline().split()
    if con[0] == "L":
        if len(ch)!= 0:
            chright.append(ch.pop())
    elif con[0] == "D":
        if len(chright)!=0:
            ch.append(chright.pop())
    elif con[0] == "B":
        if len(ch)!= 0:
            ch.pop()
    elif con[0] == "P":
        ch.append(con[1])
result = ch + chright[::-1]
for i in result:
    print(i, end = "")