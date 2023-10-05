T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    result = 0
    pan = [[0 for i in range(201)] for j in range(201)]
    for i in range(201):
        for j in range(201):
            score = 11
            p = (i*i+j*j)//400
            if p>100:
                continue
            else:
                pan[i][j] = 10-int(pow(p, 1/2))
    for i in range(N):
        x, y = map(int, input().split())
        result += pan[abs(x)][abs(y)]
    print(f'#{test_case} {int(result)}')