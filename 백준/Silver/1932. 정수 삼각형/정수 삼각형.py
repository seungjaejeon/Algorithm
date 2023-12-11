import sys
N = int(sys.stdin.readline())
tri = []
dp = []
for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    tri.append(line)
    dp.append(line)

for i in range(N-2, -1, -1):
    for j in range(i+1):
        dp[i][j] = max(dp[i+1][j], dp[i+1][j+1]) + tri[i][j]
print(dp[0][0])
