T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    s = []
    k = []
    def dfs(i, taste, kcal):
        global max_taste
        if kcal>L:
            return
        if taste > max_taste:
            max_taste = taste
        if i==N:
            return
        dfs(i+1, taste + s[i], kcal + k[i]) # i번째 재료 선택
        dfs(i+1, taste, kcal) # i번째 재료 미선택
    for _ in range(N):
        score, kcal = map(int, input().split())
        s.append(score)
        k.append(kcal)
    max_taste = 0
    dfs(0,0,0)
    print(f'#{test_case} {max_taste}')
    