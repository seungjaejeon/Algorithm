T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    result = 0
    for i in range(N):
        x, y = map(int, input().split())
        r2 = x*x + y*y
        p = r2//400
        # 10 -> 0~1
        # 9 -> 1~4
        # 8 -> 4~9....
        score = pow(p,1/2)
        result += (10-int(score))
    print(f'#{test_case} {int(result)}')