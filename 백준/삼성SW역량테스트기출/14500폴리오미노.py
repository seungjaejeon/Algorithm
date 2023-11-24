import sys
N, M = map(int, sys.stdin.readline().split())
pan = []
for i in range(N):
    pan.append(list(map(int, sys.stdin.readline().split())))
    

# 완전탐색
polio = [[[0,0],[0,1],[0,2],[0,3]],[[0,0],[1,0],[2,0],[2,1]],[[0,0],[0,1],[1,0],[1,1]],[[0,0],[1,0],[1,1],[2,1]],[[0,0],[0,1],[0,2],[1,1]]]
# -> 오른쪽으로 회전하면 [[0,0],[0,1],[0,2],[1,2]] 안에 값이 swap됨
# 왼쪽으로 회전하면 [[0,0],[0,-1],[0,-2],[-1,-2]] 안에값 스왑하고 -붙임
# 180도 회전하면 [[0,0],[-1,0],[-2,0],[-2,-1]]됨 -만 붙임
# 좌우 반전하면 [[0,0],[1,0],[2,0],[2,-1]] 
# 상하 반전하면 [[0,0],[-1,0],[-2,0],[-2,1]]이다.
#도형 돌려보기

def turn(polio):
    for i in range(5):
        a, b, c, d, e, f, g, h = polio[i][0][0],polio[i][0][1],polio[i][1][0],polio[i][1][1],polio[i][2][0],polio[i][2][1],polio[i][3][0],polio[i][3][1]
        polio.append([[b,a],[d,c],[f,e],[h,g]])
        polio.append([[-b,-a],[-d,-c],[-f,-e],[-h,-g]])
        polio.append([[-a,-b],[-c,-d],[-e,-f],[-g,-h]])
        polio.append([[-a,b],[-c,d],[-e,f],[-g,h]])
        polio.append([[a,-b],[c,-d],[e,-f],[g,-h]])
        polio.append([[b,-a],[d,-c],[f,-e],[h,-g]])
        polio.append([[-b,a],[-d,c],[-f,e],[-h,g]])
def go(x, y):
    global answer
    for pol in polio:

        four = []
        count = 0
        for i in range(4):
            four.append([x+pol[i][0], y+pol[i][1]])

        for one in four:
            if one[0]<0 or one[1]<0 or one[0]>N-1 or one[1]>M-1:
                break
            count += pan[one[0]][one[1]]
        if count > answer:
            answer = count
            

answer = 0
turn(polio)
for x in range(N):
    for y in range(M):
        go(x,y)
print(answer)
