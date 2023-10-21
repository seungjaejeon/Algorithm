result = []
for _ in range(10):
    # 도착 지점에 연결된 출발점을 찾아야 하기 때문에 도착점부터 탐색을 시작한다.
    test_case = int(input())
    ladder = []
    for i in range(100):
        line = list(map(int, input().split()))
        ladder.append(line)
    # d=1 => 왼 d=2 => 오른쪽, d=3 => 위
    def ladder_up(x,y,d):
        if d==3: # 위로쭉
            for i in range(x,-1,-1):
                if i==0:
                    result.append(y)
                if y-1>=0 and ladder[i][y-1]==1:
                    d=1 # 방향 왼쪽으로 틀고
                    ladder_up(i,y-1,d)
                    break
                elif y+1<=99 and ladder[i][y+1]==1:
                    d=2 # 방향 오른쪽으로 틀고
                    ladder_up(i,y+1,d)
                    break
        # 왼쪽으로 쭉
        elif d==1:
            for i in range(y,-1,-1):
                if ladder[x-1][i]==1:
                    d=3 # 위
                    ladder_up(x-1,i,d)
                    break
        elif d==2: #
            for i in range(y,100):
                if ladder[x-1][i]==1:
                    d=3
                    ladder_up(x-1,i,d)
                    break
    for i, val in enumerate(ladder[99]):
        if val == 2:
            ladder_up(99,i,3)
            break
    print(f'#{test_case} {result[test_case-1]}')
