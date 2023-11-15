T = int(input())
for test_case in range(1, T + 1):
    pan = []
    row = [[] for i in range(9)]
    xy = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
    result = 1

    def is_right(linelist):
        for i in range(1,10):
            if i not in linelist:
                return 0
        return 1

    def three_squre(x,y):
        visited = [False for _ in range(10)]
        for i in range(3):
            for j in range(3):
                if visited[pan[x+i][y+j]] == True:
                    return 0
                else:
                    visited[pan[x+i][y+j]] = True
        return 1

    for i in range(9):
        line = list(map(int, input().split()))
        for j in range(9):
            row[j].append(line[j])
        pan.append(line)

    for i in range(9):
        result = result*is_right(pan[i])*is_right(row[i])*three_squre(xy[i][0], xy[i][1])

    print(f'#{test_case} {result}')