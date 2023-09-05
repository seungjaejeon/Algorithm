import sys
N, r, c = map(int, sys.stdin.readline().split())
# 0~2^N
# 0~2^N
temp = 0
def Z(n,x,y):
    global temp
    if x>r or x+(2**n)<=r or y>c or y+(2**n)<=c: # 재귀의 범위 내에 r,c가 없으면 temp에 그 넓이만큼 더해줌
        temp += (2**n)**2 # 길이의 제곱
        return # 부함수 종료
    if n == 1: # 2*2의 박스
        if x==r and y==c: # 1사분면
            print(temp)
        if x==r and y+1==c: # 2사분면
            print(temp+1)
        if x+1==r and y==c: # 3사분면
            print(temp+2)
        if x+1==r and y+1==c: # 4사분면
            print(temp+3)
        return # 종료
    else:
        n -= 1 # 4분의 1
        Z(n,x, y) # 1사분면
        Z(n,x, y+(2**n)) # 2사분면
        Z(n,x+(2**n), y) # 3사분면
        Z(n,x+(2**n), y+(2**n)) # 4사분면
        
Z(N, 0, 0)