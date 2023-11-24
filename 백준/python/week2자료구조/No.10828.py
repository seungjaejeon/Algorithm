import sys
stack = []
n = int(sys.stdin.readline())

for i in range(n):
    line = list(map(str, sys.stdin.readline().split()))
    if line[0] == "push": # push
        stack.append(line[1])
    elif line[0] == "pop": # pop
        print(stack.pop(-1)) if stack else print(-1)
    elif line[0] == "size": # size
        print(len(stack))
    elif line[0] == "empty": # empty
        print(0) if stack else print(1)
    elif line[0] == "top": # top
        print(stack[-1]) if stack else print(-1)         
        