T = int(input())
def lis():
    for i in range(1, N): # 1부터 끝까지
        for j in range(i-1, -1, -1): # i번째 인덱스보다 1작은 곳부터 0까지
            if num[j] < num[i]: # num[i]가 뒤에 붙으려면 당연히 그 전의 수가 더 작아야 함
                dp[i] = max(dp[i], dp[j] + 1) # 마지막이 num[j]로 끝나는 가장 긴 수열 뒤에 num[i]를 붙임
    return max(dp) # 가장 긴 문자열의 길이 반환
for test_case in range(1, T + 1):
    N = int(input())
    dp = [1 for i in range(N)]
    num = list(map(int, input().split()))
    print(f'#{test_case} {lis()}')

