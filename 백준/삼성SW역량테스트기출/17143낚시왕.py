import sys
R,C,M = map(int, sys.stdin.readline().split())
shark_input = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
pan = [[[] for i in range(C)] for _ in range(R)]
# 낚시왕 한칸 이동
# 땅과 가장 가까운 상어 잡기, 사라짐
# 상어 이동
shark = []
#  (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기이다. d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다.
while shark_input:
    r,c,s,d,z = shark_input.pop()
    pan[r-1][c-1].append([s,d,z])
result = 0
dx = [-1,1,0,0]
dy = [0,0,1,-1]
# 낚시왕 이동
for i in range(C):
    # 땅과 가장 가까운 상어 잡기
    for j in range(R):
        if pan[j][i]:
            s,d,z = pan[j][i].pop()
            result += z
            break
    # 상어 이동
    for j in range(R):
        for k in range(C):
            if pan[j][k]:
                s,d,z=pan[j][k].pop()
                shark.append([j,k,s,d,z])
    while shark:
        j,k,s,d,z = shark.pop()
        for _ in range(s):
            j = j+dx[d-1]
            k = k+dy[d-1]
            if k<0 or j<0 or j>R-1 or k>C-1:
                if d==1:
                    d=2
                elif d==2:
                    d=1
                elif d==3:
                    d=4
                elif d==4:
                    d=3
                j = j+2*dx[d-1]
                k = k+2*dy[d-1] 
                
        pan[j][k].append([s,d,z])
    # 같은 자리에 있는 상어 잡아먹기
    for j in range(R):
        for k in range(C):
            if len(pan[j][k])>=2:
                pan[j][k].sort(key=lambda x:-x[2])
                while len(pan[j][k])>1:
                    pan[j][k].pop()
print(result)
