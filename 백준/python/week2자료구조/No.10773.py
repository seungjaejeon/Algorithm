import sys
stack = []
K = int(sys.stdin.readline())
for i in range(K):
    n = int(sys.stdin.readline())
    if n != 0:
        stack.append(n)
    else: stack.pop()
print(sum(stack))
