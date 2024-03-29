# 알고리즘 및 수행시간
# 우선 두가지의 경우로 나뉜다. 그 이유는 한 자리에 10이 들어갈 수 없기 때문이다.
# 첫째 S가 9보다 작거나 같을 경우는 dp[L-1][S] + dp[L][S-1]이다.
# 그 이유는 L자리의 S합을 가지는 경우를 출력하고자 했을 때
# 이는 결국 맨 앞에 1이 온다고 가정하고 L-1자리에 S-1합을 가지는 경우 + 2가 온다고 가정 후 L-1자리에 S-1합을 가지는경우 ... k가 온다고 가정 후 L-1자리에 S-1합을 가지는 경우이다.
# 따라서 dp[L][S-1]값이 위 값중 k-1이 오고 L-1자리에 S-(k-1)합을 가지는 경우까지 더해준 것이므로 여기에 dp[L-1][S]를 더해주면 된다.
# 하지만 이 방식은 0이 앞에 오는것을 고려하지 않은 것인데 dp[i][j]에 0이 오는 것을 고려한 값은 dp[i][j+1]이다. 따라서 dp[L-1][S]를 더해주는 것이다.
# 두번째로 S가 9보다 클 경우이다. 이때도 역시 알고리즘은 같다. 하지만 10의 자리가 오는 것을 고려해야 하기 때문에
# S-9부터 S까지만 dp[L-1][S]를 다 더해준 값이 dp[L][S]이다.
# 수행시간은 for문 3개를 사용하고 있지만 for k in range()구문은 상수번의 반복이므로 따라서 Big-O표기법으로 나타내면 O(n^2)의 수행시간을 가진다.
def solve(L, S):
    for i in range(2, L+1): # 2부터 L까지
        for j in range(2, S+1): # 2부터 S까지
            if j<=9: # 9이하의 dp테이블 채우기
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
            if j>9: # 9보다 큰 dp 테이블 채우기
                for k in range(j-9, j+1): # j-9부터 j까지 
                    dp[i][j] += dp[i-1][k]
            if j>9*i: # L*9가 S보다 작으면 가능한 경우는 0이다.
                dp[i][j] = 0
    return dp[L][S] # dp[L][S]리턴
L, S = [int(x) for x in input().split()]
dp = [[0 for j in range(S + 1)] for i in range(L + 1)] #dp테이블 2차원
for j in range(S+1): # 초기 값 지정 S가 9이하일때 L이 1이면 경우는 1이다.
    dp[1][j]=1
    if j > 9:
        dp[1][j]=0
for i in range(L+1): # 초기 값 지정 L의 자리가 몇이든 합이 1이면 경우의 수는 1이다.
    dp[i][1]=1
print(solve(L, S)%2147483647)
    