'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''
for test_case in range(1, 11):
	N = int(input())
	building = list(map(int, input().split()))
	result = 0
	for i in range(2,N-2):
		left_best = max(building[i-1],building[i-2])
		right_best = max(building[i+1],building[i+2])
		best = max(left_best, right_best)
		if building[i]>best:
			result += building[i]-best
	print(f'#{test_case} {result}')