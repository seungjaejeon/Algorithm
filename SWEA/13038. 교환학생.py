T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    week = list(map(int,input().split()))
    min_result = float('inf')
    for i, val in enumerate(week):
        if val == 1:
            result = 0
            index = i
            temp = N
            while temp:
                if week[index]==1:
                    temp-=1
                index =  (index+1)%7
                result += 1
            min_result = min(result, min_result)
    print(f'#{test_case} {min_result}')