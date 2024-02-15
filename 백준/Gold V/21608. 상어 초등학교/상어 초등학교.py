import sys
N = int(sys.stdin.readline())
s = dict()
pan = [[0 for i in range(N)] for j in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for _ in range(N**2):
    line = list(map(int, sys.stdin.readline().split()))
    s_num = line[0]
    s[s_num] = [line[1],line[2],line[3],line[4]]

    can_list = []

    for i in range(N):
        for j in range(N):
            if pan[i][j] == 0: # 빈칸이면
                blank = 0 #주위 빈칸 개수
                like = 0 #주위 좋아하는 사람의 개수
                
                for index in range(4): #주변 확인
                    ni = i + dx[index]
                    nj = j + dy[index]
                    if ni<0 or nj<0 or ni>=N or nj>=N: #예외 제거
                        continue
                    if pan[ni][nj] == 0:
                        blank += 1
                    elif pan[ni][nj] in s[s_num]:
                        like += 1
                can_list.append([i, j, blank, like])
    
    can_list.sort(key=lambda x: (x[3], x[2], -x[0],-x[1]))
    i,j,blank,like = can_list.pop()
    pan[i][j] = s_num
   
result = 0
for i in range(N):
    for j in range(N):
        like = 0 #주위 좋아하는 사람의 개수
        
        for index in range(4): #주변 확인
            ni = i + dx[index]
            nj = j + dy[index]
            if ni<0 or nj<0 or ni>=N or nj>=N: #예외 제거
                continue
           
            if pan[ni][nj] in s[pan[i][j]]:
                like += 1
        
        if like == 0:
            good = 0
        if like == 1:
            good = 1
        if like == 2:
            good = 10
        if like == 3:
            good = 100
        if like == 4:
            good = 1000

        result += good

print(result)