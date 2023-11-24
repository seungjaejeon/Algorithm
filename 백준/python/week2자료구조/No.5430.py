import sys
from collections import deque
T = int(sys.stdin.readline())
for i in range(T):
    error = 1 # error인지 판단
    num = deque() # deque
    com = str(sys.stdin.readline().rstrip()) # 명령어
    N = int(sys.stdin.readline()) # 개수
    string = str(sys.stdin.readline().rstrip()) # 입력값
    for j in string: # 숫자만 num에 저장
        if ord(j) == 91 or ord(j) == 93 or ord(j) == 44:
            continue
        else:
            num.append(j)
    for k in com: # 명령어 해석
        if k == "R": # R이면 리버스
            num.reverse()
        if k == "D": # D이면 num이 존재한다면 popleft 없다면 error = 0
            if len(num) == 0 :
                error = 0
            else: num.popleft()
    if error == 1:
        print("[", end="")
        result = ",".join(map(str, num))
        print(result,end="")
        print("]")
    else:
        print("error")
