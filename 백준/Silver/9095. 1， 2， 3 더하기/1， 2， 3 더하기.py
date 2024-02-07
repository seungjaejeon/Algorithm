import sys
T = int(sys.stdin.readline())
dp = [0 for i in range(12)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(T):
    n = int(sys.stdin.readline())
    # 중복을 허용한다.
    # 1+3, 3+1은 다른 경우이다.
    # 1로 끝나는 경우 + 2로 끝나는 경우 + 3으로 끝나는 경우를 합하는 DP테이블을 만든다.
    # 점화식 -> DP[n] = DP[n-1] + DP[n-2] + DP[n-3] = 1로 끝나는 경우 + 2로 끝나는 경우 + 3으로 끝나는 경우
    print(dp[n])