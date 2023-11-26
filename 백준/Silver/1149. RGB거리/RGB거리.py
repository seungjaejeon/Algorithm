import sys
N = int(sys.stdin.readline())
house = [[0,0,0]]
for i in range(N):
    color = list(map(int, sys.stdin.readline().split()))
    house.append(color)

result = float('inf')

dp = [[0 for i in range(3)] for i in range(N+1)]

for i in range(1,N+1):
    dp[i][0] = min(dp[i-1][2],dp[i-1][1]) + house[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + house[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + house[i][2]

print(min(dp[N]))