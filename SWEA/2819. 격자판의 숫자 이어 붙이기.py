T = int(input())
for test_case in range(1, T + 1):
    pan = []
    for i in range(4):
        line = list(map(str, input().strip().split()))
        pan.append(line)
    answer = []
    def dfs(x,y, result):
        if x<0 or y<0 or x>=4 or y>=4:
            return
        result+=pan[x][y]
        if len(result)==7:
            answer.append(result)
            return
        dfs(x+1,y,result) # 하
        dfs(x,y+1,result) # 우
        dfs(x-1,y,result) # 상
        dfs(x,y-1,result) # 좌
    for i in range(4):
        for j in range(4):
            dfs(i,j,'')
    print(f'#{test_case} {len(set(answer))}')