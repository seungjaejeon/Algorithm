def gcd(a, b):
    if a * b == 0:
        return a + b
    if a > b: return gcd(b, a%b)
    else: return gcd(a, b%a)

T=int(input())

for i in range(T):
    a, b = map(int, input().split())
    min_num = gcd(a, b)
    print(a*b // min_num)