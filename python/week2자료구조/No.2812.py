import sys
N, K = map(int, sys.stdin.readline().split())
number = sys.stdin.readline().rstrip()
num = list(number)
result = [] # 결과를 저장할 리스트
need = N-K # 결과까지 필요한 남은 수
current_result = 0 # 결과의 현재 개수
result_index = 0
max_number = number[0]
while current_result < N-K:
    max_number = 0
    for i in range(result_index + 1, len(num)-need+1): # result로 가져간 다음 수 부터 결과를 채우지 못하는 수 이전까지
        if max_number < int(number[i]):
            max_number = int(number[i])
            result_index = i
    result.append(max_number)
    need -= 1
    current_result += 1
for i in result:
    print(i, end="")
