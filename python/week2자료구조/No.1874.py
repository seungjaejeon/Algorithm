import sys
n = int(sys.stdin.readline())
nums = [i+1 for i in range(n)] # 1부터 n까지 수열
h_nums = [] #have_nums 가지고 있는 수열
r_nums = [] # 입력된 수열을 만들기 위한 스택
result = [] #push,pop연산 저장리스트
j = 0
for i in range(n):#n번 반복
    have = True
    k = int(sys.stdin.readline()) # 입력값
    while have:
        if len(h_nums)==0: # 가지고 있는 수열이 0이라면
            h_nums.append(nums[j]) # nums값을 가지고 있는 수열에 append
            j += 1 # 인덱스증가
            result.append("+") #push
        if h_nums[len(h_nums)-1] != k:
            if(j>n-1):break #j가 인덱스 초과하면 반복문 탈출을 통해 NO출력
            h_nums.append(nums[j]) # nums값을 가지고 있는 수열에 append
            j += 1
            result.append("+") #push
        else:
            r_nums.append(h_nums.pop()) #결과수열에 가지고 있는 수열을 pop
            result.append("-") # pop
            have = False # while 반복문 탈출
if len(r_nums) != n:
    print("NO")
else: 
    for i in range(len(result)):
        print(result[i])

# 리스트를 3개를 만든다.
# 1부터 n까지 리스트, 스택에 저장후 pop해서 입력값의 리스트
# 스택에 저장할 리스트, 결과 (+, -)를 저장할 리스트
# for문으로 입력값을 받는다. 이때 while문으로 스택에 1부터 n까지의 리스트에서
# 하나씩 pop하며 입력값 k가 스택에 저장될때까지 pop한다. 스택에 저장되었다면
# 그 스택의 리스트의 마지막에 저장되었으므로 pop하여 입력값의 리스트에 저장한다.
# 각 연산시마다 +와 -를 결과를 저장할 리스트에 저장한다.
# 이를 n번 반복한다.

# 연산이 끝났을때 입력값의 리스트가 n개가 아니면 NO를 출력
# n개라면 모든 값들이 잘 들어간것이므로 result를 출력한다.
