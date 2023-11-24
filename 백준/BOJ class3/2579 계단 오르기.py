import sys
N = int(sys.stdin.readline())
stair = [0]
for i in range(N):
    stair.append(int(sys.stdin.readline()))

dp = [0 for i in range(N+1)]
dp[1] = stair[1]
count = 0
for i in range(2, N+1):
    dp[i] = max(dp[i-3] +stair[i-1]+ stair[i], dp[i-2] + stair[i])

print(dp[N])