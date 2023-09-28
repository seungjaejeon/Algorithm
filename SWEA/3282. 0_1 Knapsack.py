T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    V = []
    C = []
    dp = [[0 for i in range(K+1)] for j in range(N+1)]
    for i in range(N):
        v, c = map(int, input().split())
        V.append(v)
        C.append(c)

    for i in range(1, N+1):
        for k in range(K+1):
            if k >= V[i-1]:
                dp[i][k] = max(dp[i-1][k-V[i-1]]+C[i-1], dp[i-1][k])
            else:
                dp[i][k] = dp[i-1][k]
    print(dp[N][K])