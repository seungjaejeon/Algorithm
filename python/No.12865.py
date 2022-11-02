N, K = map(int, input().split())
W, V = []
temp = K
for i in range(N):
    W[i], V[i] = map(int, input().split())
dp = []
for i in range(N):
    temp - W[i]
    