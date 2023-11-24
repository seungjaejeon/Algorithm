import sys
import itertools
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
cal_count = list(map(int, sys.stdin.readline().split()))
cal = ['+','-','*','//']
cal_besort = []
for i in range(4):
    for j in range(cal_count[i]):
        cal_besort.append(cal[i])
min_result = float('inf')
max_result = float("-inf")
for i in itertools.permutations(cal_besort,len(cal_besort)):
    result = A[0]
    A_index = 1
    for k in i:
        if k=='+':
            result += A[A_index]
            A_index+=1
        elif k=='-':
            result -= A[A_index]
            A_index+=1
        elif k=='*':
            result *= A[A_index]
            A_index+=1
        else:
            if result<0: #음수를 양수로 나누는 경우
                result = (-result)//A[A_index]
                result = -result
                A_index+=1
            else: #양수를 양수로 나누는 경우
                result = result//A[A_index]
                A_index+=1
    if min_result>result:
        min_result = result # 최소값
    if max_result<result:
        max_result = result # 최대값

#출력
print(max_result)
print(min_result)