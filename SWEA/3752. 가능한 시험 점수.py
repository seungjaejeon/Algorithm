# T = int(input())
# def dfs(index, total):
#     if index == N:
#         result.append(total)
#         return
#     dfs(index+1, total+score[index])
#     dfs(index+1, total)
#     return
# for test_case in range(1, T + 1):
#     N = int(input())
#     score = list(map(int, input().split()))
#     result = []
#     dfs(0,0)
#     answer = len(set(result))
#     print(f'#{test_case} {answer}')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    dp = [0 for _ in range(10000)]
    score = list(map(int, input().split()))
    dp[0] = 1
    result = [0]
    temp = [0]
    for i in range(N):
        for j, val in enumerate(result):
            temp.append(result[j]+score[i])
        result = list(set(temp))
    print(f'#{test_case} {len(result)}')
    