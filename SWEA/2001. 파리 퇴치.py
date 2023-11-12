T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    pan = []
    answer = 0
 
    def sum_pan(x,y,m):
        result = 0
        for i in range(x,x+m):
            for j in range(y, y+m):
                result += pan[i][j]
        return result
 
    for _ in range(N):
        pan.append(list(map(int, input().split())))
    for i in range(N-M+1):
        for j in range(N-M+1):
            answer = max(answer, sum_pan(i, j, M))
 
    print(f'#{test_case} {answer}')