import sys
n = int(sys.stdin.readline())
T = [0 for _ in range(n)]
P = [0]*n
for i in range(n):
    T[i], P[i] = map(int,sys.stdin.readline().split())
dp=[0]*(n+1)
for i in range(n):
    for j in range(i+T[i],n+1):
        dp[j] = max(dp[j],dp[i]+P[i])
        print(i,j,dp)
print(dp[-1])