import sys
T = int(sys.stdin.readline())
def dfs(x, y):
    global flag
    if abs(rock_x-x)+abs(rock_y-y)<=1000:
        flag = True
        return
    for i, address in enumerate(store):
        if abs(address[0]-x)+abs(address[1]-y)<=1000 and visited[i]==False:
            visited[i] = True
            dfs(address[0], address[1])

for _ in range(T):
    N = int(sys.stdin.readline())
    home_x, home_y = map(int, sys.stdin.readline().split())
    store = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
    rock_x, rock_y = map(int, sys.stdin.readline().split())
    flag = False
    visited = [False for i in range(N)]
    # 짧은 편의점 거리로 이동 맥주 20병충전
    store.sort(key=lambda x: abs(x[0]-home_x)+abs(x[1]-home_y))
    dfs(home_x, home_y)
    if flag==True:
        print("happy")
    else:
        print("sad")
    