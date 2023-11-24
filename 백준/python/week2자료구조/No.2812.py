import sys
N, K = map(int, sys.stdin.readline().split())
number = sys.stdin.readline().rstrip()
result = [] # 결과를 저장할 리스트
k = K
for num in number:
    while k > 0 and result:
        if result[-1] < int(num):
            result.pop()
            k -= 1
        else: break
    result.append(int(num))
for i in result:
    print(i, end="")
