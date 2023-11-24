import sys
from collections import deque
F, S, G, U, D = map(int, sys.stdin.readline().split())
count = [0 for _ in range(F+1)] # 횟수 체크를 위한 배열
def bfs(): # 엘리베이터 이동을 위한 BFS
    global flag # 이동할 수 있는 위치인가를 확인하기 위한 flag
    q = deque()
    q.append(S)
    count[S]=1 # 초기값
    while q:
        cur = q.popleft()
        if cur == G: # G에 도착했다면
            flag = True # 도착할 수 있는 위치임을 나타내는 flag
            print(count[cur]-1) # 출력값
            break # 함수 종료
        for i in (U, -D): # 위, 아래로 이동
            next = cur + i # 층 수 
            if 1<=next<=F and count[next]==0: # 와본적이 없는 층수이고, 범위 내에 존재한다면
                count[next] = count[cur] + 1 # 횟수 1 증가
                q.append(next) # q에 추가하여 반복
flag = False # 초기값
bfs()
if flag==False: # 도착할 수 있는 위치가 아니라면
    print("use the stairs") # 계단 이용하세요