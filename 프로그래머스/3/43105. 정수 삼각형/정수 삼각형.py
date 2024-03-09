def solution(triangle):
    answer = 0
    N = len(triangle)
    dp = [[0 for i in range(N)] for j in range(N)]
    dp[0][0] = triangle[0][0]
    for i in range(1, N):
        for j in range(i+1):
            dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])
    return max(dp[-1])