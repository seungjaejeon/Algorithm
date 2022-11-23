import sys
def fib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)
n = int(sys.stdin.readline())
print(fib(n))