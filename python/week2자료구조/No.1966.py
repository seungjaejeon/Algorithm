# 프린터 큐
# n개의 문서중 m번째 인덱스가 몇번째로 빠져나갈까?
from collections import deque
import sys
N = int(sys.stdin.readline())
for i in range(N):
    count = 1
    n, m = map(int, sys.stdin.readline().split())
    q = deque(map(int, sys.stdin.readline().split()))
    while(True):
        if q[0] == max(q): # q의 0번째 인덱스가 max값이라면
            if m == 0: # 그 값이 심지어 m이다?
                print(count) # count값 출력
                break # 무한루프 종료
            q.popleft() # m이 아닌 제일 큰놈 pop
            count += 1 # count값 증가
            m -= 1 # 한명 빠졌으므로 m인덱스 감소
        else: # q의 0번째 인덱스가 max값이 아니라면 rotate
            q.append(q.popleft()) #q의 뒤에 제일 왼쪽 q값을 붙임
            m -= 1 # m인덱스 감소
            if m<0: # m이 0보다 작아지면 q의 뒤로 가므로 
                m = len(q) - 1