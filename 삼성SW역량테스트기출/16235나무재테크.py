import sys
from collections import deque
N, M, K = map(int, sys.stdin.readline().split())
eat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 추가되는 양분
trees = [[[] for _ in range(N)] for i in range(N)]
for i in range(M):
    x,y,age = map(int, sys.stdin.readline().split())
    trees[x-1][y-1].append(age)
pan = [[5]*N for _ in range(N)]
die_trees = []
# 가장 처음 양분 = 5
# 사계절이란 순서를 말하는 것.
# 1. 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다. 각각의 나무는 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있다. 
# 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다. -> sort lambda
# 만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.

# 2. 봄에 죽은 나무가 양분으로 변하게 된다. 
# 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. 소수점 아래는 버린다.

# 3. 나무가 번식한다. 번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다. 
# 어떤 칸 (r, c)와 인접한 칸은 (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) 이다. 
# 상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.

# S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다. 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.
dx = [0,0,1,1,1,-1,-1,-1] # 8방향
dy = [1,-1,0,-1,1,1,-1,0]

def spring(): # 봄
    for i,line in enumerate(trees):
        for j, ages in enumerate(line):
            trees[i][j].sort()
            for k, age in enumerate(ages):
                if age<=pan[i][j]:
                    pan[i][j]-=age
                    trees[i][j][k]+=1
                else:
                    for _ in range(k,len(trees[i][j])):
                        die_trees.append([i,j,trees[i][j].pop()])
                    break
    
def summer(): # 여름
    while die_trees:
        x,y,age = die_trees.pop()
        pan[x][y]+=age//2 #양분화됨
def autumn(): # 가을
    for i,line in enumerate(trees):
        for j, ages in enumerate(line):
            for k, age in enumerate(ages):
                if age%5==0 and age!=0: #나이가 5의 배수
                    for t in range(8):
                        ni=i+dx[t]
                        nj=j+dy[t]
                        if ni>=N or nj>=N or ni<0 or nj<0:
                            continue
                        trees[ni][nj].append(1)

            pan[i][j] += eat[i][j] # 로봇이 양분 추가 winter

for _ in range(K):
    spring()
    summer()
    autumn()
result = 0
for i in range(N):
    for j in range(N):
        result += len(trees[i][j])
print(result)