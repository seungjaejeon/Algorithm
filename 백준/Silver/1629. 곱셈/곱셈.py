import sys

A, B, C = map(int, sys.stdin.readline().split())


def divide2(a, b):
    if b == 1:
        return a % C
    temp = divide2(a, b//2)
    if b % 2 == 0:
        return temp * temp % C
    else:
        return temp * temp * a % C


print(divide2(A, B))
