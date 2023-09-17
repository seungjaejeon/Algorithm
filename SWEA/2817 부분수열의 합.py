T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def dfs(i, result):
    global count
    if result == K:
        count += 1
        return
    if i == N:
        return
    dfs(i + 1, result + number[i])
    dfs(i+1, result)
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    number = list(map(int, input().split()))
    count = 0
    dfs(0, 0)
    print(f'#{test_case} {count}')