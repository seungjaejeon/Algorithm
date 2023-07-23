# N개의 수 A1, A2, ..., AN과 L이 주어진다.

# Di = Ai-L+1 ~ Ai 중의 최솟값이라고 할 때, D에 저장된 수를 출력하는 프로그램을 작성하시오. 이때, i ≤ 0 인 Ai는 무시하고 D를 구해야 한다.
import sys
from collections import deque
N, L = map(int,sys.stdin.readline().split(" "))
A = list(map(int,sys.stdin.readline().split(" ")))
myDeque = deque()

# ([인덱스][값]) 형태로 myDeque에 데이터 관리
for i in range(N):

    # 새로운 값이 기존의 값보다 클 때까지 기존의 값 (끝에서부터) 제거
    while myDeque and myDeque[-1][0] > A[i]:
        myDeque.pop()
    myDeque.append((A[i], i))     # 새로운 값 입력

    # 슬라이딩 윈도우가 인덱스 범위에서 벗어난 경우 제거
    if myDeque[0][1] <= i-L:
        myDeque.popleft()

    print(myDeque, end=' ')